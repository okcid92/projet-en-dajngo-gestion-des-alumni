from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from .models import Etudiant, Promotion, Diplome, Entreprise, Emploi
from django.db.models import Q
from django.utils import timezone
from .forms import EtudiantForm
import logging
import json

logger = logging.getLogger(__name__)

# Create your views here.

class EtudiantListView(LoginRequiredMixin, ListView):
    model = Etudiant
    template_name = 'alumni/etudiant_list.html'
    context_object_name = 'etudiants'
    ordering = ['nom', 'prenom']

class EtudiantDetailView(LoginRequiredMixin, DetailView):
    model = Etudiant
    template_name = 'alumni/etudiant_detail.html'
    context_object_name = 'etudiant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        etudiant = self.get_object()
        context['diplomes'] = etudiant.diplomes.all()
        context['emplois'] = etudiant.emploi_set.all()
        return context

class EtudiantCreateView(LoginRequiredMixin, CreateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'alumni/etudiant_form.html'
    success_url = reverse_lazy('alumni:etudiant-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entreprises'] = Entreprise.objects.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        etudiant = form.instance

        # Gérer les diplômes
        intitules = self.request.POST.getlist('diplome_intitule[]')
        specialisations = self.request.POST.getlist('diplome_specialisation[]')
        universites = self.request.POST.getlist('diplome_universite[]')
        annees = self.request.POST.getlist('diplome_annee[]')

        # Supprimer tous les diplômes existants
        etudiant.diplomes.all().delete()

        # Créer les nouveaux diplômes
        for i in range(len(intitules)):
            if intitules[i] and specialisations[i] and universites[i] and annees[i]:
                Diplome.objects.create(
                    etudiant=etudiant,
                    intitule=intitules[i],
                    specialisation=specialisations[i],
                    universite=universites[i],
                    annee_obtention=annees[i]
                )

        # Gérer l'emploi si nécessaire
        if etudiant.statut_actuel in ['en_poste', 'en_stage']:
            entreprise_id = self.request.POST.get('entreprise')
            poste = self.request.POST.get('poste')
            type_contrat = self.request.POST.get('type_contrat')
            date_debut = self.request.POST.get('date_debut')

            if entreprise_id and poste and type_contrat and date_debut:
                Emploi.objects.create(
                    etudiant=etudiant,
                    entreprise_id=entreprise_id,
                    poste=poste,
                    type_contrat=type_contrat,
                    date_debut=date_debut
                )

        return response

class EtudiantUpdateView(LoginRequiredMixin, UpdateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'alumni/etudiant_form.html'
    success_url = reverse_lazy('alumni:etudiant-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entreprises'] = Entreprise.objects.all()
        context['emploi'] = self.object.emploi_set.first()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        etudiant = form.instance

        # Gérer les diplômes
        intitules = self.request.POST.getlist('diplome_intitule[]')
        specialisations = self.request.POST.getlist('diplome_specialisation[]')
        universites = self.request.POST.getlist('diplome_universite[]')
        annees = self.request.POST.getlist('diplome_annee[]')

        # Supprimer tous les diplômes existants
        etudiant.diplomes.all().delete()

        # Créer les nouveaux diplômes
        for i in range(len(intitules)):
            if intitules[i] and specialisations[i] and universites[i] and annees[i]:
                Diplome.objects.create(
                    etudiant=etudiant,
                    intitule=intitules[i],
                    specialisation=specialisations[i],
                    universite=universites[i],
                    annee_obtention=annees[i]
                )

        # Gérer l'emploi
        emploi = etudiant.emploi_set.first()
        if etudiant.statut_actuel in ['en_poste', 'en_stage']:
            entreprise_id = self.request.POST.get('entreprise')
            poste = self.request.POST.get('poste')
            type_contrat = self.request.POST.get('type_contrat')
            date_debut = self.request.POST.get('date_debut')

            if entreprise_id and poste and type_contrat and date_debut:
                if emploi:
                    emploi.entreprise_id = entreprise_id
                    emploi.poste = poste
                    emploi.type_contrat = type_contrat
                    emploi.date_debut = date_debut
                    emploi.save()
                else:
                    Emploi.objects.create(
                        etudiant=etudiant,
                        entreprise_id=entreprise_id,
                        poste=poste,
                        type_contrat=type_contrat,
                        date_debut=date_debut
                    )
        elif emploi:
            emploi.delete()

        return response

class EtudiantDeleteView(LoginRequiredMixin, DeleteView):
    model = Etudiant
    template_name = 'alumni/etudiant_confirm_delete.html'
    success_url = reverse_lazy('alumni:etudiant-list')

# Vues pour Promotion
class PromotionListView(LoginRequiredMixin, ListView):
    model = Promotion
    template_name = 'alumni/promotion_list.html'
    context_object_name = 'promotions'

class PromotionDetailView(LoginRequiredMixin, DetailView):
    model = Promotion
    template_name = 'alumni/promotion_detail.html'
    context_object_name = 'promotion'

class PromotionCreateView(LoginRequiredMixin, CreateView):
    model = Promotion
    template_name = 'alumni/promotion_form.html'
    fields = ['nom', 'annee_debut', 'annee_fin', 'specialisation']
    success_url = reverse_lazy('alumni:promotion-list')

class PromotionUpdateView(LoginRequiredMixin, UpdateView):
    model = Promotion
    template_name = 'alumni/promotion_form.html'
    fields = ['nom', 'annee_debut', 'annee_fin', 'specialisation']
    success_url = reverse_lazy('alumni:promotion-list')

class PromotionDeleteView(LoginRequiredMixin, DeleteView):
    model = Promotion
    template_name = 'alumni/promotion_confirm_delete.html'
    success_url = reverse_lazy('alumni:promotion-list')

# Vues pour Entreprise
class EntrepriseListView(LoginRequiredMixin, ListView):
    model = Entreprise
    template_name = 'alumni/entreprise_list.html'
    context_object_name = 'entreprises'
    ordering = ['nom']

class EntrepriseDetailView(LoginRequiredMixin, DetailView):
    model = Entreprise
    template_name = 'alumni/entreprise_detail.html'
    context_object_name = 'entreprise'

class EntrepriseCreateView(LoginRequiredMixin, CreateView):
    model = Entreprise
    template_name = 'alumni/entreprise_form.html'
    fields = ['nom', 'secteur', 'adresse', 'site_web', 'email_contact']
    success_url = reverse_lazy('alumni:entreprise-list')

class EntrepriseUpdateView(LoginRequiredMixin, UpdateView):
    model = Entreprise
    template_name = 'alumni/entreprise_form.html'
    fields = ['nom', 'secteur', 'adresse', 'site_web', 'email_contact']
    success_url = reverse_lazy('alumni:entreprise-list')

class EntrepriseDeleteView(LoginRequiredMixin, DeleteView):
    model = Entreprise
    template_name = 'alumni/entreprise_confirm_delete.html'
    success_url = reverse_lazy('alumni:entreprise-list')

class CustomLoginView(LoginView):
    template_name = 'alumni/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('alumni:dashboard')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'alumni/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_etudiants'] = Etudiant.objects.count()
        context['total_entreprises'] = Entreprise.objects.count()
        context['total_diplomes'] = Diplome.objects.count()
        context['total_emplois'] = Emploi.objects.count()
        
        # Statistiques des étudiants par statut
        context['etudiants_en_poste'] = Etudiant.objects.filter(statut_actuel='en_poste').count()
        context['etudiants_en_stage'] = Etudiant.objects.filter(statut_actuel='en_stage').count()
        context['etudiants_en_recherche'] = Etudiant.objects.filter(statut_actuel='en_recherche').count()
        
        # Dernières promotions
        context['dernieres_promotions'] = Promotion.objects.order_by('-annee_debut')[:5]
        
        # Derniers étudiants ajoutés (triés par INE)
        context['derniers_etudiants'] = Etudiant.objects.order_by('-ine')[:5]
        
        return context

class StatisticsView(LoginRequiredMixin, TemplateView):
    template_name = 'alumni/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Distribution des statuts actuels
        statuts_distribution = Etudiant.objects.values('statut_actuel')\
            .annotate(count=Count('ine'))\
            .order_by('statut_actuel')
        context['statuts_labels'] = json.dumps([s['statut_actuel'] for s in statuts_distribution])
        context['statuts_data'] = json.dumps([s['count'] for s in statuts_distribution])
        
        # Distribution par promotion
        promotions_distribution = Etudiant.objects.values('promotion__nom')\
            .annotate(count=Count('ine'))\
            .order_by('promotion__annee_debut')
        context['promotions_labels'] = json.dumps([p['promotion__nom'] for p in promotions_distribution])
        context['promotions_data'] = json.dumps([p['count'] for p in promotions_distribution])
        
        # Top 5 des spécialisations
        top_specialisations = Diplome.objects.values('specialisation')\
            .annotate(count=Count('id'))\
            .order_by('-count')[:5]
        context['specialisations_labels'] = json.dumps([s['specialisation'] for s in top_specialisations])
        context['specialisations_data'] = json.dumps([s['count'] for s in top_specialisations])
        
        # Top 5 des entreprises
        top_entreprises = Emploi.objects.values('entreprise__nom')\
            .annotate(count=Count('id'))\
            .order_by('-count')[:5]
        context['entreprises_labels'] = json.dumps([e['entreprise__nom'] for e in top_entreprises])
        context['entreprises_data'] = json.dumps([e['count'] for e in top_entreprises])
        
        # Taux d'insertion par promotion
        insertion_rates = []
        for promotion in Promotion.objects.all():
            total = Etudiant.objects.filter(promotion=promotion).count()
            employed = Etudiant.objects.filter(promotion=promotion, statut_actuel='en_poste').count()
            rate = (employed / total * 100) if total > 0 else 0
            insertion_rates.append({
                'promotion': promotion.nom,
                'rate': round(rate, 2)
            })
        context['insertion_labels'] = json.dumps([r['promotion'] for r in insertion_rates])
        context['insertion_data'] = json.dumps([r['rate'] for r in insertion_rates])
        
        # Distribution des types de contrats
        contrats_distribution = Emploi.objects.values('type_contrat')\
            .annotate(count=Count('id'))\
            .order_by('type_contrat')
        context['contrats_labels'] = json.dumps([c['type_contrat'] for c in contrats_distribution])
        context['contrats_data'] = json.dumps([c['count'] for c in contrats_distribution])
        
        # Évolution des diplômes
        evolution_diplomes = Diplome.objects.values('annee_obtention')\
            .annotate(count=Count('id'))\
            .order_by('annee_obtention')
        context['evolution_labels'] = json.dumps([e['annee_obtention'] for e in evolution_diplomes])
        context['evolution_data'] = json.dumps([e['count'] for e in evolution_diplomes])
        
        # Secteurs d'activité
        secteurs_distribution = Entreprise.objects.values('secteur')\
            .annotate(count=Count('id'))\
            .order_by('secteur')
        context['secteurs_labels'] = json.dumps([s['secteur'] for s in secteurs_distribution])
        context['secteurs_data'] = json.dumps([s['count'] for s in secteurs_distribution])
        
        return context

class DiplomeListView(LoginRequiredMixin, ListView):
    model = Diplome
    template_name = 'alumni/diplome_list.html'
    context_object_name = 'diplomes'
    ordering = ['-annee_obtention', 'intitule']

    def get_queryset(self):
        queryset = super().get_queryset()
        specialisation = self.request.GET.get('specialisation')
        universite = self.request.GET.get('universite')
        annee = self.request.GET.get('annee')

        if specialisation:
            queryset = queryset.filter(specialisation__icontains=specialisation)
        if universite:
            queryset = queryset.filter(universite__icontains=universite)
        if annee:
            queryset = queryset.filter(annee_obtention=annee)

        return queryset

class DiplomeDetailView(LoginRequiredMixin, DetailView):
    model = Diplome
    template_name = 'alumni/diplome_detail.html'
    context_object_name = 'diplome'

class DiplomeCreateView(LoginRequiredMixin, CreateView):
    model = Diplome
    template_name = 'alumni/diplome_form.html'
    fields = ['intitule', 'specialisation', 'universite', 'annee_obtention', 'etudiant']

    def get_initial(self):
        initial = super().get_initial()
        etudiant_ine = self.request.GET.get('etudiant')
        if etudiant_ine:
            try:
                etudiant = Etudiant.objects.get(ine=etudiant_ine)
                initial['etudiant'] = etudiant
            except Etudiant.DoesNotExist:
                pass
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        etudiant_ine = self.request.GET.get('etudiant')
        if etudiant_ine:
            try:
                etudiant = Etudiant.objects.get(ine=etudiant_ine)
                context['etudiant'] = etudiant
            except Etudiant.DoesNotExist:
                pass
        return context

    def get_success_url(self):
        etudiant_ine = self.request.GET.get('etudiant')
        if etudiant_ine:
            return reverse_lazy('alumni:etudiant-detail', kwargs={'pk': etudiant_ine})
        return reverse_lazy('alumni:diplome-list')

class DiplomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Diplome
    template_name = 'alumni/diplome_form.html'
    fields = ['intitule', 'specialisation', 'universite', 'annee_obtention', 'etudiant']

    def get_success_url(self):
        return reverse_lazy('alumni:etudiant-detail', kwargs={'pk': self.object.etudiant.ine})

class DiplomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Diplome
    template_name = 'alumni/diplome_confirm_delete.html'
    success_url = reverse_lazy('alumni:diplome-list')
