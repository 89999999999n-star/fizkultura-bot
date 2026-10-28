CHANNEL = "@FIZKYLTYRA11"

async def check_subscription(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ("creator", "administrator", "member") or (
            member.status == "restricted" and member.is_member
        )
    except Exception:
        return False
