from pydantic import BaseModel, Field
from typing import Dict

class OptimalPortfolioResponse(BaseModel):
    optimal_portfolio: Dict[str, float] = Field(..., description="Optimal weights by ticker")
