
# app/api/routes/analyze.py

from fastapi import APIRouter, UploadFile, File
from app.pipeline.analyzer import run_pipeline

router = APIRouter()

@router.post("/analyze-screenshot")
async def analyze_screenshot(file: UploadFile = File(...)):

    result = await run_pipeline(
        input_type="image",
        data=file
    )

    return result


@router.post("/analyze-market")
async def analyze_market(symbol: str, timeframe: str):

    result = await run_pipeline(
        input_type="market",
        data={"symbol": symbol, "timeframe": timeframe}
    )

    return result
