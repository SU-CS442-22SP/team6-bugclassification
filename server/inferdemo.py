from infer import InferService

infer_service = InferService()
reply = infer_service.classify(open("bug1.java").read())
print("ChatGPT reply:", reply)
