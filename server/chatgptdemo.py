from chatgpt import ChatGPTService

gpt_service = ChatGPTService()
reply = gpt_service.classify(open("bug1.java").read())
print("ChatGPT reply:", reply)
