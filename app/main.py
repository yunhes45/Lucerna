from fastapi import FastAPI
from app.core.es_client import es
from app.router.collection_router import router as collection_router
from app.router.record_router import router as record_router

app = FastAPI()
app.include_router(collection_router)
app.include_router(record_router)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/es-check")
def es_check():
    return es.info()
