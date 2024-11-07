from dataclasses import dataclass, field
from typing import List, Optional
from .livestream import Livestream
from .user import User


@dataclass
class BadgeImage:
    src: str
    srcset: str = ""

@dataclass
class SubscriberBadge:
    badge_image: BadgeImage
    channel_id: int
    id: int
    months: int

@dataclass
class Chatroom:
    channel_id: int
    chat_mode: str
    chat_mode_old: str
    chatable_id: int
    chatable_type: str
    created_at: str
    emotes_mode: bool
    followers_mode: bool
    following_min_duration: int
    id: int
    message_interval: int
    slow_mode: bool
    subscribers_mode: bool
    updated_at: str

@dataclass
class Image:
    url: str

@dataclass
class OfflineBannerImage:
    src: str
    srcset: str

@dataclass
class Channel:
    id: int
    user_id: int
    vod_enabled: bool
    verified: bool
    can_host: bool
    followers_count: int
    is_banned: bool
    muted: bool
    playback_url: str
    slug: str
    subscription_enabled: bool
    user: User
    livestream: Livestream
    chatroom: Chatroom
    banner_image: Image
    offline_banner_image: OfflineBannerImage
    role: Optional[str]
    follower_badges: List[str] = field(default_factory=list)
    subscriber_badges: List[SubscriberBadge] = field(default_factory=list)
    recent_categories: List[str] = field(default_factory=list)