# index.py

import logging
from typing import List
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Define student marks data directly in the Python file
marks_data = [{"name":"Qa9ldC9wIn","marks":51},{"name":"TsQeRixst","marks":67},{"name":"V4nh","marks":77},{"name":"sW5jhz385","marks":10},{"name":"m","marks":22},{"name":"x858T0","marks":72},{"name":"4Ge6FcU","marks":23},{"name":"zKh","marks":2},{"name":"mq40z","marks":81},{"name":"ggPe7EksZa","marks":3},{"name":"7C5AY","marks":97},{"name":"ModeOkEuSk","marks":99},{"name":"lPI","marks":58},{"name":"bF8BF","marks":48},{"name":"BVQiA","marks":53},{"name":"0dWvp","marks":56},{"name":"3","marks":36},{"name":"fXqIslky1o","marks":50},{"name":"80bvsiiqdD","marks":9},{"name":"TfUYbZA","marks":80},{"name":"uZouLRF","marks":11},{"name":"O2KXmtQzux","marks":19},{"name":"WVJ","marks":82},{"name":"ljUf4Fej","marks":43},{"name":"RVVWXar","marks":11},{"name":"NjBGB3Gpjm","marks":28},{"name":"TVDNyPHnQ","marks":60},{"name":"1WqXy43b","marks":34},{"name":"v9","marks":27},{"name":"pReiQQTB2","marks":96},{"name":"8TXfAoonD","marks":37},{"name":"n7fs58XulF","marks":10},{"name":"A","marks":82},{"name":"FgGjbKX3h","marks":38},{"name":"0CjPeLD","marks":88},{"name":"NiMd","marks":4},{"name":"UR","marks":84},{"name":"tI2J","marks":10},{"name":"LI","marks":9},{"name":"ttB6XOv","marks":37},{"name":"nuC","marks":63},{"name":"hBJNtOg","marks":30},{"name":"s","marks":63},{"name":"P32U","marks":34},{"name":"RWgtqP6i","marks":61},{"name":"f","marks":25},{"name":"ed8y3dwS","marks":2},{"name":"4","marks":88},{"name":"6U","marks":77},{"name":"IKdrBIp","marks":54},{"name":"Az","marks":67},{"name":"o41F4BFfja","marks":58},{"name":"jT2vv7v","marks":77},{"name":"ldE98pAg","marks":50},{"name":"VONkrdVXzL","marks":45},{"name":"7v7R","marks":61},{"name":"0AfKNBd","marks":81},{"name":"pdO0iZysRi","marks":28},{"name":"dNDI","marks":4},{"name":"w","marks":86},{"name":"EL","marks":60},{"name":"nHPYQ","marks":24},{"name":"DEA","marks":43},{"name":"h","marks":71},{"name":"u5Y7","marks":34},{"name":"0Kdjwa","marks":60},{"name":"0NU6M7","marks":95},{"name":"ARsOa","marks":99},{"name":"j","marks":6},{"name":"Ak9","marks":40},{"name":"Nx","marks":55},{"name":"aFLMga5","marks":4},{"name":"qwEwW","marks":99},{"name":"yxFFPIPEN","marks":3},{"name":"FVYPPQFTT","marks":13},{"name":"IiQ","marks":93},{"name":"a3","marks":57},{"name":"K","marks":40},{"name":"QS9Kg10L4","marks":41},{"name":"ZW8gJB","marks":43},{"name":"wB","marks":19},{"name":"M","marks":58},{"name":"iDTi","marks":80},{"name":"jX2v9Zq","marks":66},{"name":"FrUT","marks":88},{"name":"jUxmyFBJz","marks":74},{"name":"nz","marks":40},{"name":"bZxKuTAiZ","marks":48},{"name":"EK","marks":3},{"name":"9pmCATl0gZ","marks":4},{"name":"Qi0","marks":78},{"name":"0IPn1Q","marks":19},{"name":"o4sHZh41","marks":33},{"name":"LvQSXQ","marks":35},{"name":"9H4","marks":51},{"name":"B","marks":47},{"name":"bQGehDP8g1","marks":90},{"name":"6SiBs6","marks":78},{"name":"aq8kKmK","marks":96},{"name":"8","marks":87}]

logging.info("Loaded marks: %s", marks_data)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
def get_marks(name: List[str] = Query(default=[])):
    logging.info("Query received: %s", name)
    result = [{n: marks_data.get(n, "Not Found")} for n in name]
    return JSONResponse(content={"marks": result})
