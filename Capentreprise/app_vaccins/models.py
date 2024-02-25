from django.db import models

# Create your models here.
class ODS_Flux_total_dep(models.Model):
    """_summary_

    Args:
        models (_type_): ODS

    Returns:
        _type_: _description_
    """
    code_region = models.CharField(max_length=250)
    code_departement = models.CharField(max_length=250)
    libelle_region = models.CharField(max_length=250)
    libelle_departement = models.CharField(max_length=250)
    date_fin_semaine = models.CharField(max_length=250)
    type_de_vaccin = models.CharField(max_length=250)
    nb_ucd = models.CharField(max_length=250)
    nb_doses = models.CharField(max_length=250)
    def __str__(self) :
        return self.code_region + self.libelle_region + self.code_departement + self.libelle_departement 
class Departement(models.Model):
    pk_departement = models.CharField(primary_key=True, max_length=250, unique=True, default=None)
    code_departement = models.CharField(max_length=250, default=None)
    code_region = models.CharField(max_length=250, default=None)
    libelle_region = models.CharField(max_length=250, default=None)
    libelle_departement = models.CharField(max_length=250, default=None)

    def save(self, *args, **kwargs):
        # Générer la clé primaire de manière unique
        self.pk_departement = f'{self.code_departement}-{self.libelle_region}-{self.code_region}-{self.libelle_departement}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.libelle_departement}-{self.libelle_region}-{self.libelle_departement}'

class D_type_vaccin(models.Model):
    """_summary_

    Args:
        models (_type_): Vaccins

    Returns:
        _type_: le type du vaccin
    """
    pk_type_vaccin = models.CharField(primary_key=True,max_length=250)
    def __str__(self):
        return f'{self.pk_type_vaccin}'
    
class D_dates(models.Model):
    pk_date = models.DateField(primary_key=True, default='1900-01-01')

    def __str__(self):
        return f'{self.pk_date}'   

class F_doses(models.Model):
    """_summary_

    Args:
        models (_type_): F_doses du vaccin
    """
    pk_F_doses = models.CharField(primary_key=True,max_length=250)
    nb_ucd = models.IntegerField()
    nb_doses = models.IntegerField()
    code_departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    pk_type_vaccin = models.ForeignKey(D_type_vaccin, on_delete=models.CASCADE)
    pk_date = models.ForeignKey(D_dates,default='1900-01-01' ,on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
       
        self.pk_F_doses = f"{self.code_departement}_{self.pk_type_vaccin}_{self.pk_date}"
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.pk_F_doses},semaine {self.pk_date},doses {self.nb_doses},ucd {self.nb_ucd}'