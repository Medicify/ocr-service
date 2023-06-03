from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
from fuzzywuzzy import fuzz,process
import requests
import os
from typing import Optional

load_dotenv()


DEBUG = os.environ.get("DEBUG")
PORT = 5000 if os.environ.get("PORT") is None else int(os.environ.get("PORT"))
DRUG_SERVICE_URL = os.environ.get("DRUG_SERVICE_URL");




app = FastAPI(docs_url="/api/recommendation/documentation",debug=DEBUG)
responsePayload = {
    "service" : "recommendation service", 
    "status" : "success", 
    "request" : None, 
    "response" : {
        "data" : None,
        "total" : None
    }
}


class RecommendationPayload(BaseModel):
    title: str
    score : Optional[int] = None

@app.post("/api/ocr")
def findDrugTitle(request : RecommendationPayload):
    drugs = requests.get(f"{DRUG_SERVICE_URL}/api/drugs").json()['response']['data']
    matches = []
    score = 80 if request.score is None else int(request.score)
    for drug in drugs:
        similarity = fuzz.token_set_ratio(request.title.lower(), drug['title'].lower())
        if(similarity > score):
            matches.append(drug)
    responsePayload['response']['data'] = matches
    responsePayload['request'] = request
    return responsePayload

@app.on_event("startup")
def startup():
    print(f"server running on port: {PORT}")