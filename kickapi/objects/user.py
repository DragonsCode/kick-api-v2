from dataclasses import dataclass


@dataclass
class User:
    agreed_to_terms: bool
    bio: str
    city: str
    country: str
    discord: str
    email_verified_at: str
    facebook: str
    id: int
    instagram: str
    profile_pic: str
    state: str
    tiktok: str
    twitter: str
    username: str
    youtube: str