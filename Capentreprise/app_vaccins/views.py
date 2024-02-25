# app_vaccins/views.py
# views.py

from django.shortcuts import render
from .models import ODS_Flux_total_dep, Departement, D_type_vaccin, D_dates, F_doses
from django.db.models import Sum
from itertools import groupby
from operator import itemgetter

def display_ods(request):
    ods_flux_total_dep = ODS_Flux_total_dep.objects.all()

    context = {
        'ods_flux_total_dep': ods_flux_total_dep,
    }
    return render(request, 'ods_template.html', context)

# Ajoutez des vues similaires pour les autres tables.





def total_vaccines_per_department(request):
    department_details = {}

    # Obtenez toutes les instances de Departement
    departments = Departement.objects.all()

    for department in departments:
        # Calculez le total des doses pour chaque département
        total_doses = F_doses.objects.filter(code_departement=department).aggregate(Sum('nb_doses'))['nb_doses__sum']
        
        # Si le total des doses est None, remplacez-le par zéro
        total_doses = total_doses if total_doses is not None else 0

        # Obtenez toutes les doses pour chaque département
        doses = F_doses.objects.filter(code_departement=department)

        # Ajoutez les détails du département au dictionnaire
        department_details[department] = {
            'libelle_departement': department.libelle_departement,
            'total_vaccines': total_doses,
            'doses': doses,
        }

    context = {
        'department_details': department_details,
    }

    return render(request, 'total_vaccines_per_department.html', context)
