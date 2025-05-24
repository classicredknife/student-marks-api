# index.py

import json
import logging
from typing import List
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Load student marks from JSON once on startup
try:
    with open("q-vercel-python.json", "r") as f:
        marks_data = json.load(f)
        logging.info("Loaded marks: %s", marks_data)
except (FileNotFoundError, json.JSONDecodeError) as e:
    logging.error("Error loading marks data: %s", e)
    marks_data = {}

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
def get_marks(name: List[str] = None):
    if name is None:
        name = []
    logging.info("Query received: %s", name)
    result = [{n: marks_data.get(n, "Not Found")} for n in name]
    return JSONResponse(content={"marks": result})
