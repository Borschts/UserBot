import logging

from sqlalchemy import BigInteger, Boolean, Column, Integer, String

from database.mixin import BaseMixin, TimestampMixin
from main import db

log: logging.Logger = logging.getLogger(__name__)


class User(db.base, BaseMixin, TimestampMixin):
    uid: int = Column(BigInteger, nullable=False)
    dc_id: int = Column(Integer)
    first_name: str = Column(String(64))
    last_name: str = Column(String(64))
    username: str = Column(String(64))
    about: str = Column(String(128))

    bot: bool = Column(Boolean, nullable=False)
    deleted: bool = Column(Boolean, nullable=False)
    verified: bool = Column(Boolean, nullable=False)
    scam: bool = Column(Boolean, nullable=False)
    support: bool = Column(Boolean, nullable=False)
    restricted: bool = Column(Boolean, nullable=False)

    phone_calls_available: bool = Column(Boolean, nullable=False)
    phone_calls_private: bool = Column(Boolean, nullable=False)
    video_calls_available: bool = Column(Boolean, nullable=False)

    bot_chat_history: bool = Column(Boolean)
    bot_nochats: bool = Column(Boolean)
    bot_inline_geo: bool = Column(Boolean)
    bot_inline_placeholder: bool = Column(Boolean)
    bot_info_version: int = Column(Integer)
    bot_description: str = Column(String(512))

    common_chats_count: int = Column(Integer, nullable=False)

    def __init__(self, uid: int):
        self.uid = uid
