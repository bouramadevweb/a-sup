from rest_framework import serializers
from app_vaccins.models import Departement, ODS_Flux_total_dep, D_dates,F_doses,D_type_vaccin
        
class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields =  '__all__'
class ODS_Flux_total_depSerializer(serializers.ModelSerializer):
    class Meta:
        model = ODS_Flux_total_dep
        fields =  '__all__'
class D_datesSerializer(serializers.ModelSerializer):
    class Meta:
        model = D_dates
        fields =  '__all__'
class F_dosesSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_doses
        fields =  '__all__'
class D_type_vaccinSerializer(serializers.ModelSerializer):
    class Meta:
        model = D_type_vaccin
        fields =  '__all__'
         



