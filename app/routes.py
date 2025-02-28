from fastapi import APIRouter, HTTPException
from app.models import PredictRequest, PredictResponse
from app.services import model_inference
from app.config import LABELS

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Input text cannot be empty")
    
    predicted_label = model_inference(text)
    return PredictResponse(label=predicted_label, category=LABELS[predicted_label])