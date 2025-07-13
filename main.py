from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🎉 Your first FastAPI app is live!"}
