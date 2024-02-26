from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from app_vaccins.models import Departement, ODS_Flux_total_dep, D_dates,F_doses,D_type_vaccin
from .serializers import DepartementSerializer, ODS_Flux_total_depSerializer, D_datesSerializer, F_dosesSerializer, D_type_vaccinSerializer 
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
class DepartementList(ListModelMixin,CreateModelMixin, GenericAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    def get(self, request):
        departements = Departement.objects.all()
        serializer = DepartementSerializer(departements, many=True)
        return Response(serializer.data)
class ODS_Flux_total_depList(ListModelMixin,CreateModelMixin, GenericAPIView):
    queryset = ODS_Flux_total_dep.objects.all()
    serializer_class = ODS_Flux_total_depSerializer
    def get(self, request):
        ODS_Flux_total_dep = ODS_Flux_total_dep.objects.all()
        serializer = ODS_Flux_total_depSerializer(ODS_Flux_total_dep, many=True)
        return Response(serializer.data)
class D_datesList(ListModelMixin,CreateModelMixin, GenericAPIView):
    queryset = D_dates.objects.all()
    serializer_class = D_datesSerializer
    def get(self, request):
        D_dates = D_dates.objects.all()
        serializer = D_datesSerializer(D_dates, many=True)
        return Response(serializer.data)
class F_dosesList(ListModelMixin,CreateModelMixin, GenericAPIView):
    queryset = F_doses.objects.all()
    serializer_class = F_dosesSerializer
    def get(self, request):
        F_doses = F_doses.objects.all()
        serializer = F_dosesSerializer(F_doses, many=True)
        return Response(serializer.data)
class F_vaccinsList(ListModelMixin,CreateModelMixin, GenericAPIView):
    queryset = D_type_vaccin.objects.all()
    serializer_class = D_type_vaccinSerializer
    def get(self, request):
        F_vaccins = D_type_vaccinSerializer.objects.all()
        serializer = D_type_vaccinSerializer(F_vaccins, many=True)
        return Response(serializer.data)
    
        
    
