# API, JSON, HTML, & Javascript HW2

## Website Picture:
![hw2website](https://github.com/plovanpete/cs3980-hw2-datausa/assets/145849883/51022c47-54ea-4b93-8805-95abb910dd31)

## What is needed to run:
We will need to install these packages: FastAPI, Pydantic, and Uvicorn
'''
pip install fastapi pydantic uvicorn
'''

## index.html
This HTML file contains both the CSS and Javascript. This is used for putting the template on the site.

### HTML File P1 (Has CSS Stylesheet):
![hw2indexcommentpt1v2](https://github.com/plovanpete/cs3980-hw2-datausa/assets/145849883/dba9c19b-b953-4cda-9df8-64ab4f7e2d78)

### HTML File P2 (Has JavaScript):
![hw2indexcommentpt2v2](https://github.com/plovanpete/cs3980-hw2-datausa/assets/145849883/9149ae1c-f40e-493a-8ea1-a3061cd81590)

## main.py
This python file allows for the server and script to run to show the data.

### main.py Code:
![hw2main](https://github.com/plovanpete/cs3980-hw2-datausa/assets/145849883/f4b3bfbe-408d-4f66-bab5-2b9c8e8a23e2)


## model.py
This python file creates a Pydantic BaseModel used to specify the USPopulationData.
Allows for data validation of USPopulationData which has data of Year and Population of the US.

### model.py Code:
![hw2model](https://github.com/plovanpete/cs3980-hw2-datausa/assets/145849883/f4bf2ada-5b5b-4568-8d77-bd806eb3e345)


## popluation_chart.py
This python file creates a router in which we can grab the JSON Data from the URL and puts it in readable format.

### population_chart.py Code:
![hw2populationdatav2](https://github.com/plovanpete/cs3980-hw2-datausa/assets/145849883/c5afa0e7-9916-4bcb-be1f-13896e1b31e5)

