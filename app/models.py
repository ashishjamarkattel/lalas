from pydantic import BaseModel
from typing import Literal

class PredictRequest(BaseModel):
    text: str

class PredictResponse(BaseModel):
    label: Literal[0, 1, 2, 3]
    category: Literal["World", "Sports", "Business", "Sci/Tech"]