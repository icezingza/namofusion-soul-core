from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "NaMo Framework API is running"}

@app.get("/status")
def status():
    return {"status": "ok", "framework": "NaMo", "version": "1.0"}
