from pydantic import BaseModel

class USPopulationData(BaseModel):
    population: int
    year : int
    