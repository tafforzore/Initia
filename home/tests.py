import json, requests
url = "http://95.111.235.145:8000/api/authentification/"  
data = {
    'username' : 'username',
    'phonenumber': '+237656426897',
    'email' : 'email',
    'password' : 'password',
    'oauth_github': '123',
}
payload = json.dumps(data)

headers = {
    "Content-Type": "application/json", 
}

response = requests.post(url, data=payload, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("la requette ne c'est pas executer")