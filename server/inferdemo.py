from services import InferService
import glob


# Get all tests files
test_files = glob.glob("./benchmarks/test/*.java")

for artifact in test_files:
    infer_service = InferService()
    reply = infer_service.classify(artifact)
    print("Artifact: ", artifact, "Infer reply:", reply)