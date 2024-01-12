from django.contrib import admin
from .models import Utilisateurs,Projet, Investissement, Produit, Type, Phase

# Register your models here.
@admin.register(Utilisateurs)
class Useradmin(admin.ModelAdmin):
    list_display = ('id','username','nom','prenom','numeros')

@admin.register(Projet)
class Projetadmin(admin.ModelAdmin):
    list_display = ('id','nom','montant_actuel','objectif','montant_projet','type','photos')

@admin.register(Investissement)
class Ivestisementadmin(admin.ModelAdmin):
    list_display = ('id','jour','montant','email_personne','payment_ref','projet')

@admin.register(Produit)
class Produitadmin(admin.ModelAdmin):
    list_display = ('id','nom','petite_description','grande_description','photos','type','couverture_principale')

@admin.register(Type)
class typeadmin(admin.ModelAdmin):
    list_display = ('id','nom')

@admin.register(Phase)
class typeadmin(admin.ModelAdmin):
    list_display = ('id','nom_phases','debut','fin','statut','montant','nom_projet')
