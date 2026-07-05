
from fastapi import FastAPI
from app.api.routes import analyze, health

app = FastAPI(title="Atlas AI")

app.include_router(health.router)
app.include_router(analyze.router)
