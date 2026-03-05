# Intégration Tailwind CSS - Guide de setup et utilisation

## Vue d'ensemble
Le projet a été migré de Bootstrap 5 à **Tailwind CSS v4.2.1** pour une interface utilisateur modernisée et responsive.

## Structure et fichiers

### Fichiers de configuration Tailwind
- **`tailwind.config.js`** - Configuration Tailwind avec couleurs personnalisées
- **`postcss.config.js`** - Configuration PostCSS 
- **`alumni/static/alumni/css/input.css`** - Fichier source Tailwind
- **`alumni/static/alumni/css/output.css`** - Fichier compilé Tailwind (généré)

### Scripts npm
```bash
# Compiler les styles Tailwind une fois
npm run build

# Compiler en mode watch (rechargement automatique)
npm run dev
```

## Couleurs personnalisées
Les couleurs de l'IBAM sont intégrées comme couleurs personnalisées Tailwind :
- `primary: '#EA663B'` - Orange principal
- `secondary: '#F0906E'` - Orange secondaire  
- `info: '#42B5DA'` - Bleu information
- `accent: '#F30C05'` - Rouge accent

Utilisez-les comme: `bg-primary`, `text-info`, `border-secondary`, etc.

## Mise à jour du côté Django

### Settings.py
Les styles Tailwind sont inclus via le fichier `output.css` dans `base.html`:
```html
<link href="{% static 'alumni/css/output.css' %}" rel="stylesheet">
```

### Exécution en développement
1. **Terminal 1 - Tailwind watch mode** :
   ```bash
   npm run dev
   ```

2. **Terminal 2 - Django dev server** :
   ```bash
   python manage.py runserver
   ```

## Classes CSS principales utilisées

### Composants
- `.card` - Carte avec ombre et border
- `.btn-primary`, `.btn-secondary`, `.btn-info`, `.btn-accent` - Boutons stylisés
- `.form-control` - Champs de formulaire
- `.form-label` - Étiquettes de formulaire
- `.alert`, `.alert-error`, `.alert-success`, `.alert-info` - Alertes

### Utilitaires Tailwind standards
- Espacement: `p-6`, `m-4`, `gap-4`, etc.
- Grille: `grid`, `grid-cols-1`, `md:grid-cols-2`, `lg:grid-cols-3`
- Flexbox: `flex`, `flex-col`, `items-center`, `justify-between`
- Couleurs: `text-gray-800`, `bg-blue-50`, `border-red-200`
- États: `hover:`, `focus:`, `transition-`

## Templates convertis ✅
- ✅ base.html - Navigation et layout
- ✅ login.html - Page de connexion
- ✅ dashboard.html - Tableau de bord avec statistiques
- ✅ etudiant_list.html - Liste des étudiants (table)
- ✅ etudiant_form.html - Formulaire d'étudiant
- ✅ etudiant_confirm_delete.html - Confirmation suppression
- ✅ promotion_list.html - Liste des promotions (grid cards)
- ✅ promotion_form.html - Formulaire promotion
- ✅ promotion_confirm_delete.html - Confirmation suppression
- ✅ entreprise_list.html - Liste des entreprises (grid cards)
- ✅ entreprise_confirm_delete.html - Confirmation suppression
- ✅ diplome_list.html - Liste des diplômes (table avec filtres)
- ✅ diplome_confirm_delete.html - Confirmation suppression

## Templates à compléter 📝
Les templates suivants conservent une structure compatible mais peuvent être améliorés :
- `etudiant_detail.html`
- `promotion_detail.html`
- `promotion_form.html` 
- `enterprise_form.html`
- `diplomme_form.html`
- `diplomme_detail.html`
- `statistics.html`

## Collecte des fichiers statiques

Pour la production, exécutez :
```bash
python manage.py collectstatic
```

## Dépendances
- Node.js 14+
- npm 6+
- Python 3.8+
- Django 5.2.3
- Pillow (déjà installé)

## Troubleshooting

### Les styles ne s'affichent pas
1. Vérifiez que `output.css` existe dans `alumni/static/alumni/css/`
2. Exécutez `npm run build`
3. Videz le cache navigateur (Ctrl+Shift+Delete)
4. Redémarrez le serveur Django

### Les couleurs personnalisées ne fonctionnent pas
1. Vérifiez `tailwind.config.js`
2. Recompilez avec `npm run build`

### Le mode watch ne fonctionne pas
```bash
npm install -D @tailwindcss/cli
npm run dev
```

## Ressources
- [Documentation Tailwind CSS](https://tailwindcss.com/docs)
- [Configuration Tailwind](https://tailwindcss.com/docs/configuration)
- [Utility-First CSS](https://tailwindcss.com/docs/utility-first)

---

**Date de migration :** Février 2026  
**Version Tailwind :** 4.2.1  
**Version Django :** 5.2.3
