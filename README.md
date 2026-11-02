# Annual Report Analyst

AI research assistant for Indian company annual reports, built step by step.

## Endpoints

| Method | Path | Success | Errors |
|---|---|---|---|
| GET | /companies | 200 | — |
| GET | /companies/{company_id} | 200 | 404 not found, 422 invalid id |
| POST | /companies | 201 | 409 duplicate id, 422 invalid body |

## Run locally

```
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m fastapi dev main.py
```

Then open http://127.0.0.1:8000/docs

## Roadmap

- [x] Company API: list, get one, create (FastAPI + Pydantic)
- [ ] PostgreSQL storage
- [ ] Docker + cloud deploy
- [ ] Structured extraction of key figures
- [ ] RAG Q&A with page citations
- [ ] Evaluation
- [ ] Company comparison agent