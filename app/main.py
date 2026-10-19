from fastapi import FastAPI

app = FastAPI(title="ledger-api")

@app.get("/health")
def health():
    return {"status": "ok"}