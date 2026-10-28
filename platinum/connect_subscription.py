from pathlib import Path

root = Path.home() / "dvizh-bot"
source = root / "bot_fixed.py"
target = root / "bot_platinum.py"

code = source.read_text(encoding="utf-8")

if 'async def start(' not in code:
    raise SystemExit("Не найден обработчик start. Ничего не изменено.")

if 'app.add_handler(CommandHandler("start", start))' not in code:
    raise SystemExit("Не найдена регистрация /start. Ничего не изменено.")

if 'app.run_polling()' not in code:
    raise SystemExit("Не найден запуск бота. Ничего не изменено.")

if 'CallbackQueryHandler' not in code:
    raise SystemExit("Не найден импорт CallbackQueryHandler.")

code = code.replace(
    'async def start(',
    '''from platinum.sub_menu import subscription_menu
from platinum.check_sub import check_subscription

async def platinum_start(update, ctx):
    subscribed = await check_subscription(
        ctx.bot, update.effective_user.id
    )
    if not subscribed:
        await update.message.reply_text(
            "💎 ФИЗКУЛЬТУРА PLATINUM\\\\n\\\\n"
            "Для входа подпишись на наш бесплатный канал.",
            reply_markup=subscription_menu()
        )
        return
    await start(update, ctx)

async def platinum_check(update, ctx):
    q = update.callback_query
    await q.answer()
    subscribed = await check_subscription(
        ctx.bot, q.from_user.id
    )
    if not subscribed:
        await q.message.reply_text(
            "Подписка пока не найдена. Подпишись и проверь ещё раз.",
            reply_markup=subscription_menu()
        )
        return
    await q.message.reply_text(
        "✅ Подписка подтверждена! "
        "Отправь /start, чтобы открыть меню тренировок."
    )

async def start(''',
    1
)

code = code.replace(
    'app.add_handler(CommandHandler("start", start))',
    '''app.add_handler(CommandHandler("start", platinum_start))
    app.add_handler(CallbackQueryHandler(
        platinum_check, pattern="^check_subscription$"
    ))''',
    1
)

target.write_text(code, encoding="utf-8")
print("PLATINUM_CREATED")
