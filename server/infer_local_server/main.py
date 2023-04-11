from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import subprocess
from datetime import datetime
import os

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
    with open(filename, "wb") as file:
        file.write(contents)
    file_path = os.path.dirname(os.path.abspath(__file__)) + "/" + filename
    command = "infer run -- javac " + file_path
    output = subprocess.check_output(command.split())
    print(output)
    return output
