from app_vaccins.models import D_type_vaccin ,ODS_Flux_total_dep
from django.db import IntegrityError

try:
    for D_type_vaccin_entry in ODS_Flux_total_dep.objects.all():
        print(f"Insertion des données pour {D_type_vaccin_entry.type_de_vaccin}")
       
        D_type_vaccin_instance = D_type_vaccin(
            pk_type_vaccin=D_type_vaccin_entry.type_de_vaccin
        )

        # Enregistrez dans la base de données
        D_type_vaccin_instance.save()

    print('Fin d\'insertion des données de la table D_type_vaccin')
except IntegrityError as e:
    print(f"IntegrityError: {e}")
else:
    print('Insertion des données de la table D_type_vaccin terminée avec succès.')