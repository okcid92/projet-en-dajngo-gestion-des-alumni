# 📚 Gestion des Alumni IBAM - Tailwind CSS Edition

Application Django avec Tailwind CSS pour la gestion des étudiants sortants.

## 🚀 Démarrage rapide

### 1. Installation des dépendances

```bash
# Dépendances Python
pip install Django==5.2.3 Pillow>=11.0.0

# Dépendances Node.js (pour Tailwind)
npm install
```

### 2. Configuration Django

```bash
# Migrations
python manage.py migrate

# Créer un utilisateur admin
python manage.py createsuperuser
```

### 3. Lancer l'application

**Terminal 1 - Tailwind CSS (Watch mode):**
```bash
npm run dev
```

**Terminal 2 - Serveur Django:**
```bash
python manage.py runserver
```

Accédez à l'application: http://localhost:8000/

## 📁 Structure du projet

```
.
├── alumni/                          # App principale Django
│   ├── templates/alumni/            # Templates HTML (Tailwind)
│   │   ├── base.html               # Layout principal
│   │   ├── dashboard.html          # Tableau de bord
│   │   ├── [etudiant|promotion|entreprise|diplome]_*.html
│   ├── static/alumni/
│   │   ├── css/
│   │   │   ├── input.css           # Source Tailwind
│   │   │   └── output.css          # CSS compilée
│   ├── models.py                   # Modèles de données
│   ├── views.py                    # Vues Django
│   ├── forms.py                    # Formulaires
│   ├── urls.py                     # URLs
│   └── admin.py                    # Admin Django
├── gestion_sortants/                # Configuration Django
│   ├── settings.py
│   └── urls.py
├── tailwind.config.js              # Configuration Tailwind
├── postcss.config.js               # Configuration PostCSS
├── package.json                    # Scripts npm
├── db.sqlite3                       # Base de données
├── manage.py                        # Utilitaire Django
├── TAILWIND_SETUP.md               # Guide technique Tailwind
├── MIGRATION_SUMMARY.md            # Résumé de la migration
└── README.md                        # Ce fichier
```

## 🎨 Couleurs personnalisées

```css
primary: #EA663B    // Orange IBAM
secondary: #F0906E  // Orange secondaire
info: #42B5DA       // Bleu
accent: #F30C05     // Rouge
```

Utilisez-les dans les templates:
```html
<button class="bg-primary text-white">Bouton</button>
<div class="text-info">Texte bleu</div>
```

## 📝 Scripts npm disponibles

```bash
npm run build    # Compiler Tailwind une fois
npm run dev      # Watch mode (recommandé en dev)
```

## 🔧 Commandes Django utiles

```bash
# Server de développement
python manage.py runserver

# Migrations
python manage.py migrate
python manage.py makemigrations

# Admin
python manage.py createsuperuser

# Collecte des static files (production)
python manage.py collectstatic
```

## 📚 Fonctionnalités

- ✅ Gestion des étudiants (CRUD)
- ✅ Gestion des promotions
- ✅ Gestion des entreprises
- ✅ Gestion des diplômes
- ✅ Tableau de bord avec statistiques
- ✅ Authentification utilisateur
- ✅ Interface responsive (mobile & desktop)

## 🆘 Aide & Documentation

- **Tailwind CSS:** Voir [TAILWIND_SETUP.md](TAILWIND_SETUP.md)
- **Résumé migration:** Voir [MIGRATION_SUMMARY.md](MIGRATION_SUMMARY.md)
- **Documentation Django:** https://docs.djangoproject.com/
- **Documentation Tailwind:** https://tailwindcss.com/docs

## 🐛 Problèmes courants

### Les styles ne s'appliquent pas?
1. Vérifier que `npm run dev` est en cours d'exécution
2. Vider le cache navigateur (Ctrl+Shift+Delete)
3. Relancer le serveur Django

### Port 8000 déjà utilisé?
```bash
python manage.py runserver 8001
```

### Besoin de réinitialiser la BD?
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 🚢 Déploiement en production

```bash
# Compiler les styles Tailwind
npm run build

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Définir DEBUG=False dans settings.py
# Créer un fichier .env avec les variables d'environnement
```

## 📄 Licence

Projet éducatif - IBAM 2026

---

**Besoin d'aide?** Consultez les fichiers de documentation ou la documentation officielle de Django et Tailwind CSS.
