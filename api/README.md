# 🚀 CY Weather - API Backend (FastAPI)

API REST moderne pour récupérer les données météorologiques en temps réel.

## 📋 Description

API FastAPI qui fournit deux endpoints pour consulter la météo actuelle et les prévisions sur 7 jours. L'API utilise Open-Meteo (gratuit, sans clé API) comme source de données météorologiques.

## ✨ Fonctionnalités

- 🌡️ **Météo actuelle** : Température, ressenti, humidité, pression, vent
- 📅 **Prévisions 7 jours** : Températures min/max, probabilité de pluie
- 🌍 **Géocodage automatique** : Conversion ville → coordonnées GPS
- 📚 **Documentation interactive** : Swagger UI et ReDoc
- 🚀 **Performance** : API asynchrone ultra-rapide
- ✅ **Validation** : Pydantic pour la validation des données
- 🔒 **CORS** : Configuré pour le développement cross-origin

## 🏗️ Architecture

```
api/
├── src/
│   ├── models/
│   │   └── Weather.py          # Modèles Pydantic (DTOs)
│   ├── services/
│   │   └── weather_service.py  # Logique métier
│   └── resources/
│       └── weather_resource.py # Endpoints API
├── main.py                     # Point d'entrée
├── pyproject.toml             # Dépendances
└── README.md                  # Ce fichier
```

### Séparation des responsabilités

- **Models** : Définition des structures de données (DTO)
- **Services** : Logique métier et appels API externes
- **Resources** : Endpoints FastAPI avec validation

## 🚀 Installation

### Option 1 : Avec UV (Recommandé - Ultra rapide)

