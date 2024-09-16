import requests

from kickapi.methods import get_channel, get_livestream, get_user
from kickapi.objects import Channel, Livestream, User
from kickapi.utils.errors import NoLivestreamError, JSONFailedError


class Kick:
    def __init__(self, username: str) -> None:
        self.username = username
        self.session = requests.Session()
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Accept-Language": "ar,en-US;q=0.7,en;q=0.3",
            "Alt-Used": "kick.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
        }
    
    def get_channel(self) -> Channel:
        try:
            return get_channel(self.username, self.headers, self.session)
        except ValueError:
            raise JSONFailedError

    def get_livestream(self) -> Livestream:
        try:
            return get_livestream(self.username, self.headers, self.session)
        except ValueError:
            raise JSONFailedError
        except:
            raise NoLivestreamError

    def get_user(self) -> User:
        try:
            return get_user(self.username, self.headers, self.session)
        except ValueError:
            raise JSONFailedError

    def __str__(self) -> str:
        return f"Kick api for {self.username}"
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()