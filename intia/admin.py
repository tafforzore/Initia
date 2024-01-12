from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Personnel)
class Useradmin(admin.ModelAdmin):
    list_display = ('nom','prenom', 'desactivation')

# Register your models here.
@admin.register(Jour)
class Useradmin(admin.ModelAdmin):
    list_display = ('id','jour')

# Register your models here.
@admin.register(Activite)
class Useradmin(admin.ModelAdmin):
    list_display = ('nom',)

# Register your models here.
@admin.register(Heure)
class Useradmin(admin.ModelAdmin):
    list_display = ('id','heure')

# Register your models here.
@admin.register(Jour_Heure)
class Useradmin(admin.ModelAdmin):
    list_display = ('heure','jour','activite')


@admin.register(Personne_Travaille)
class Useradmin(admin.ModelAdmin):
    list_display = ('Personnel','jour')
