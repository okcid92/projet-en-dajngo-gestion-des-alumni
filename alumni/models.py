from django.db import models

# Create your models here.

class Promotion(models.Model):
    nom = models.CharField(max_length=100)
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()
    specialisation = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nom} ({self.annee_debut}-{self.annee_fin})"

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

class Etudiant(models.Model):
    STATUT_CHOICES = [
        ('en_etude', 'En étude'),
        ('en_poste', 'En poste'),
        ('en_stage', 'En stage'),
        ('en_recherche', 'En recherche d\'emploi'),
        ('autre', 'Autre'),
    ]

    ine = models.CharField(max_length=12, primary_key=True, help_text="N suivi de 11 chiffres")
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    telephone = models.CharField(max_length=15)
    date_naissance = models.DateField()
    adresse = models.TextField()
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    annee_sortie = models.IntegerField()
    statut_actuel = models.CharField(max_length=20, choices=STATUT_CHOICES)
    photo_profil = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.ine})"

    class Meta:
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"

class Diplome(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='diplomes')
    intitule = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=100)
    universite = models.CharField(max_length=100)
    annee_obtention = models.IntegerField()

    def __str__(self):
        return f"{self.intitule} - {self.specialisation} ({self.annee_obtention})"

    class Meta:
        verbose_name = "Diplôme"
        verbose_name_plural = "Diplômes"

class Entreprise(models.Model):
    nom = models.CharField(max_length=150)
    secteur = models.CharField(max_length=100)
    adresse = models.TextField()
    site_web = models.URLField(max_length=255)
    email_contact = models.EmailField(max_length=150)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Entreprise"
        verbose_name_plural = "Entreprises"

class Emploi(models.Model):
    TYPE_CONTRAT_CHOICES = [
        ('cdi', 'CDI'),
        ('cdd', 'CDD'),
        ('stage', 'Stage'),
        ('autre', 'Autre'),
    ]

    poste = models.CharField(max_length=150)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    type_contrat = models.CharField(max_length=20, choices=TYPE_CONTRAT_CHOICES)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.poste} chez {self.entreprise.nom}"

    class Meta:
        verbose_name = "Emploi"
        verbose_name_plural = "Emplois"
