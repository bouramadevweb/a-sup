from app_vaccins.models import ODS_Flux_total_dep, D_dates, Departement, F_doses, D_type_vaccin
import pandas as pd

try:
    for ods_entry in ODS_Flux_total_dep.objects.all():
        print(f"Insertion des données pour {ods_entry.date_fin_semaine}")

        # Récupérez tous les objets correspondants avec le même libelle_departement
        departement_instances = Departement.objects.filter(libelle_departement=ods_entry.libelle_departement)

        # Traitez chaque objet correspondant
        for departement_instance in departement_instances:
            # Créez l'instance de D_dates avec la clé étrangère libelle_departement
            code_date = f"{departement_instance.libelle_departement}-{ods_entry.date_fin_semaine}"

            # Vérifiez l'existence de l'instance D_dates
            d_dates_instance, created_date = D_dates.objects.get_or_create(
                pk_date=ods_entry.date_fin_semaine,
                defaults={'code_date': code_date}
            )

            print(f"Comparaison pour {ods_entry.date_fin_semaine}, {departement_instance.libelle_departement}, {ods_entry.type_de_vaccin}")

            # Traitement des valeurs 'nan'
            nb_ucd = pd.to_numeric(ods_entry.nb_ucd, errors='coerce')
            nb_doses = pd.to_numeric(ods_entry.nb_doses, errors='coerce')

            # Replace NaN with 0
            nb_ucd = 0 if pd.isna(nb_ucd) else int(nb_ucd)
            nb_doses = 0 if pd.isna(nb_doses) else int(nb_doses)

            # Vérifiez l'existence de l'instance F_doses
            pk_F_doses = f"{departement_instance.pk_departement}_{ods_entry.type_de_vaccin}_{ods_entry.date_fin_semaine}"
            if not F_doses.objects.filter(pk_F_doses=pk_F_doses).exists():
                f_doses_instance = F_doses(
                    pk_F_doses=pk_F_doses,
                    nb_ucd=nb_ucd,
                    nb_doses=nb_doses,
                    code_departement=departement_instance,
                    pk_type_vaccin=D_type_vaccin.objects.get(pk_type_vaccin=ods_entry.type_de_vaccin),
                    pk_date=d_dates_instance
                )
                f_doses_instance.save()
                print(f"Nouvelle instance de F_doses créée pour {ods_entry.date_fin_semaine}")
            else:
                print(f"Instance existante de F_doses pour {ods_entry.date_fin_semaine}")

    print('Fin d\'insertion des données de la table F_doses')
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
else:
    print('Insertion des données de la table F_doses terminée avec succès.')





# from app_vaccins.models import F_doses

# #Delete all records from the F_doses table
# F_doses.objects.all().delete()

# print('All records from F_doses table have been deleted.')

