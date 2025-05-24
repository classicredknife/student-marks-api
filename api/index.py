# index.py
import json
from typing import List
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Load student marks from JSON once on startup
with open ("q-vercel-python.json", "r") as f:
    marks_data = json.load(f)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins =["*"], # allow all origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api")
def get_marks(name: list[str] = []):
    result = [marks_data.get(n, None) for n in name]
    return JSONResponse(content={"marks": result})