[uv](https://github.com/astral-sh/uv) est un gestionnaire de packages Python ultra-rapide écrit en Rust.

```bash
# Installation de uv (si pas déjà installé)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Aller dans le dossier api
cd api

# Créer l'environnement virtuel
uv venv

# Activer l'environnement
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Installer les dépendances
uv sync

# Lancer l'API
uv run -- fastapi dev
```

### Option 2 : Avec pip (Traditionnel)

```bash
cd api

# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt
# ou si vous avez pyproject.toml
pip install -e .

# Lancer l'API
fastapi dev main.py
```

### Option 3 : Avec Docker

```bash
cd api
docker build -t cy-weather-api .
docker run -p 8000:8000 cy-weather-api
```

## 🏃 Démarrage

### Mode développement (avec hot-reload)

```bash
# Avec uv
uv run fastapi dev main.py

# Avec pip
python -m fastapi dev main.py
```

L'API sera accessible sur : http://localhost:8000

### Mode production

```bash
# Avec uv
uv run fastapi run main.py

# Avec pip
python -m fastapi run main.py
```

## 📚 Documentation API

Une fois l'API démarrée, accédez à :

- **Swagger UI** : http://localhost:8000/api/docs
- **ReDoc** : http://localhost:8000/docs
- **OpenAPI JSON** : http://localhost:8000/api/openapi.json

## 🔌 Endpoints

### Health Check

```http
GET /api/health
```

Vérifie que l'API est en ligne.

**Réponse** :
```json
{
  "status": "ok"
}
```

### Météo actuelle

```http
GET /api/weather/current?city=Paris&country_code=FR
```

**Paramètres** :
- `city` (requis) : Nom de la ville
- `country_code` (optionnel) : Code pays ISO (ex: FR, US, JP)

**Exemple de réponse** :
```json
{
  "city": "Paris",
  "country": "FR",
  "timestamp": "2026-01-11T14:30:00",
  "weather": {
    "temperature": 8.5,
    "feels_like": 6.2,
    "humidity": 75,
    "pressure": 1013,
    "wind_speed": 4.5,
    "description": "Partiellement nuageux",
    "icon": "03d"
  }
}
```

### Prévisions 7 jours

```http
GET /api/weather/forecast?city=Paris&country_code=FR
```

**Paramètres** :
- `city` (requis) : Nom de la ville
- `country_code` (optionnel) : Code pays ISO

**Exemple de réponse** :
```json
{
  "city": "Paris",
  "country": "FR",
  "forecast": [
    {
      "date": "2026-01-11",
      "temp_min": 5.2,
      "temp_max": 12.8,
      "temp_day": 10.5,
      "temp_night": 6.8,
      "humidity": 70,
      "wind_speed": 5.2,
      "description": "Ciel dégagé",
      "icon": "01d",
      "precipitation_probability": 10
    }
    // ... 6 autres jours
  ]
}
```

## 🧪 Tests avec curl

```bash
# Health check
curl http://localhost:8000/api/health

# Météo actuelle à Paris
curl "http://localhost:8000/api/weather/current?city=Paris&country_code=FR"

# Prévisions à Tokyo
curl "http://localhost:8000/api/weather/forecast?city=Tokyo&country_code=JP"

# Météo à New York (avec espace dans le nom)
curl "http://localhost:8000/api/weather/current?city=New%20York&country_code=US"
```

## 📦 Dépendances

Définies dans `pyproject.toml` :

```toml
dependencies = [
    "fastapi[standard]>=0.128.0",
    "python-dotenv>=1.2.1",
    "requests>=2.32.5",
    "httpx>=0.27.0",
]
```

### Dépendances principales

- **FastAPI** : Framework web moderne et rapide
- **Pydantic** : Validation des données (inclus avec FastAPI)
- **HTTPX** : Client HTTP asynchrone
- **python-dotenv** : Gestion des variables d'environnement
- **Uvicorn** : Serveur ASGI (inclus avec FastAPI[standard])

## ⚙️ Configuration

### Variables d'environnement (optionnel)

Créez un fichier `.env` dans le dossier `api/` si vous avez besoin de configuration :

```env
# Port de l'API (par défaut: 8000)
PORT=8000

# Mode debug
DEBUG=true

# CORS origins (séparés par des virgules)
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

## 🐳 Docker

### Build de l'image

```bash
docker build -t cy-weather-api .
```

### Lancer le conteneur

```bash
docker run -p 8000:8000 cy-weather-api
```

### Avec docker-compose

```bash
# Depuis la racine du projet
docker-compose up api
```

## 🛠️ Développement

### Ajouter une dépendance

```bash
# Avec uv
uv add nom-du-package

# Avec pip
pip install nom-du-package
pip freeze > requirements.txt
```

### Structure des modèles (DTOs)

Les modèles Pydantic sont dans `src/models/Weather.py` :

```python
class WeatherRequest(BaseModel):
    """DTO pour la requête météo"""
    city: str
    country_code: Optional[str] = None

class WeatherResponse(BaseModel):
    """DTO pour la réponse météo actuelle"""
    city: str
    country: str
    timestamp: datetime
    weather: CurrentWeatherData
```

### Ajouter un nouveau endpoint

1. Créer le modèle dans `src/models/`
2. Ajouter la logique dans `src/services/`
3. Créer l'endpoint dans `src/resources/`
4. Enregistrer le router dans `main.py`

## 🧪 Tests

### Tests manuels

```bash
# Tester le health check
curl http://localhost:8000/api/health

# Tester avec une ville inexistante (devrait retourner 404)
curl "http://localhost:8000/api/weather/current?city=VilleQuiNExistePas"
```

### Tests automatisés (à implémenter)

```bash
# Avec pytest
uv add --dev pytest pytest-asyncio httpx
uv run pytest
```

## 🔍 Débogage

### Activer les logs détaillés

```bash
# Mode debug avec reload automatique
fastapi dev main.py --reload --log-level debug
```

### Vérifier l'installation

```bash
# Avec uv
uv run python --version
uv run python -c "import fastapi; print(fastapi.__version__)"

# Avec pip
python --version
python -c "import fastapi; print(fastapi.__version__)"
```

## 📊 Performance

L'API utilise :
- **Async/await** : Requêtes non-bloquantes
- **Pydantic V2** : Validation ultra-rapide
- **HTTPX** : Client HTTP performant
- **FastAPI** : Framework rapide basé sur Starlette

## 🐛 Résolution de problèmes

### L'API ne démarre pas

```bash
# Vérifier que le port 8000 n'est pas utilisé
lsof -i :8000  # Linux/Mac
netstat -ano | findstr :8000  # Windows

# Vérifier les dépendances
uv sync
# ou
pip install -e .
```

### Erreur "Module not found"

```bash
# Réinstaller les dépendances
rm -rf .venv
uv venv
uv sync
```

### Erreur CORS

Si le frontend ne peut pas accéder à l'API, vérifiez la configuration CORS dans `main.py` :

```python
origins = ["*"]  # Permet toutes les origines en dev
# En production, spécifiez les domaines autorisés
```

## 🚀 Déploiement

### Avec Uvicorn (production)

```bash
# Installer uvicorn avec les extras
uv add 'uvicorn[standard]'

# Lancer en production
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Avec Gunicorn + Uvicorn

```bash
# Installer gunicorn
uv add gunicorn

# Lancer avec plusieurs workers
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 📈 Monitoring

### Health check endpoint

L'endpoint `/api/health` peut être utilisé pour :
- Docker healthchecks
- Kubernetes liveness/readiness probes
- Monitoring externe (Uptime Robot, etc.)

## 🔗 Liens utiles

- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation Pydantic](https://docs.pydantic.dev/)
- [Documentation HTTPX](https://www.python-httpx.org/)
- [Documentation UV](https://github.com/astral-sh/uv)
- [Open-Meteo API](https://open-meteo.com/)

## 📄 Licence

MIT
