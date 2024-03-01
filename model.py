from pydantic import BaseModel

# This is a BaseModel used for the US Population Data.
class USPopulationData(BaseModel):
    population: int
    year : int
    