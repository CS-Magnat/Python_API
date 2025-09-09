import httpx

from tools.fakers import fake

payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user = httpx.post("http://localhost:8000/api/v1/users", json=payload)
resp = create_user.json()
print(resp)



payload_aut = {
    "email": payload ["email"],
    "password": payload ["password"]
}

reg = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload_aut)
req1 = reg.json()
print(req1)



pat = {
  "email": "user7@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

head = {
    "Authorization": f"Bearer {req1['token']['accessToken']}"
}
upd = httpx.patch(f"http://localhost:8000/api/v1/users/{resp["user"] ["id"]}", json=pat, headers=head)
print("patch:", upd.json())