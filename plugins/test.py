import logging

from pyrogram import Client, Message, Filters

log = logging.getLogger(__name__)


@Client.on_message(Filters.dan & Filters.me)
def test(cli: Client, msg: Message) -> None:
    """Empty for copy"""
    raise NotImplemented
