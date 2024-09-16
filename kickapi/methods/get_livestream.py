import requests

from kickapi.objects import Livestream

def get_livestream(username: str, headers: dict, session: requests.Session, api_url: str = "https://kick.com/api/v2") -> Livestream:
    r = session.get(f"{api_url}/channels/{username}", headers=headers)
    data = r.json()
    livestream = Livestream(**data["livestream"])
    return livestream