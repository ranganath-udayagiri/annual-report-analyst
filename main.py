from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException          # NEW

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

@app.post("/companies", status_code=201)
def add_company(company: Company):
    for c in companies:
        if c["id"] == company.id:
            raise HTTPException(status_code=409, detail="Company id already exists")
    companies.append(company.model_dump())
    return company

@app.get("/companies/{company_id}")
def get_company(company_id: int):
    for c in companies:
        if c["id"] == company_id:
            return c
    raise HTTPException(status_code=404, detail="Company not found")