from django.urls import include, path
from .views import *

urlpatterns = [
    path('',ManagePerson.index, name='indexe'),
    path('ajouter_personnel/',ManagePerson.ajouter, name='ajouter_personnel'),
    path('modifier_personnel/',ManagePerson.modifier, name='modifier_personnel'),
    path('update_person/',ManagePerson.fom_modif_personne, name='update_personnel'),
    path('ajouter_activiter/',ManageActiviter.ajouter, name='ajouter_activiter'),
]