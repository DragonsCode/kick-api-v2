from curl_cffi.requests import AsyncSession
import certifi
from kickapi.objects import Livestream

async def get_livestream(username: str, session: AsyncSession, cookies=None, api_url: str = "https://kick.com/api/v2") -> Livestream:
    r = await session.get(f"{api_url}/channels/{username}", cookies=cookies, verify=certifi.where())
    if r.content:
        print("Received response: ", r.text)
        data = r.json()
    else:
        # Handle the empty response scenario, maybe retry or log the error
        print("Received empty response")
        data = None  # Or handle appropriately
    livestream = Livestream(**data["livestream"])
    return livestream