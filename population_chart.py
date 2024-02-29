from fastapi import Request, APIRouter, HTTPException
from fastapi.responses import JSONResponse
import requests

from model import USPopulationData

population_router = APIRouter()

@population_router.get("/population-data")
def get_population_data(request: Request):
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["data"]
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to get US Population Data: {str(e)}")

    population_data = [
        USPopulationData(year=item["Year"], population=item["Population"])
        for item in data
    ]

    population_data_dicts = [item.model_dump() for item in population_data]

    return JSONResponse(content=population_data_dicts, status_code=200)