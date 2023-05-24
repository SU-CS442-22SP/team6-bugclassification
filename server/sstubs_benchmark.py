import subprocess
import json
import os
from time import sleep
from services import PMDService, InferService, ChatGPTService


def read_dataset_json(filename):
    with open(filename, "r") as file:
        dataset_json = json.load(file)
    return dataset_json


def check_repo_exists(repo_dir):
    return os.path.exists(repo_dir)


def append_csv(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")


dataset = read_dataset_json("sstubs.json")

for data in dataset:
    userName, projectName = data["projectName"].split(".")
    repo_dir = data["projectName"]
    repo_url = f"https://github.com/{userName}/{projectName}"
    fix_commit_sha1 = data["fixCommitSHA1"]
    java_file_path = data["bugFilePath"]

    if "java" not in java_file_path:
        continue
    java_file = repo_dir + "/" + java_file_path

    if check_repo_exists(repo_dir) is False:
        subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
    subprocess.run(["git", "checkout", fix_commit_sha1], cwd=repo_dir, check=True)

    with open(java_file, "r") as file:
        java_code = file.read()
    print(java_code)
    print(java_file)
    pmd = PMDService("pmd_config.xml")
    pmd_response = pmd.classify(java_file)
    print(pmd_response)
    infer = InferService()
    infer_response = infer.classify(java_file)
    print(infer_response)
    chatgpt = ChatGPTService()
    chatgpt_response = chatgpt.classify(java_file)
    append_csv("results.csv", f"{java_file},{pmd_response},{infer_response},{chatgpt_response}")
    sleep(4)