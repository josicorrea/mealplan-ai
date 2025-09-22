
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .openrouter_client import get_mealplan_from_llm
import asyncio

app = FastAPI()

class MealPlanRequest(BaseModel):
    preferencias: str
    dias: int

@app.get("/")
def root():
    return {"message": "Mealplan AI API running"}

@app.post("/generar-mealplan")
async def generar_mealplan(request: MealPlanRequest):
    try:
        plan = await get_mealplan_from_llm(request.preferencias, request.dias)
        return {"plan": plan}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
