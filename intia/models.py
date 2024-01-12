from django.db import models

# Create your models here.

class Personnel(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    desactivation = models.BooleanField(default = False)

    def __str__(self):
        return self.nom
    


class Jour(models.Model):
    jour = models.CharField(max_length=100)
    def __str__(self):
        return self.jour

class Activite(models.Model):
    nom = models.CharField( max_length=50)
    def __str__(self):
        return self.nom

class Heure(models.Model):
    heure = models.IntegerField()
    def __str__(self):
        return str(self.heure)


class Personne_Travaille(models.Model):
    Personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    jour = models.ForeignKey(Jour, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Personnel)

##heure de traveille de la journe
class Jour_Heure(models.Model):
    heure = models.ForeignKey(Heure, on_delete=models.CASCADE)
    jour = models.ForeignKey(Jour, on_delete=models.CASCADE)
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE, default=1)



##activite reserver a une heure
class Activite_Heure(models.Model):
    heure = models.ForeignKey(Heure, on_delete=models.CASCADE)
    activitte = models.ForeignKey(Activite, on_delete=models.CASCADE)   