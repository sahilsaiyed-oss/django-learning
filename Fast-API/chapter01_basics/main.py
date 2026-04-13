from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Backend - Chapter 1"}

# About endpoint
@app.get("/about")
def about():
    return {
        "project": "FastAPI 30 Days Mastery",
        "chapter": "Chapter 1 - Basics",
        "author": "Sahil"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "OK"}