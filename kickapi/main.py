from curl_cffi.requests import AsyncSession
import traceback
from curl_cffi.requests.exceptions import SSLError
from kickapi.methods import get_channel, get_livestream, get_user
from kickapi.objects import Channel, Livestream, User
from kickapi.utils.errors import NoLivestreamError, JSONFailedError
from kickapi.cookies import fetch_new_cookies, load_cookies

class Kick:
    def __init__(self, username: str = None) -> None:
        self.username = username
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
    
    async def get_channel(self) -> Channel:
        async with AsyncSession(headers=self.headers) as session:
            try:
                cookies = load_cookies()
                if cookies:
                    session.cookies.jar._cookies.update(cookies)
                    
                return await get_channel(self.username, session, cookies)
            except ValueError:
                cookies = await fetch_new_cookies()
                try:
                    return await get_channel(self.username, session, cookies)
                except Exception:
                    traceback.print_exc()

    async def get_livestream(self) -> Livestream:
        print(self.username)
        async with AsyncSession(headers=self.headers) as session:
            try:
                cookies = load_cookies()
                if cookies:
                    session.cookies.jar._cookies.update(cookies)
                    
                res = await get_livestream(self.username, session, cookies)
                print(res)
                return res
            except ValueError:
                cookies = await fetch_new_cookies(self.username)
                print(cookies)
                try:
                    res = await get_livestream(self.username, session, cookies)
                    print(res)
                    return res
                except Exception:
                    traceback.print_exc()
            except SSLError:
                print('SSLError')
            except:
                raise NoLivestreamError

    async def get_user(self) -> User:
        async with AsyncSession(headers=self.headers) as session:
            try:
                cookies = load_cookies()
                if cookies:
                    session.cookies.jar._cookies.update(cookies)
                    
                return await get_user(self.username, session, cookies)
            except ValueError:
                cookies = await fetch_new_cookies()
                try:
                    return await get_user(self.username, session, cookies)
                except Exception:
                    traceback.print_exc()

    def __str__(self) -> str:
        return f"Kick api for {self.username}"
    
    # def __enter__(self):
    #     return self
    
    # def __exit__(self, exc_type, exc_value, traceback):
    #     self.session.close()
    
    # def __aenter__(self):
    #     return self
    
    # def __aexit__(self, exc_type, exc_value, traceback):
    #     self.session.close()