from fastapi import FastAPI
from routers import recipes, categories

app = FastAPI()

app.include_router(recipes.router)
app.include_router(categories.router)