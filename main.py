from fastapi import FastAPI
from pydantic import BaseModel          # NEW

app = FastAPI()

class Company(BaseModel):               # NEW
    id: int
    name: str
    sector: str

companies = [
    {"id": 1, "name": "TCS", "sector": "IT"},
    {"id": 2, "name": "Infosys", "sector": "IT"},
]

@app.get("/companies")
def list_companies():
    return companies

@app.post("/companies")                 # NEW
def add_company(company: Company):
    companies.append(company.model_dump())
    return company