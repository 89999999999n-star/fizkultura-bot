from telegram import InlineKeyboardButton, InlineKeyboardMarkup

CHANNEL = "@FIZKYLTYRA11"

def subscription_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "ПОДПИСАТЬСЯ НА КАНАЛ",
            url="https://t.me/FIZKYLTYRA11"
        )],
        [InlineKeyboardButton(
            "ПРОВЕРИТЬ ПОДПИСКУ",
            callback_data="check_subscription"
        )]
    ])
