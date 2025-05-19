import numpy as np
import pandas as pd

from scipy.optimize import minimize

from app.logger import logger

def optimize_portfolio(returns: pd.DataFrame, risk_level: float, max_weight: float) -> dict:
    logger.info("Starting portfolio optimization")
    
    returns_clean = returns.dropna(how='any')
    logger.info(f"Cleaned returns DataFrame shape after dropping NaNs: {returns_clean.shape}")
    logger.debug(f"Cleaned returns head:\n{returns_clean.to_string()}")

    tickers = returns_clean.columns
    mean_returns = returns_clean.mean()
    cov_matrix = returns_clean.cov()
    n = len(tickers)

    logger.info(f"Number of assets: {n}")
    logger.debug(f"Tickers: {list(tickers)}")

    def objective(weights):
        return -weights @ mean_returns.values

    def portfolio_variance(weights):
        return weights.T @ cov_matrix.values @ weights

    constraints = [
        {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
        {'type': 'ineq', 'fun': lambda w: risk_level**2 - portfolio_variance(w)}
    ]

    bounds = [(0, max_weight) for _ in range(n)]
    x0 = np.array([1 / n] * n)

    logger.info("Running optimization...")
    result = minimize(objective, x0=x0, bounds=bounds, constraints=constraints)

    if not result.success:
        logger.error(f"Optimization failed: {result.message}")
        raise ValueError("Could not find an optimal solution")

    logger.info("Optimization successful")
    logger.debug(f"Optimal weights: {result.x}")

    rounded_weights = {ticker: round(weight, 6) for ticker, weight in zip(tickers, result.x)}
    return rounded_weights
