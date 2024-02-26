from app_vaccins.models import Departement ,ODS_Flux_total_dep
# from django.db import IntegrityError

# try:
#     for departement_entry in ODS_Flux_total_dep.objects.all():
#         print(f"insertion des donnée pour {departement_entry.code_departement}-{departement_entry.code_region}")
       
#         departement_instance = Departement(
           
                
#             code_departement=departement_entry.code_departement,
#             code_region=departement_entry.code_region,
#             libelle_region=departement_entry.libelle_region,
#             libelle_departement=departement_entry.libelle_departement
#         )

#         # Enregistrez dans la base de données
#         departement_instance.save()

#     print('Fin d\'insertion des données de la table Departement')
# except IntegrityError as e:
#     print(f"IntegrityError: {e}")
# else:
#     print('Insertion des données de la table Departement terminée avec succès.')

# # from app_vaccins.models import Departement

# # # Supprimer toutes les entrées de la table Departement
# # Departement.objects.all().delete()
# from app_vaccins.models import Departement, ODS_Flux_total_dep
# from django.db import IntegrityError

# try:
#     for departement_entry in ODS_Flux_total_dep.objects.all():
#         print(f"Insertion des données pour {departement_entry.code_region}-{departement_entry.code_departement}")

#         # Créer un département avec les données de ODS_Flux_total_dep
#         departement_instance = Departement(
#             code_departement=departement_entry.code_departement,
#             code_region=departement_entry.code_region,
#             libelle_region=departement_entry.libelle_region,
#             libelle_departement=departement_entry.libelle_departement
#         )

#         # Générer la clé primaire de manière unique
#         departement_instance.save()

#         print(f"Insertion des données pour {departement_instance.pk_departement}")

# except IntegrityError as e:
#     print(f"Erreur d'intégrité : {e}")
# else:
#     print('Fin d\'insertion des données de la table Departement')

from app_vaccins.models import Departement, ODS_Flux_total_dep
from django.db import IntegrityError

try:
    for departement_entry in ODS_Flux_total_dep.objects.all():
        print(f"Insertion des données pour {departement_entry.code_region}-{departement_entry.code_departement}")

        # Pad single-digit values with leading zeros if length is less than three
        padded_code_departement = str(departement_entry.code_departement).zfill(2) if len(str(departement_entry.code_departement)) < 3 else str(departement_entry.code_departement)

        departement_instance, created = Departement.objects.get_or_create(
            code_departement=padded_code_departement,
            defaults={
                'code_region': departement_entry.code_region,
                'libelle_region': departement_entry.libelle_region,
                'libelle_departement': departement_entry.libelle_departement,
            }
        )

        if created:
            print(f"Insertion des données pour {departement_instance.pk_departement}")
        else:
            print(f"Le département {departement_instance.pk_departement} existe déjà.")

except IntegrityError as e:
    print(f"Erreur d'intégrité : {e}")
else:
    print('Fin d\'insertion des données de la table Departement')
