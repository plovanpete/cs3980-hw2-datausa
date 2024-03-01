from fastapi import Request, APIRouter, HTTPException
from fastapi.responses import JSONResponse
import requests

from model import USPopulationData

population_router = APIRouter()

# Defines router and gets the population data for the table under the Years and Population.
@population_router.get("/population-data")
def get_population_data(request: Request):
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    try:
        # Fetches Data from the API.
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["data"]
    except requests.exceptions.RequestException as e:

        # Error is it can't fetch data.
        raise HTTPException(status_code=500, detail=f"Failed to get US Population Data: {str(e)}")

    # Converts the data to Pydantic model and loops through it to get the items.
    population_data = [
        USPopulationData(year=item["Year"], population=item["Population"])
        for item in data
    ]

    # Converts the model to readable JSON.
    population_data_json = [item.model_dump() for item in population_data]

    # Returns the JSON response with the population data provided.
    return JSONResponse(content=population_data_json, status_code=200)