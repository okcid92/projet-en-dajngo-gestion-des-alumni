from django import forms
from .models import Etudiant, Entreprise, Emploi, Promotion

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['ine', 'nom', 'prenom', 'email', 'telephone', 'date_naissance', 
                 'adresse', 'promotion', 'annee_sortie', 'statut_actuel', 'photo_profil']
        widgets = {
            'ine': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'annee_sortie': forms.NumberInput(attrs={'class': 'form-control'}),
            'statut_actuel': forms.Select(choices=[
                ('en_etude', 'En étude'),
                ('en_poste', 'En poste'),
                ('en_stage', 'En stage'),
                ('en_recherche', 'En recherche d\'emploi'),
                ('autre', 'Autre')
            ], attrs={'class': 'form-control'}),
            'photo_profil': forms.FileInput(attrs={'class': 'form-control'}),
        }

    promotion = forms.ModelChoiceField(
        queryset=Promotion.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Champs pour les diplômes
    diplome_intitule = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    diplome_specialisation = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    diplome_universite = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    diplome_annee = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    # Champs pour l'emploi
    entreprise = forms.ModelChoiceField(
        queryset=Entreprise.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    poste = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    type_contrat = forms.ChoiceField(
        choices=Emploi.TYPE_CONTRAT_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date_debut = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    ) 