import torch

MODEL_PATH = "model/"  # Change this to the actual model path
DEVICE = 0 if torch.cuda.is_available() else -1
LABELS = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Sci/Tech"
}