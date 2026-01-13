# 🌐 CY Weather - Frontend (Vue.js)

Interface web moderne pour l'application météo CY Weather.

## 📋 Description

Application Vue.js 3 avec TypeScript permettant de visualiser la météo actuelle et les prévisions sur 7 jours. L'interface est responsive, moderne et optimisée pour tous les appareils.

## ✨ Fonctionnalités

- 🔍 Barre de recherche avec ville et code pays
- 🌡️ Affichage de la météo actuelle avec détails
- 📅 Prévisions sur 7 jours avec graphiques
- 📱 Design responsive (mobile, tablette, desktop)
- ⚡ Chargement asynchrone avec états de chargement
- ❌ Gestion complète des erreurs
- 🎨 Interface moderne avec dégradés et animations

## 🚀 Installation

### Prérequis

- Node.js 18+ et npm
- L'API backend doit être en cours d'exécution (port 8000)

### Installation des dépendances

```bash
cd web
npm install
```

## 🏃 Démarrage

### Mode développement

```bash
npm run dev
```

L'application sera accessible sur : http://localhost:5173

### Build pour production

```bash
npm run build
```

Les fichiers de production seront dans le dossier `dist/`

### Prévisualisation du build

```bash
npm run preview
```

## ⚙️ Configuration

### Variables d'environnement

Créez un fichier `.env` à la racine du dossier `web/` :

```env
VITE_API_URL=http://localhost:8000/api
```

Ou pour un déploiement en production :

```env
VITE_API_URL=https://votre-domaine.com/api
```

## 🐳 Docker

### Build de l'image

```bash
docker build -t cy-weather-web \
  --build-arg VITE_API_URL=http://localhost:8000/api .
```

### Lancer le conteneur

```bash
docker run -p 80:80 cy-weather-web
```

Accéder à l'application : http://localhost

## 📁 Structure du projet

```
web/
├── src/
│   ├── api/
│   │   └── api.ts              # Client API avec fetch
│   ├── components/
│   │   ├── CurrentWeather.vue  # Composant météo actuelle
│   │   └── WeatherForecast.vue # Composant prévisions
│   ├── types/
│   │   └── weather.ts          # Types TypeScript
│   ├── App.vue                 # Composant principal
│   ├── main.ts                 # Point d'entrée
│   └── style.css               # Styles globaux
├── public/                     # Assets statiques
├── index.html                  # Page HTML principale
├── vite.config.ts             # Configuration Vite
├── tsconfig.json              # Configuration TypeScript
├── Dockerfile                 # Image Docker
├── nginx.conf                 # Configuration Nginx
└── package.json               # Dépendances npm
```

## 🛠️ Technologies utilisées

- **Vue.js 3** - Framework JavaScript progressif
- **TypeScript** - Superset typé de JavaScript
- **Vite** - Build tool rapide et moderne
- **Fetch API** - Requêtes HTTP natives (pas d'Axios)
- **CSS3** - Styles avec animations et dégradés
- **Nginx** - Serveur web pour production
- **Brotli** - Compression pour optimiser le chargement

## 📝 Scripts disponibles

| Commande | Description |
|----------|-------------|
| `npm run dev` | Démarre le serveur de développement |
| `npm run build` | Crée le build de production |
| `npm run preview` | Prévisualise le build de production |

## 🎨 Composants

### App.vue
Composant principal qui gère :
- La barre de recherche
- L'état de l'application
- Les appels API
- L'affichage des composants enfants

### CurrentWeather.vue
Affiche la météo actuelle :
- Température et ressenti
- Icône météo
- Humidité, pression, vent
- Horodatage

### WeatherForecast.vue
Affiche les prévisions :
- Grille de 7 jours
- Températures min/max
- Probabilité de précipitations
- Vitesse du vent

## 🔌 API Client

Le client API est implémenté dans `src/api/api.ts` avec :
- Utilisation de l'API Fetch native
- Gestion des erreurs HTTP
- Types TypeScript complets
- Configuration de l'URL via variables d'environnement

### Exemple d'utilisation

```typescript
import { getCurrentWeather, getWeatherForecast } from './api/api';

// Récupérer la météo actuelle
const weather = await getCurrentWeather('Paris', 'FR');

// Récupérer les prévisions
const forecast = await getWeatherForecast('Paris', 'FR');
```

## 🎯 Points d'attention

### CORS
Si vous rencontrez des erreurs CORS, vérifiez que :
1. L'API backend autorise les requêtes depuis votre domaine
2. Les en-têtes CORS sont correctement configurés dans FastAPI

### Variables d'environnement
- Les variables doivent commencer par `VITE_`
- Elles sont injectées au moment du build
- Pour changer l'URL en production, rebuild l'image Docker

### Performance
- Les assets sont compressés avec Brotli et Gzip
- Le cache des fichiers statiques est configuré sur 1 an
- Le code est minifié et optimisé par Vite

## 🐛 Débogage

### Le frontend ne se connecte pas à l'API

```bash
# Vérifier l'URL de l'API
echo $VITE_API_URL

# Vérifier que l'API répond
curl http://localhost:8000/api/health

# Vérifier les logs du navigateur (Console F12)
```

### Erreur au build

```bash
# Nettoyer et réinstaller
rm -rf node_modules package-lock.json
npm install

# Rebuild
npm run build
```

### Erreur "Module not found"

```bash
# Vérifier les imports et les chemins
# Les imports doivent utiliser des chemins relatifs ou alias
```

## 🚀 Déploiement

### Avec Nginx (recommandé)

```bash
# Build
npm run build

# Copier vers Nginx
sudo cp -r dist/* /var/www/html/

# Configurer Nginx avec nginx.conf
sudo cp nginx.conf /etc/nginx/sites-available/cy-weather
sudo ln -s /etc/nginx/sites-available/cy-weather /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### Avec Docker (production)

```bash
docker build -t cy-weather-web \
  --build-arg VITE_API_URL=https://api.votre-domaine.com/api .
docker run -d -p 80:80 cy-weather-web
```

## 📊 Optimisations

- **Code splitting** : Vite sépare automatiquement le code
- **Tree shaking** : Élimination du code inutilisé
- **Compression** : Brotli + Gzip pour réduire la taille
- **Cache** : Headers de cache optimisés pour les assets
- **Lazy loading** : Chargement différé des composants

## 🔗 Liens utiles

- [Documentation Vue.js 3](https://vuejs.org/)
- [Documentation Vite](https://vitejs.dev/)
- [Documentation TypeScript](https://www.typescriptlang.org/)
- [API Fetch MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

## 📄 Licence

MIT
