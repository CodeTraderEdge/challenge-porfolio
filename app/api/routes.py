from fastapi import APIRouter, UploadFile, File, Form, HTTPException

import pandas as pd

from app.services.optimizer import optimize_portfolio
from app.schemas.response import OptimalPortfolioResponse

router = APIRouter()

@router.post("/optimize-portfolio", response_model=OptimalPortfolioResponse)
async def optimize_endpoint(
    file: UploadFile = File(...),
    risk_level: float = Form(...),
    max_weight: float = Form(...)
):
    try:
        df = pd.read_csv(file.file, index_col=0)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV file: {e}")

    if df.empty or df.shape[1] < 1:
        raise HTTPException(status_code=400, detail="Invalid or empty CSV file")

    try:
        portfolio = optimize_portfolio(df, risk_level, max_weight)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"optimal_portfolio": portfolio}
