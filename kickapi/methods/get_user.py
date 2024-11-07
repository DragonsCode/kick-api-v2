from curl_cffi.requests import AsyncSession
import certifi
from kickapi.objects import User

async def get_user(username: str, session: AsyncSession, cookies=None, api_url: str = "https://kick.com/api/v2") -> User:
    r = await session.get(f"{api_url}/channels/{username}", cookies=cookies, verify=certifi.where())
    data = r.json()
    user = User(**data["user"])
    return user