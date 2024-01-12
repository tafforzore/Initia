from django.shortcuts import render,get_object_or_404, redirect
from .models import *

# Create your views here.

class ManagePerson:
    def index(request):
        ListePersonnel = Personnel.objects.all()
        ListeActivite = Activite.objects.all()
        personne_travaille = Personne_Travaille.objects.all()

        activite_journaliere = Jour_Heure.objects.all()

        print(personne_travaille)
        return render(request, 'blank.html',{
            'liste_personel':ListePersonnel,
            'liste_activite':ListeActivite,
            'personne_travaille':personne_travaille,
            'activite_journaliere':activite_journaliere
        })
    
    def ajouter(request):
        if request.method =='POST':
            nom = request.POST['nom']
            prenom = request.POST['prenom']

            new_personne = Personnel(
                nom = nom,
                prenom = prenom
            )
            new_personne.save()

            return redirect('indexe')


    def modifier(request):
        if request.method == 'POST':
            if 'Desactiver' in request.POST:
                identifiant = request.POST['identifiant']
                personne = get_object_or_404(Personnel, id=identifiant)
                personne.desactivation = True
                personne.save()
                return redirect('indexe')
            
            if 'Modifier' in request.POST:
                identifiant = request.POST['identifiant']
                return ManagePerson.modif_page(request,identifiant)
        pass

    def modif_page(request,identifiant):
        personne = Personnel.objects.get(id=identifiant)
        print(personne.id)
        return render(request, 'modifier.html',{
            'nom':personne.nom,
            'prenom':personne.prenom,
            'identifiant': personne.id
        })
    
    def fom_modif_personne(request):
        if request.method == 'POST':
            nom = request.POST['nom']
            prenom = request.POST['prenom']
            identifiant = request.POST['identifiant']

            personne = get_object_or_404(Personnel, id=identifiant)
            personne.nom = nom
            personne.prenom = prenom
            personne.save()

            return redirect('indexe')
        pass


class ManageActiviter:
    def ajouter(request):
        if request.method == 'POST':
            nom = request.POST['nom']
            activite = Activite(
                nom = nom
            )
            activite.save()

            return redirect('indexe')