from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message":"pong"}


from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

max_speed: int
max_fuel_capacity: int

id : str
brand : str
model : str
characteristics : characteristics

cars = []
@app.post("/cars")
status_code = status.http_201_created
def create_car(car: Car):
    cars.append(car.dict())
    return("message":"Car created successfully", "car":car)

@app.get("/cars")
def get_cars():
    return cars


from fastapi import HTTPException

@app.get("/cars/{id}")
def get_car_by_id(id: str):
    for car in cars:
        if car["id"] == id:
            return car
    raise HTTPException(status_code=404, detail="Car not found")

@app.put("/cars/{id}")
def update_car(id: str, new_car: Car):
   for index, car in enumerate(cars):
       if car["id"] == id:
           cars[index] = new_car.dict()
           return {"message": "Car updated successfully", "car": new_car} 
         
    raise HTTPException(status_code=404, detail="Car not found")

