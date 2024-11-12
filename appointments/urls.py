from django.urls import path
from . import views

urlpatterns = [
    path('api/consultations/', views.ConsultationListView.as_view(), name='consultations-list'),
    path('api/consultations/<int:pk>/', views.ConsultationDetailView.as_view(), name='consultation-detail'),
    path('api/consultations/', views.ConsultationCreateView.as_view(), name='consultation-create'), # Adicionado o path para criação
]