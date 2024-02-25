# from app_vaccins.models import ODS_Flux_total_dep, D_dates, Departement, F_doses, D_type_vaccin
# from django.db import IntegrityError
import pandas as pd

# try:
#     for ods_entry in ODS_Flux_total_dep.objects.all():
#         print(f"Insertion des données pour {ods_entry.date_fin_semaine}")

#         # Récupérez tous les objets correspondants avec le même libelle_departement
#         departement_instances = Departement.objects.filter(libelle_departement=ods_entry.libelle_departement)

#         # Traitez chaque objet correspondant
#         for departement_instance in departement_instances:
#             # Créez l'instance de D_dates avec la clé étrangère libelle_departement
#             code_date = f"{departement_instance.libelle_departement}-{ods_entry.date_fin_semaine}"

#             # Check if the record already exists
#             if not D_dates.objects.filter(code_date=code_date).exists():
#                 print(f"Comparaison pour {ods_entry.date_fin_semaine}, {departement_instance.libelle_departement}, {ods_entry.type_de_vaccin}")

#                 d_dates_instance = D_dates(
#                     code_date=code_date,
#                     date_fin_semaine=ods_entry.date_fin_semaine,
#                     libelle_departement=departement_instance
#                 )
#                 d_dates_instance.save()

#                 # Traitement des valeurs 'nan'
#                 nb_ucd = pd.to_numeric(ods_entry.nb_ucd, errors='coerce')
#                 nb_doses = pd.to_numeric(ods_entry.nb_doses, errors='coerce')

#                 # Replace NaN with 0
#                 nb_ucd = 0 if pd.isna(nb_ucd) else int(nb_ucd)
#                 nb_doses = 0 if pd.isna(nb_doses) else int(nb_doses)

#                 # Créez l'instance de F_doses avec les clés étrangères correspondantes
#                 f_doses_instance = F_doses(
#                     nb_ucd=nb_ucd,
#                     nb_doses=nb_doses,
#                     pk_departement=departement_instance,
#                     pk_type_vaccin=D_type_vaccin.objects.get(pk_type_vaccin=ods_entry.type_de_vaccin),
#                     pk_date=d_dates_instance
#                 )

#                 # Enregistrez dans la base de données
#                 f_doses_instance.save()

#     print('Fin d\'insertion des données de la table F_doses')
# except IntegrityError as e:
#     print(f"IntegrityError: {e}")
# else:
#     print('Insertion des données de la table F_doses terminée avec succès.')



# from app_vaccins.models import F_doses

# #Delete all records from the F_doses table
# F_doses.objects.all().delete()

# print('All records from F_doses table have been deleted.')

from app_vaccins.models import ODS_Flux_total_dep, D_dates, Departement, F_doses, D_type_vaccin
from django.db import IntegrityError
import pandas as pd  # Ajout de l'import pour pandas

try:
    for ods_entry in ODS_Flux_total_dep.objects.all():
        print(f"Insertion des données pour {ods_entry.date_fin_semaine}")

        # Récupérez tous les objets correspondants avec le même libelle_departement
        departement_instances = Departement.objects.filter(libelle_departement=ods_entry.libelle_departement)

        # Convertissez les champs nb_ucd et nb_doses en nombres
        nb_ucd = pd.to_numeric(ods_entry.nb_ucd, errors='coerce')
        nb_doses = pd.to_numeric(ods_entry.nb_doses, errors='coerce')

        # Remplacez NaN par 0
        nb_ucd = 0 if pd.isna(nb_ucd) else int(nb_ucd)
        nb_doses = 0 if pd.isna(nb_doses) else int(nb_doses)

        # Traitez chaque objet correspondant
        for departement_instance in departement_instances:
            # Utilisez get_or_create pour récupérer une instance existante ou en créer une nouvelle
            d_dates_instance, created = D_dates.objects.get_or_create(
                code_date=f"{departement_instance.libelle_departement}-{ods_entry.date_fin_semaine}",
                defaults={
                    'date_fin_semaine': ods_entry.date_fin_semaine,
                    'libelle_departement': departement_instance
                }
            )

            # Créez l'instance de F_doses avec les clés étrangères correspondantes
            f_doses_instance = F_doses(
                nb_ucd=nb_ucd,
                nb_doses=nb_doses,
                pk_departement=departement_instance,
                pk_type_vaccin=D_type_vaccin.objects.get(pk_type_vaccin=ods_entry.type_de_vaccin),
                pk_date=d_dates_instance
            )

            # Enregistrez dans la base de données
            f_doses_instance.save()

    print('Fin d\'insertion des données de la table F_doses')

except IntegrityError as e:
    print(f"IntegrityError: {e}")

else:
    print('Insertion des données de la table F_doses terminée avec succès.')
