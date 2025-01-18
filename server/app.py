from fastapi import FastAPI
from pydantic import BaseModel
from utils.read_weight import read_weight

app = FastAPI()

class WeightResponse(BaseModel):
    weight: float
    unit: str = "KG"

@app.get("/read_weight", response_model=WeightResponse)
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
            return {"weight": float(weight), "unit": "KG"}
        return {"weight": 0.0, "unit": "KG"}
    except Exception as e:
        return {"error": str(e)}
