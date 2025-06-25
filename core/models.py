from django.db import models

# Hazard tracking models
class Hazard(models.Model):
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('med', 'Medium'),
        ('high', 'High'),
        ('closed', 'Area Closed'),
    ]
    STATUS_CHOICES = [
        ('logged', 'Logged'),
        ('progress', 'In Progress'),
        ('mitigated', 'Mitigated'),
    ]
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='logged')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hazard {self.id} ({self.severity})"

class HazardPhoto(models.Model):
    hazard = models.ForeignKey(Hazard, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='hazard_photos/')

class MitigationNote(models.Model):
    hazard = models.ForeignKey(Hazard, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField()
    photo = models.ImageField(upload_to='hazard_notes/', blank=True, null=True)
    author_name = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

# Patrol scheduling models
class CrewMember(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class PatrolShift(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    crew = models.ManyToManyField(CrewMember, related_name='shifts')

    def __str__(self):
        return f"Shift {self.start}"

class Incident(models.Model):
    CATEGORY_CHOICES = [
        ('trespasser', 'Trespasser'),
        ('fence', 'Fence Damage'),
        ('other', 'Other'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    photo = models.ImageField(upload_to='incident_photos/', blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)
    shift = models.ForeignKey(PatrolShift, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Incident {self.id} ({self.category})"

# Inventory models
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    total_quantity = models.IntegerField()
    low_stock_threshold = models.IntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='transactions')
    out_by = models.CharField(max_length=100)
    out_datetime = models.DateTimeField(auto_now_add=True)
    expected_return = models.DateTimeField(null=True, blank=True)
    in_datetime = models.DateTimeField(null=True, blank=True)
    out_notes = models.TextField(blank=True)
    out_photo = models.ImageField(upload_to='transaction_photos/out/', blank=True, null=True)
    in_notes = models.TextField(blank=True)
    in_photo = models.ImageField(upload_to='transaction_photos/in/', blank=True, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} by {self.out_by}"
