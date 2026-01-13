from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import FastAPI, APIRouter
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from src.resources.weather_resource import router as weather_router


tags_metadata = [
    {
        "name": "Health",
        "description": "Health check endpoints",
    },
    {
        "name": "Weather",
        "description": "Endpoints pour récupérer les données météo actuelles et les prévisions",
    },
]

app = FastAPI(
    title="CY Weather API",
    description="API for CY Weather application",
    version="0.1.0",
    openapi_tags=tags_metadata,
    redoc_url="/docs",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

# Metrics
REQUEST_COUNT = Counter(
    "app_requests_total", 
    "Total number of requests", 
    ["method", "endpoint"])
REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "Request latency", 
    ["method", "endpoint"])

# CORS Middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Metrics Middleware
@app.middleware("http")
async def metrics_middleware(request, call_next):
    import time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    start = time.time()
    response = await call_next(request)
    resp_time = time.time() - start
    REQUEST_LATENCY.labels(method=request.method, endpoint=request.url.path).observe(resp_time)
    return response

router = APIRouter(
    prefix="/api",
)

@router.get("/metrics", tags=["Metrics"])
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@router.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "ok"}


app.include_router(router)
app.include_router(weather_router, prefix="/api")