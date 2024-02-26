from django.contrib import admin

# Register your models here.
from app_vaccins.models import Departement, ODS_Flux_total_dep, D_dates,F_doses,D_type_vaccin
admin.site.register(ODS_Flux_total_dep)
admin.site.register(Departement)
admin.site.register(F_doses)
admin.site.register(D_dates)
admin.site.register(D_type_vaccin)