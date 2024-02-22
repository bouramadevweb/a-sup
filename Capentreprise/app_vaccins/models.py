from django.db import models

# Create your models here.
class ODS_Flux_total_dep(models.Model):
    code_region = models.CharField(max_length=250)
    libelle_region = models.CharField(max_length=250)
    code_departement = models.CharField(max_length=250)
    libelle_departement = models.CharField(max_length=250)
    date_fin_semaine = models.CharField(max_length=250)
    type_de_vaccin = models.CharField(max_length=250)
    nb_ucd = models.CharField(max_length=250)
    nb_doses = models.CharField(max_length=250)
    def __str__(self) :
        return self.code_region + self.libelle_region + self.code_departement + self.libelle_departement 
    