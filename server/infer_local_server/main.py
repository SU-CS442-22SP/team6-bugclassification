from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import subprocess
from datetime import datetime
import os
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


@app.post("/infer")
async def example(file: UploadFile = File(...)):
    contents = await file.read()
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"file_{current_time}.java"
    try:
        with open(filename, "wb") as file:
            file.write(contents)
        file_path = os.path.dirname(os.path.abspath(__file__)) + "/" + filename
        command = "infer run -- javac " + file_path
        output = subprocess.check_output(command.split())
        with open("infer-out/report.json") as f:
            output = f.read()
            json_output = json.loads(output)
            bug_type = json_output[0]["bug_type"]
    except:
        bug_type = "NO_BUG"
    return {"bug_type": bug_type}
