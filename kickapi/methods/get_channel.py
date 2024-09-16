import requests

from kickapi.objects import Channel

def get_channel(username: str, headers: dict, session: requests.Session, api_url: str = "https://kick.com/api/v2") -> Channel:
    r = session.get(f"{api_url}/channels/{username}", headers=headers)
    data = r.json()
    channel = Channel(**data)
    return channel