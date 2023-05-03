from services.chatgpt import ChatGPTService
from services.infer import InferService
import glob

# Get all tests files
test_files = glob.glob("./benchmarks/test/*.java")

results = []

for artifact in test_files:
    gpt_service = ChatGPTService()
    infer_services = InferService()
    reply_gpt = gpt_service.classify(open(artifact).read())
    reply_infer = infer_services.classify(open(artifact).read())
    artifact_name = artifact.split("/")[-1].replace(".java", "")
    results.append({"artifact": artifact_name, "gpt": reply_gpt, "infer": reply_infer})

with open("results.json", "w") as f:
    f.write(str(results))
