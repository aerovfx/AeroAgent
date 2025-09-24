from fastapi import FastAPI, UploadFile, File
from app.ocr import perform_ocr
from app.parser import parse_rubric
from app.scorer import score_text
from pydantic import BaseModel

app = FastAPI()

class AnalysisResult(BaseModel):
    extracted_text: str
    scores: dict
    total_score: float

@app.post("/analyze")
async def analyze(handwriting: UploadFile = File(...), rubric: UploadFile = File(...)):
    # Read files
    hw_content = await handwriting.read()
    rubric_content = await rubric.read()
    
    # Step 1: OCR
    text = perform_ocr(hw_content)
    
    # Step 2: Parse rubric
    criteria = parse_rubric(rubric_content)
    
    # Step 3: Score
    scores, total = score_text(text, criteria)
    
    return AnalysisResult(extracted_text=text, scores=scores, total_score=total)