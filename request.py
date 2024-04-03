import requests

# Replace with your actual endpoint and credentials
auth_url = 'http://20.244.56.144/test/auth'
payload = {
    "companyName": "GoMarket",
    "clientId": "47be243a-77cd-4459-affe-125abac6604d",
    "clientSecret": "RNWUPFNWQYlpDaJY",
    "ownerName": "Chirag Gupta",
    "ownerEmail": "cs8467@srmist.edu.in",
    "rollNo": "RA2111003010171",
    "accessCode": "bntKpm"
}

# Send POST request to obtain the authorization token
response = requests.post(auth_url, json=payload)

# Assuming the response contains JSON with the token information
token_data = response.json()

print(token_data)
