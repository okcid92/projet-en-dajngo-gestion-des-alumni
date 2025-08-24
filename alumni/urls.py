from django.urls import path
from . import views

app_name = 'alumni'

urlpatterns = [
    # URLs pour l'authentification et le dashboard
    path('', views.CustomLoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('logout/', views.LogoutView.as_view(next_page='alumni:login'), name='logout'),

    # URLs pour Etudiant
    path('etudiants/', views.EtudiantListView.as_view(), name='etudiant-list'),
    path('etudiants/create/', views.EtudiantCreateView.as_view(), name='etudiant-create'),
    path('etudiants/<str:pk>/update/', views.EtudiantUpdateView.as_view(), name='etudiant-update'),
    path('etudiants/<str:pk>/delete/', views.EtudiantDeleteView.as_view(), name='etudiant-delete'),
    path('etudiants/<str:pk>/', views.EtudiantDetailView.as_view(), name='etudiant-detail'),

    # URLs pour Promotion
    path('promotions/', views.PromotionListView.as_view(), name='promotion-list'),
    path('promotions/create/', views.PromotionCreateView.as_view(), name='promotion-create'),
    path('promotions/<int:pk>/update/', views.PromotionUpdateView.as_view(), name='promotion-update'),
    path('promotions/<int:pk>/delete/', views.PromotionDeleteView.as_view(), name='promotion-delete'),
    path('promotions/<int:pk>/', views.PromotionDetailView.as_view(), name='promotion-detail'),

    # URLs pour Entreprise
    path('entreprises/', views.EntrepriseListView.as_view(), name='entreprise-list'),
    path('entreprises/create/', views.EntrepriseCreateView.as_view(), name='entreprise-create'),
    path('entreprises/<int:pk>/update/', views.EntrepriseUpdateView.as_view(), name='entreprise-update'),
    path('entreprises/<int:pk>/delete/', views.EntrepriseDeleteView.as_view(), name='entreprise-delete'),
    path('entreprises/<int:pk>/', views.EntrepriseDetailView.as_view(), name='entreprise-detail'),

    # URLs pour Diplome
    path('diplomes/', views.DiplomeListView.as_view(), name='diplome-list'),
    path('diplomes/create/', views.DiplomeCreateView.as_view(), name='diplome-create'),
    path('diplomes/<int:pk>/update/', views.DiplomeUpdateView.as_view(), name='diplome-update'),
    path('diplomes/<int:pk>/delete/', views.DiplomeDeleteView.as_view(), name='diplome-delete'),
    path('diplomes/<int:pk>/', views.DiplomeDetailView.as_view(), name='diplome-detail'),

    # URL pour la recherche avancée
    path('statistics/', views.StatisticsView.as_view(), name='statistics'),
] 