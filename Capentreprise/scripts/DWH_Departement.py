# from app_vaccins.models import Departement ,ODS_Flux_total_dep
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
from app_vaccins.models import Departement, ODS_Flux_total_dep
from django.db import IntegrityError

try:
    for departement_entry in ODS_Flux_total_dep.objects.all():
        print(f"Insertion des données pour {departement_entry.code_departement}-{departement_entry.code_region}")

        # Vérifier si le département existe déjà
        departement_instance, created = Departement.objects.get_or_create(
            code_departement=departement_entry.code_departement,
            code_region=departement_entry.code_region,
            libelle_region=departement_entry.libelle_region,
            libelle_departement=departement_entry.libelle_departement
        )

        if not created:
            print(f"Le département {departement_instance.pk_departement} existe déjà.")
        else:
            print(f"Insertion des données pour {departement_instance.pk_departement}")

except IntegrityError as e:
    print(f"IntegrityError: {e}")
else:
    print('Fin d\'insertion des données de la table Departement')
