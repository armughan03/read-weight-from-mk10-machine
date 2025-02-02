from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.read_weight import read_weight

app = FastAPI()

origins = [
    "https://qadmin.qwqer.pk",
    "https://dev-admin.qwqer.pk",
    "https://staging-admin.qwqer.pk",
    "http://localhost:3000",
    "http://localhost:9999",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class WeightResponse(BaseModel):
    message: str
    weight: float
    unit: str = "KG"

@app.get("/api/read_weight", response_model=WeightResponse)
async def get_weight(port: str = "COM3", baudrate: int = 9600, timeout: int = 1):
    """
    Reads the weight from the MK10 scale and returns it as a JSON response.

    Query Parameters:
    - port: Serial port (default: COM3)
    - baudrate: Communication speed (default: 9600)
    - timeout: Serial read timeout (default: 1 second)
    """
    try:
        weight = read_weight(port=port, baudrate=baudrate, timeout=timeout)
        if weight:
            return {"message": "Weight read successfully", "weight": float(weight), "unit": "KG"}
        return {"message": "Failed to read weight", "weight": 0.0, "unit": "KG"}
    except Exception as e:
        return {"message": str(e), "weight": 0.0, "unit": "KG"}


@app.get("/api/health")
async def health():
    return {"message": "OK"}
