# ledger-api

API REST de libro contable (cuentas y transacciones) construida con FastAPI y MySQL.

## Ejecutar en local

    python -m venv .venv
    source .venv/Scripts/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload

Documentación interactiva en http://127.0.0.1:8000/docs