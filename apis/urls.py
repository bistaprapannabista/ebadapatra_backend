from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('province',ProvinceViewSet)
router.register('district',DistrictViewSet)
router.register('local-government',LocalGovernmentViewSet)

urlpatterns = [
    path('',include(router.urls)),
]