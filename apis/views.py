from rest_framework import viewsets

from .serializers import DistrictSerializer,ProvinceSerializer, LocalGovernmentSerializer
from .models import District, Province, LocalGovernment

# Create your views here.

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class LocalGovernmentViewSet(viewsets.ModelViewSet):
    queryset = LocalGovernment.objects.all()
    serializer_class = LocalGovernmentSerializer

