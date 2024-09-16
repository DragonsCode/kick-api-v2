from dataclasses import dataclass


@dataclass
class Livestream:
    categories: list
    channel_id: int
    created_at: str
    duration: int
    id: int
    is_live: bool
    is_mature: bool
    language: str
    risk_level_id: int
    session_title: str
    slug: str
    source: str
    start_time: str
    tags: list
    thumbnail: dict
    twitch_channel: str
    viewer_count: int