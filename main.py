from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
from fuzzywuzzy import fuzz,process
import requests
import os
from typing import Optional
import mysql.connector
import re

load_dotenv()


DEBUG = os.environ.get("DEBUG")
PORT = 5000 if os.environ.get("PORT") is None else int(os.environ.get("PORT"))
# DRUG_SERVICE_URL = os.environ.get("DRUG_SERVICE_URL")

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DATABASE = os.environ.get("DB_DATABASE")



select_query = "select * from drugs"
ctx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD,
                              host=DB_HOST,
                              database=DB_DATABASE)

cursor = ctx.cursor()
app = FastAPI(docs_url="/api/ocr/documentation",debug=DEBUG)
responsePayload = {
    "service" : "ocr service", 
    "status" : "success", 
    "request" : None, 
    "response" : {
        "data" : None,
        "total" : None
    }
}


class Payload(BaseModel):
    title: str
    score : Optional[int] = None

@app.post("/api/ocr")
def findDrugTitle(request : Payload):
    cursor.execute(select_query)
    columns = cursor.description 
    drugs = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    matches = []
    score = 80 if request.score is None else int(request.score)
    for drug in drugs:
        similarity = fuzz.token_set_ratio(request.title.lower(), drug['title'].lower())
        drug["title"] = re.split("[\d.]", drug['title'])[0]
        if(similarity > score):
            matches.append(drug)

    
    responsePayload['response']['data'] = matches
    responsePayload['request'] = request
    return responsePayload

@app.on_event("startup")
def startup():
    print(f"server running on port: {PORT}")