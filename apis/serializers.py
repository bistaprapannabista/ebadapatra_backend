from rest_framework import serializers

from .models import Province, District, LocalGovernment

class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    province = ProvinceSerializer()
    class Meta:
        model = District
        fields = '__all__'


class LocalGovernmentSerializer(serializers.HyperlinkedModelSerializer):
    province = ProvinceSerializer()
    district = DistrictSerializer()
    class Meta:
        model = LocalGovernment
        fields = '__all__'