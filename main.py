from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse
from population_chart import population_router

app = FastAPI()

@app.get("/")
async def view_index():
    return FileResponse("index.html")

app.include_router(population_router)
