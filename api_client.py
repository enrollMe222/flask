import requests

response = requests.get('http://127.0.0.1:5000/api/users')
if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"Username: {user['username']}")
else:
    print("Failed to retrieve users")
