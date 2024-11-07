from curl_cffi.requests import AsyncSession
import certifi
from kickapi.objects import Channel

async def get_channel(username: str, session: AsyncSession, cookies=None, api_url: str = "https://kick.com/api/v2") -> Channel:
    r = await session.get(f"{api_url}/channels/{username}", cookies=cookies, verify=certifi.where())
    data = r.json()
    channel = Channel(**data)
    return channel