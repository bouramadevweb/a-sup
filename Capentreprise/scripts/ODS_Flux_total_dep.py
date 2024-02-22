import os
import pandas as pd
from app_vaccins.models import ODS_Flux_total_dep
from  Capentreprise.settings import DATA_DIR

def run():
    """Lire un fichier CSV, traiter les données et insérer dans le modèle Django ODS."""
    try:
        # Définir le chemin du fichier CSV
        csv_file_path = os.path.join(DATA_DIR, 'flux-total-dep.csv')

        # Lire le fichier CSV dans un DataFrame pandas
        df = pd.read_csv(csv_file_path, sep=',',dtype=str,encoding="ISO-8859-1")
        print(df.head())

        # Créer une liste pour stocker les objets ODS
        my_ods = []

        # Iterer sur les lignes du DataFrame et créer des objets ODS
        for index, row in df.iterrows():
            ods = ODS_Flux_total_dep(
                code_region = row['code_region'],
                libelle_region = row['libelle_region'],
                code_departement = row['code_departement'],
                libelle_departement = row['libelle_departement'],
                date_fin_semaine = row['date_fin_semaine'],
                type_de_vaccin = row['type_de_vaccin'],
                nb_ucd = row['nb_ucd'],
                nb_doses = row['nb_doses'],
                
            )
            my_ods.append(ods)

        ODS_Flux_total_dep.objects.bulk_create(my_ods)
        print("Insertion des données réussie.")

    except Exception as e:
        print(f"Une erreur s'est produite: {str(e)}")

if __name__ == "__main__":
    run()

