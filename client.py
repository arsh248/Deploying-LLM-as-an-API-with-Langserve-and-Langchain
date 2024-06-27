import requests

response=requests.post(
    "http://localhost:8001/poem/invoke",
    json={'input':{'topic':"my best friend"}})

print(response.json()['output']['content'])

