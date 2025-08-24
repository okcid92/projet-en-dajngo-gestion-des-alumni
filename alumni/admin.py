from django.contrib import admin
from .models import Promotion, Etudiant, Diplome, Entreprise, Emploi

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'annee_debut', 'annee_fin', 'specialisation')
    search_fields = ('nom', 'specialisation')
    list_filter = ('annee_debut', 'annee_fin')

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('ine', 'nom', 'prenom', 'email', 'promotion', 'statut_actuel')
    search_fields = ('ine', 'nom', 'prenom', 'email')
    list_filter = ('promotion', 'statut_actuel', 'annee_sortie')
    date_hierarchy = 'date_naissance'

@admin.register(Diplome)
class DiplomeAdmin(admin.ModelAdmin):
    list_display = ('intitule', 'specialisation', 'universite', 'annee_obtention', 'etudiant')
    search_fields = ('intitule', 'specialisation', 'universite')
    list_filter = ('annee_obtention', 'universite')

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'secteur', 'email_contact')
    search_fields = ('nom', 'secteur', 'email_contact')
    list_filter = ('secteur',)

@admin.register(Emploi)
class EmploiAdmin(admin.ModelAdmin):
    list_display = ('poste', 'entreprise', 'etudiant', 'date_debut', 'date_fin', 'type_contrat')
    search_fields = ('poste', 'entreprise__nom', 'etudiant__nom', 'etudiant__prenom')
    list_filter = ('type_contrat', 'date_debut')
    date_hierarchy = 'date_debut'
