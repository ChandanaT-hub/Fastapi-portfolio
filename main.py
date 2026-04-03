from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from controller.portfolio import router as portfolio_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(portfolio_router)
