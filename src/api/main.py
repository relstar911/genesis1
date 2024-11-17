import logging
from pathlib import Path
from typing import Dict, Any

import yaml
from fastapi import FastAPI, Security, Depends, HTTPException
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/api.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load configuration
def load_config() -> Dict[str, Any]:
    config_path = Path("config/config.yaml")
    try:
        with open(config_path) as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        raise

config = load_config()

app = FastAPI(
    title="GENESIS API",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key_header = APIKeyHeader(name="X-API-Key")

# API Key validation
async def verify_api_key(api_key: str = Security(api_key_header)) -> str:
    if api_key != config["api"].get("api_key"):  # In production, use secure key storage
        raise HTTPException(
            status_code=403,
            detail="Invalid API key"
        )
    return api_key

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    logger.info("Health check requested")
    return {"status": "healthy"}

@app.post("/ml/train")
async def train_model(
    data: Dict[str, Any],
    api_key: str = Security(verify_api_key)
) -> Dict[str, Any]:
    """Train ML model endpoint."""
    logger.info("Starting model training")
    try:
        # Implement model training logic
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Training failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ml/predict")
async def predict(
    data: Dict[str, Any],
    api_key: str = Security(verify_api_key)
) -> Dict[str, Any]:
    """Model prediction endpoint."""
    logger.info("Processing prediction request")
    try:
        # Implement prediction logic
        return {"predictions": []}
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(status_code=500, detail=str(e)) 