from django.urls import path
from . import views

urlpatterns = [
    path('hazards/', views.HazardListView.as_view(), name='hazard_list'),
    path('hazards/new/', views.HazardCreateView.as_view(), name='hazard_create'),
    path('hazards/<int:pk>/', views.HazardDetailView.as_view(), name='hazard_detail'),
    path('hazards/<int:pk>/add_note/', views.AddMitigationNoteView.as_view(), name='add_note'),
]
