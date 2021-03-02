import html
import logging
from typing import List

from pyrogram import Client, Message, Filters

from _bot_old.functions import CheckRules, have_permission
from _bot_old.plugins import LOG_CHANNEL
from _models_old.chats import CreatorChats, AdminChats
from _models_old.rules.NameRules import NameRules

log: logging.Logger = logging.getLogger(__name__)


@Client.on_message(Filters.chat(CreatorChats.list_all() + AdminChats.list_all()) & Filters.new_chat_members)
def name_check(cli: Client, msg: Message) -> None:
    full_name: str = f"{msg.from_user.first_name} {msg.from_user.last_name}"

    rules: List[str] = [r.rule for r in NameRules.get_all()]
    reply: str = f"User: <a href='tg://user?id={msg.from_user.id}'>{html.escape(full_name)}</a>" \
                 f" [<code>{msg.from_user.id}</code>]\n" \
                 f"Group: {html.escape(msg.chat.title)}" \
                 f" [<code>{msg.chat.id}</code>]\n"

    log.debug(f"Full Name: {full_name}")

    check: CheckRules = CheckRules(full_name, rules)
    if check:
        reply += check
        if have_permission(cli.get_chat_member(msg.chat.id, cli.get_me().id)):
            cli.delete_messages(msg.chat.id, [msg.message_id])

    cli.send_message(LOG_CHANNEL, reply)