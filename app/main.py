from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Portfolio Optimizer API")

app.include_router(router)
