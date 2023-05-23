from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import subprocess
from datetime import datetime
import os
from pprint import pprint
from services.pmd import PMDService
from services.infer import InferService
from services.chatgpt import ChatGPTService
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def save_file(file):
    contents = await file.read()
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"file_{current_time}.java"
    with open("files/" + filename, "wb") as file:
        file.write(contents)
    file_path = os.path.dirname(os.path.abspath(__file__)) + "/files/" + filename
    return file_path

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    file_path = await save_file(file)
    pmd_service = PMDService("config.xml")
    infer_service = InferService()
    chatgpt_service = ChatGPTService()
    pmd_response = pmd_service.classify(file_path)
    infer_response = infer_service.classify(file_path)
    chatgpt_response = chatgpt_service.classify(file_path)
    return {"pmd": pmd_response, "infer": infer_response, "chatgpt": chatgpt_response}
