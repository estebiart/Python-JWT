import jwt
import json



url_json= 'payload.json'
json_data = json.dumps(url_json)
with open(url_json, "r") as j:
    payload_data=json.load(j)
    print(payload_data)
key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
token=jwt.encode( 
    payload=payload_data,
    key=key
    )
print(token)