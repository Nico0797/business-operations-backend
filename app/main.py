from fastapi import FastAPI

app = FastAPI(
    title="Business Operations Backend",
    description="API for managing products, customers, invoices, and business operations.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Business Operations Backend is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}