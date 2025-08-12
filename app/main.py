from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # metti il dominio frontend Vercel qui per maggiore sicurezza
    allow_methods=["*"],
    allow_headers=["*"],
)

class SumRequest(BaseModel):
    num1: float
    num2: float

@app.post("/sum")
def sum_numbers(data: SumRequest):
    return {"result": data.num1 + data.num2}
