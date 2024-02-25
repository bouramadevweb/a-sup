# from app_vaccins.models import ODS_Flux_total_dep, D_dates, Departement
# from django.db import IntegrityError

# try:
#     for ods_entry in ODS_Flux_total_dep.objects.all():
#         print(f"Insertion des données pour {ods_entry.date_fin_semaine}")
       
#         # Récupérez tous les objets correspondants avec le même libelle_departement
#         departement_instances = Departement.objects.filter(libelle_departement=ods_entry.libelle_departement)

#         # Traitez chaque objet correspondant
#         for departement_instance in departement_instances:
#             # Créez l'instance de D_dates avec la clé étrangère libelle_departement
#             d_dates_instance = D_dates(
#                 code_date=f"{departement_instance.libelle_departement}-{ods_entry.date_fin_semaine}",
#                 date_fin_semaine=ods_entry.date_fin_semaine,
#                 libelle_departement=departement_instance
#             )

#             # Enregistrez dans la base de données
#             d_dates_instance.save()

#     print('Fin d\'insertion des données de la table D_dates')
# except IntegrityError as e:
#     print(f"IntegrityError: {e}")
# else:
#     print('Insertion des données de la table D_dates terminée avec succès.')


# from app_vaccins.models import D_dates

# # Supprimer toutes les entrées de la table D_dates
# D_dates.objects.all().delete()

# print('Toutes les entrées de la table D_dates ont été supprimées.')

# from app_vaccins.models import ODS_Flux_total_dep, D_dates, Departement
# from django.db import IntegrityError

# # Récupérez toutes les dates de la table D_dates
# dates_enregistrees = set(D_dates.objects.values_list('date_fin_semaine', flat=True))

# try:
#     for ods_entry in ODS_Flux_total_dep.objects.all():
#         print(f"Insertion des données pour {ods_entry.date_fin_semaine}")

#         # Récupérez tous les objets correspondants avec le même libelle_departement
#         departement_instances = Departement.objects.filter(libelle_departement=ods_entry.libelle_departement)

#         # Traitez chaque objet correspondant
#         for departement_instance in departement_instances:
#             # Créez l'instance de D_dates avec la clé étrangère libelle_departement
#             d_dates_instance = D_dates(
#                 code_date=f"{departement_instance.libelle_departement}-{ods_entry.date_fin_semaine}",
#                 date_fin_semaine=ods_entry.date_fin_semaine,
#                 libelle_departement=departement_instance
#             )

#             # Enregistrez dans la base de données
#             d_dates_instance.save()

#     print('Fin d\'insertion des données de la table D_dates')

#     # Vérifiez les dates manquantes
#     dates_manquantes = set(ODS_Flux_total_dep.objects.values_list('date_fin_semaine', flat=True)) - dates_enregistrees
#     if dates_manquantes:
#         print(f"Dates manquantes : {dates_manquantes}")
#     else:
#         print('Aucune date manquante')

# except IntegrityError as e:
#     print(f"IntegrityError: {e}")
# else:
#     print('Insertion des données de la table D_dates terminée avec succès.')
# from app_vaccins.models import ODS_Flux_total_dep, D_dates, Departement
# from django.db import IntegrityError

# # Récupérez toutes les dates de la table D_dates
# dates_enregistrees = set(D_dates.objects.values_list('date_fin_semaine', flat=True))

# try:
#     for ods_entry in ODS_Flux_total_dep.objects.all():
#         print(f"Insertion des données pour {ods_entry.date_fin_semaine}")

#         # Récupérez tous les objets correspondants avec le même libelle_departement
#         departement_instances = Departement.objects.filter(libelle_departement=ods_entry.libelle_departement)

#         # Traitez chaque objet correspondant
#         for departement_instance in departement_instances:
#             # Créez l'instance de D_dates avec la clé étrangère libelle_departement
#             d_dates_instance = D_dates(
#                 code_date=f"{departement_instance.libelle_departement}-{ods_entry.date_fin_semaine}",
#                 date_fin_semaine=ods_entry.date_fin_semaine,
#                 libelle_departement=departement_instance
#             )

#             # Enregistrez dans la base de données
#             d_dates_instance.save()

#     print('Fin d\'insertion des données de la table D_dates')

#     # Vérifiez les dates manquantes
#     dates_manquantes = set(ODS_Flux_total_dep.objects.values_list('date_fin_semaine', flat=True)) - dates_enregistrees
#     if dates_manquantes:
#         print(f"Dates manquantes : {dates_manquantes}")
#     else:
#         print('Aucune date manquante')

# except IntegrityError as e:
#     print(f"IntegrityError: {e}")
# else:
#     print('Insertion des données de la table D_dates terminée avec succès.')
from app_vaccins.models import ODS_Flux_total_dep, D_dates, Departement
from django.db import IntegrityError

try:
    for ods_entry in ODS_Flux_total_dep.objects.all():
        print(f"Insertion des données pour {ods_entry.date_fin_semaine}")

        for departement_instance in Departement.objects.filter(libelle_departement=ods_entry.libelle_departement):
            # Vérifiez si la date existe déjà
            existing_date = D_dates.objects.filter(code_date=f"{departement_instance.libelle_departement}-{ods_entry.date_fin_semaine}")

            if existing_date.exists():
                d_dates_instance = existing_date.first()
            else:
                # Créez une nouvelle instance de D_dates
                d_dates_instance = D_dates(
                    code_date=f"{departement_instance.libelle_departement}-{ods_entry.date_fin_semaine}",
                    date_fin_semaine=ods_entry.date_fin_semaine,
                    libelle_departement=departement_instance
                )

                # Enregistrez dans la base de données
                d_dates_instance.save()

    print('Fin d\'insertion des données de la table D_dates')

except IntegrityError as e:
    print(f"IntegrityError: {e}")

else:
    print('Insertion des données de la table D_dates terminée avec succès.')
