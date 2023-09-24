from fastapi import Depends, FastAPI, HTTPException, Request, Response, status, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from sickness_db import Sickness, arrOfdiseases
from typing import Annotated
import uvicorn

app = FastAPI()

# setting up cors policy
origins = [
    "http://192.168.43.163:3000",
    "http://192.168.43.163:3000/order",
    "http://localhost:3000",
    "http://localhost:3000/order",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # expose_headers=["*"],
)

@app.get(
    "/sickness/diagnostic",
    response_model=list[Sickness],
    include_in_schema=True,
)
def show_sickness():
    json_compatible_item_data = jsonable_encoder(arrOfdiseases)
    return json_compatible_item_data

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )