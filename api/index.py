# index.py

import os
import json
from typing import List
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Load student marks from JSON once on startup
with open (os.path.join(os.path.dirname(__file__), "home/gouri/student-marks-api/q-vercel-python.json"), "r") as f:
    marks_data = json.load(f)
    print("Loaded marks:", marks_data)

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
    print("Query recieved:", name) # debugging line
    result = [marks_data.get(n, None) for n in name]
    return JSONResponse(content={"marks": result})
