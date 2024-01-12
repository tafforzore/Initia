
from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Type(models.Model):
    nom = models.CharField(max_length=200)  
    
    def __str__(self):
        return self.nom


# Create your models here.
class Utilisateurs(models.Model):
    username = models.CharField(max_length=10000)
    nom = models.CharField(max_length=1000000)
    prenom = models.CharField(max_length=1000000, default=None)
    numeros = models.IntegerField()
    pays = models.CharField(max_length=1000000)

    def __str__(self):
        return self.username  

    # class Meta:
    #     verbose_name = 'Utilisateurs'
    #     verbose_name_plural = 'Utilisateurs'

class Projet(models.Model):
    nom = models.CharField(max_length=1000000) 
    montant_actuel = models.IntegerField(default = 0) 
    objectif = models.TextField(max_length=1000000)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    photos = models.ImageField(height_field=None, width_field=None, max_length=None,  upload_to='image')
    montant_projet = models.IntegerField()
    

    def __str__(self):
        return self.nom

    
class Produit(models.Model):
    nom = models.CharField(max_length=1000000)  
    petite_description = models.CharField(max_length=80)
    grande_description = models.TextField(max_length=1000000)
    photos = models.ImageField(height_field=None, width_field=None, max_length=None, upload_to='image')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    couverture_principale = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class Phase(models.Model):
    nom_projet = models.ForeignKey(Projet, on_delete=models.CASCADE) 
    nom_phases = models.CharField(max_length=1000000)  
    debut = models.DateField()
    fin = models.DateField()
    statut =  models.BooleanField(default=False)
    montant = models.BigIntegerField(default=100)

    def __str__(self):
        return self.nom_phases


class Investissement(models.Model):
    jour = models.DateField()
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    email_personne = models.ForeignKey(User, on_delete=models.CASCADE) 
    payment_ref = models.CharField(max_length=1000000)
    montant = models.IntegerField()  
    nombre_part = models.IntegerField()
