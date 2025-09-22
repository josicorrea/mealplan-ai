import httpx
from .config import get_openrouter_api_key

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

async def get_mealplan_from_llm(preferences: str, days: int) -> str:
    api_key = get_openrouter_api_key()
    prompt = (
        f"Eres un nutricionista. Genera un plan de alimentación de 4 comidas por día para {days} días, "
        f"según estas preferencias: {preferences}. El resultado debe ser claro y estructurado por día y comida."
    )
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",  
        "messages": [
            {"role": "system", "content": "Eres un nutricionista experto en planes alimenticios."},
            {"role": "user", "content": prompt}
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(OPENROUTER_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
