import requests

from kickapi.objects import User

def get_user(username: str, headers: dict, session: requests.Session, api_url: str = "https://kick.com/api/v2") -> User:
    r = session.get(f"{api_url}/channels/{username}", headers=headers)
    data = r.json()
    user = User(**data["user"])
    return user