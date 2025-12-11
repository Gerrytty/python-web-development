import requests

payload = {
    "jsonrpc": "2.0",
    "method": "sum",
    "params": [5, 7],
    "id": 1
}

r = requests.post("http://localhost:5050", json=payload)
print("Response:", r.text)

