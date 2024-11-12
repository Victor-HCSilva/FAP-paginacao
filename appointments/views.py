from django.db import models
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Patient, Doctor, Consultation
from .serializers import ConsultationSerializer

# --------------------------------------------------------------------
# View para listar e criar consultas (com paginação, busca e ordenação)
class ConsultationListView(generics.ListCreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 2  # Define o tamanho da página
    filter_backends = [SearchFilter, OrderingFilter]  # Define os filtros
    search_fields = ['patient__name', 'doctor__name', 'description']  # Campos para busca
    ordering_fields = ['date', 'time']  # Campos para ordenação

# --------------------------------------------------------------------
# View para visualizar, atualizar e excluir consultas
class ConsultationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

# --------------------------------------------------------------------
# View para criar consultas
class ConsultationCreateView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer