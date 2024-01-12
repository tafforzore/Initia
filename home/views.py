from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from theme_pixel.models import Phase, Utilisateurs, Investissement

# Create your views here.

def index(request):

    phases = Phase.objects.all()
    nb_user = Utilisateurs.objects.all()

    ####montant investit
    montant_all = Investissement.objects.all()
    montants = 0
    for montant in montant_all:
        montants = montants + int(montant.montant)

    #### nombre de pays actifs
    pays = 5
    
    dico = {    
        'phases':phases,
        'user_count': nb_user.count(),
        'montants_investit' : montants,
        'objectifs': '6280000',
        'pays': pays
    }
    return render(request, 'pages/index.html', dico)
