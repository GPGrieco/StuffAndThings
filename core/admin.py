from django.contrib import admin
from .models import (
    Hazard, HazardPhoto, MitigationNote,
    CrewMember, PatrolShift, Incident,
    Supplier, Item, Transaction,
)

admin.site.register(Hazard)
admin.site.register(HazardPhoto)
admin.site.register(MitigationNote)
admin.site.register(CrewMember)
admin.site.register(PatrolShift)
admin.site.register(Incident)
admin.site.register(Supplier)
admin.site.register(Item)
admin.site.register(Transaction)
