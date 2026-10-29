from fastapi import FastAPI

app= FastAPI(
    title="Cloud AI Assistant",
    description="A learning project for cloud deployment and CI/CD.",
    version="0.1.0",
)


@app.get("/")
def home():
    return{
        "message":"Cloud AI Assistant is running",
        "status": "healthy",
        "version": "0.1.0",
    }  


@app.get("/health")
def health_check():
    return {"status":"Ok"}