from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse
from population_chart import population_router

app = FastAPI()

# Endpoint to view the HTML file.
@app.get("/")
async def view_index():
    return FileResponse("index.html")

# Includes the FastAPI population_router for the population data.
app.include_router(population_router)
