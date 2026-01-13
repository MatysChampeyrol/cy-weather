# 🌤️ CY Weather - Application Météo

Application météo complète avec une API backend FastAPI et un frontend Vue.js moderne.

![Architecture](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square)
![Frontend](https://img.shields.io/badge/Frontend-Vue.js-4FC08D?style=flat-square)
![API](https://img.shields.io/badge/API-Open--Meteo-blue?style=flat-square)

## 📋 Table des matières

- [Description](#description)
- [Fonctionnalités](#fonctionnalités)
- [Architecture](#architecture)
- [Installation](#installation)
- [Démarrage rapide](#démarrage-rapide)
- [Documentation](#documentation)
- [Technologies utilisées](#technologies-utilisées)

## 📖 Description

CY Weather est une application web permettant de consulter la météo actuelle et les prévisions sur 7 jours pour n'importe quelle ville dans le monde. L'application utilise l'API gratuite Open-Meteo pour récupérer les données météorologiques en temps réel.

## ✨ Fonctionnalités

### Backend (API)
- 🌡️ **Météo actuelle** : Température, ressenti, humidité, pression, vent
- 📅 **Prévisions 7 jours** : Températures min/max, probabilité de précipitations
- 🌍 **Recherche mondiale** : Support de toutes les villes avec code pays optionnel
- 📚 **Documentation interactive** : Swagger UI intégré
- 🚀 **Performance** : API rapide et optimisée avec FastAPI
- 🆓 **Gratuit** : Utilise Open-Meteo (pas de clé API nécessaire)

### Frontend (Web)
- 🎨 **Interface moderne** : Design responsive avec dégradés et animations
- 🔍 **Recherche intuitive** : Barre de recherche avec code pays
- 📱 **Mobile-first** : Parfaitement adapté aux mobiles et tablettes
- ⚡ **Temps réel** : Chargement rapide des données
- 🌐 **Multilingue** : Descriptions météo en français

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Utilisateur                         │
└────────────────────────┬────────────────────────────────┘
                         │
                         │ HTTP
                         ▼
┌────────────────────────────────────────────────────────┐
│                  Frontend (Vue.js)                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐  │
│  │  App.vue │──│Components│──│ API Client (fetch)   │  │
│  └──────────┘  └──────────┘  └──────────┬───────────┘  │
└─────────────────────────────────────────┼──────────────┘
                                          │
                         │ REST API       │
                         ▼                ▼
┌─────────────────────────────────────────────────────────┐
│                  Backend (FastAPI)                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐   │
│  │Resources │──│ Services │──│  Models (Pydantic)   │   │
│  └──────────┘  └────┬─────┘  └──────────────────────┘   │
└─────────────────────┼───────────────────────────────────┘
                      │
                      │ HTTP
                      ▼
┌─────────────────────────────────────────────────────────┐
│           API Externe (Open-Meteo)                      │
│  - Géocodage (coordonnées GPS)                          │
│  - Météo actuelle                                       │
│  - Prévisions 7 jours                                   │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Installation

### Prérequis

- **Python 3.10+** (pour l'API)
- **Node.js 18+** (pour le frontend)
- **Docker & Docker Compose** (optionnel, pour le déploiement conteneurisé)

### Option 1 : Avec Docker (Recommandé pour les débutants)

```bash
# Cloner le projet
git clone https://github.com/RolletQuentin/cy-weather
cd cy-weather

# Lancer avec Docker Compose
docker-compose up --build

# Accéder à l'application
# Frontend: http://localhost:5173
# API: http://localhost:8000/api/docs
```

### Option 2 : Installation locale

Voir les README spécifiques dans chaque dossier :
- [README API](api/README.md) - Instructions pour le backend
- [README Web](web/README.md) - Instructions pour le frontend

## 🎯 Démarrage rapide

### Avec Docker

```bash
# Démarrer tous les services
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter les services
docker-compose down
```

### Sans Docker

Terminal 1 (API) :
```bash
cd api
uv venv
source .venv/bin/activate  # Linux/Mac
uv sync
fastapi dev main.py
```

Terminal 2 (Frontend) :
```bash
cd web
npm install
npm run dev
```

## 📚 Documentation

### API Documentation

- **Swagger UI** : http://localhost:8000/api/docs
- **ReDoc** : http://localhost:8000/docs

### Endpoints disponibles

#### Météo actuelle
```bash
GET /api/weather/current?city=Paris&country_code=FR
```

#### Prévisions 7 jours
```bash
GET /api/weather/forecast?city=Paris&country_code=FR
```

### Exemples de requêtes

```bash
# Météo à Paris
curl "http://localhost:8000/api/weather/current?city=Paris&country_code=FR"

# Prévisions à Tokyo
curl "http://localhost:8000/api/weather/forecast?city=Tokyo&country_code=JP"

# Météo à New York
curl "http://localhost:8000/api/weather/current?city=New%20York&country_code=US"
```

## 🛠️ Technologies utilisées

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderne et rapide
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Validation des données
- **[HTTPX](https://www.python-httpx.org/)** - Client HTTP asynchrone
- **[uv](https://github.com/astral-sh/uv)** - Gestionnaire de packages Python ultra-rapide
- **[Open-Meteo API](https://open-meteo.com/)** - API météo gratuite

### Frontend
- **[Vue.js 3](https://vuejs.org/)** - Framework JavaScript progressif
- **[Vite](https://vitejs.dev/)** - Build tool rapide
- **[TypeScript](https://www.typescriptlang.org/)** - JavaScript typé
- **[Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)** - Requêtes HTTP natives

### DevOps
- **[Docker](https://www.docker.com/)** - Conteneurisation
- **[Docker Compose](https://docs.docker.com/compose/)** - Orchestration multi-conteneurs
- **[Nginx](https://nginx.org/)** - Serveur web avec compression Brotli

## 📁 Structure du projet

```
devmlops/
├── api/                    # Backend FastAPI
│   ├── src/
│   │   ├── models/        # Modèles Pydantic (DTOs)
│   │   ├── services/      # Logique métier
│   │   └── resources/     # Endpoints API
│   ├── main.py            # Point d'entrée de l'API
│   ├── Dockerfile
│   └── README.md
├── web/                    # Frontend Vue.js
│   ├── src/
│   │   ├── api/           # Client API (fetch)
│   │   ├── components/    # Composants Vue
│   │   ├── types/         # Types TypeScript
│   │   └── App.vue        # Composant principal
│   ├── Dockerfile
│   ├── nginx.conf
│   └── README.md
├── docker-compose.yaml     # Configuration Docker
└── README.md              # Ce fichier
```

## 🐛 Résolution de problèmes

### L'API ne démarre pas
```bash
# Vérifier les logs
docker-compose logs api

# Ou en local
cd api
uv run fastapi dev main.py
```

### Le frontend ne se connecte pas à l'API
- Vérifiez que l'API tourne sur le port 8000
- Vérifiez l'URL de l'API dans `web/.env`
- Vérifiez les paramètres CORS dans l'API

### Erreur "Ville non trouvée"
- Vérifiez l'orthographe du nom de la ville
- Ajoutez le code pays pour plus de précision
- Essayez en anglais si le nom français ne fonctionne pas

## 🤝 Contribution

Ce projet est un projet pédagogique. Les contributions sont les bienvenues !

1. Fork le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT.

## 👥 Auteurs

Projet réalisé dans le cadre du cours DevMLOps.

## 🔗 Liens utiles

- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation Vue.js](https://vuejs.org/)
- [Open-Meteo API](https://open-meteo.com/)
- [Documentation Docker](https://docs.docker.com/)
