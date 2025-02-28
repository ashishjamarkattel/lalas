from transformers import pipeline
from app.config import MODEL_PATH, DEVICE
from utils.text_preprocess import text_normalizer

# Load model and tokenizer
classifier = pipeline("text-classification", model=MODEL_PATH, tokenizer=MODEL_PATH, device=DEVICE)


def model_inference(text: str) -> int:
    """Runs inference using the trained DistilBERT model."""
    pred = classifier(text_normalizer(text))[0]["label"]
    return int(pred.replace("LABEL_", ""))  # Extract integer label