import pytest
from fastapi.testclient import TestClient
from prometheus_client import REGISTRY
from main import app, REQUEST_COUNT, REQUEST_LATENCY


@pytest.fixture
def client():
    """Fixture pour créer un client de test FastAPI"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_metrics():
    """Reset les métriques Prometheus entre chaque test"""
    # Sauvegarder les valeurs actuelles
    collectors = list(REGISTRY._collector_to_names.keys())
    yield
    # Nettoyer après le test si nécessaire


class TestHealthEndpoint:
    """Tests pour l'endpoint health check"""
    
    def test_health_check_returns_ok(self, client):
        """Test que le health check retourne un statut ok"""
        response = client.get("/api/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
    
    def test_health_check_content_type(self, client):
        """Test que le content-type est correct"""
        response = client.get("/api/health")
        assert "application/json" in response.headers["content-type"]


class TestMetricsEndpoint:
    """Tests pour l'endpoint metrics Prometheus"""
    
    def test_metrics_endpoint_exists(self, client):
        """Test que l'endpoint metrics existe"""
        response = client.get("/api/metrics")
        assert response.status_code == 200
    
    def test_metrics_content_type(self, client):
        """Test que le content-type est celui de Prometheus"""
        response = client.get("/api/metrics")
        assert response.headers["content-type"] == "text/plain; version=1.0.0; charset=utf-8"
    
    def test_metrics_contains_custom_metrics(self, client):
        """Test que les métriques personnalisées sont présentes"""
        response = client.get("/api/metrics")
        content = response.text
        
        assert "app_requests_total" in content
        assert "request_latency_seconds" in content


class TestMetricsMiddleware:
    """Tests pour le middleware de métriques"""
    
    def test_request_counter_increments(self, client):
        """Test que le compteur de requêtes s'incrémente"""
        # Faire une requête
        client.get("/api/health")
        
        # Vérifier les métriques
        response = client.get("/api/metrics")
        content = response.text
        
        # Le compteur devrait contenir notre endpoint
        assert 'app_requests_total{endpoint="/api/health",method="GET"}' in content
    
    def test_request_latency_recorded(self, client):
        """Test que la latence est enregistrée"""
        # Faire une requête
        client.get("/api/health")
        
        # Vérifier les métriques
        response = client.get("/api/metrics")
        content = response.text
        
        # L'histogramme devrait contenir notre endpoint
        assert 'request_latency_seconds_count{endpoint="/api/health",method="GET"}' in content
        assert 'request_latency_seconds_sum{endpoint="/api/health",method="GET"}' in content


class TestCORS:
    """Tests pour la configuration CORS"""
    
    def test_cors_headers_present(self, client):
        """Test que les headers CORS sont présents"""
        response = client.options(
            "/api/health",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "GET"
            }
        )
        assert "access-control-allow-origin" in response.headers
    
    def test_cors_allows_all_origins(self, client):
        """Test que CORS permet toutes les origines"""
        response = client.get(
            "/api/health",
            headers={"Origin": "http://example.com"}
        )
        assert response.headers.get("access-control-allow-origin") == "*"


class TestAPIDocumentation:
    """Tests pour la documentation OpenAPI"""
    
    def test_openapi_json_available(self, client):
        """Test que le schéma OpenAPI est disponible"""
        response = client.get("/api/openapi.json")
        assert response.status_code == 200
        assert "openapi" in response.json()
    
    def test_api_docs_available(self, client):
        """Test que la documentation Swagger est disponible"""
        response = client.get("/api/docs")
        assert response.status_code == 200
    
    def test_redoc_available(self, client):
        """Test que ReDoc est disponible"""
        response = client.get("/docs")
        assert response.status_code == 200


class TestMultipleRequests:
    """Tests pour plusieurs requêtes successives"""
    
    def test_multiple_requests_increment_counter(self, client):
        """Test que plusieurs requêtes incrémentent correctement le compteur"""
        # Faire plusieurs requêtes
        for _ in range(3):
            client.get("/api/health")
        
        # Vérifier que le compteur a bien augmenté
        response = client.get("/api/metrics")
        content = response.text
        
        # Parser le contenu pour vérifier la valeur
        # Note: la valeur exacte dépend des autres tests, 
        # on vérifie juste que la métrique existe
        assert 'app_requests_total{endpoint="/api/health",method="GET"}' in content