from services.chatgpt import ChatGPTService
import glob

# Get all tests files
test_files = glob.glob("./benchmarks/test/*.java")

for artifact in test_files:
    gpt_service = ChatGPTService()
    reply = gpt_service.classify(artifact)
    print("Artifact: ", artifact, "ChatGPT reply:", reply)