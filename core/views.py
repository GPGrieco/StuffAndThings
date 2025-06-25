from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Hazard, HazardPhoto
from .forms import HazardForm, MitigationNoteForm

class HazardListView(ListView):
    model = Hazard
    template_name = 'hazards/hazard_list.html'
    context_object_name = 'hazards'

class HazardDetailView(DetailView):
    model = Hazard
    template_name = 'hazards/hazard_detail.html'

class HazardCreateView(View):
    def get(self, request):
        form = HazardForm()
        return render(request, 'hazards/hazard_form.html', {'form': form})

    def post(self, request):
        form = HazardForm(request.POST, request.FILES)
        if form.is_valid():
            hazard = form.save()
            for file in request.FILES.getlist('photos'):
                HazardPhoto.objects.create(hazard=hazard, image=file)
            return redirect('hazard_detail', pk=hazard.pk)
        return render(request, 'hazards/hazard_form.html', {'form': form})

class AddMitigationNoteView(View):
    def post(self, request, pk):
        hazard = get_object_or_404(Hazard, pk=pk)
        form = MitigationNoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.hazard = hazard
            note.save()
        return redirect('hazard_detail', pk=pk)
