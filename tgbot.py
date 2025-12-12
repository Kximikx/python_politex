from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 1) СЮДИ ВСТАВЛЯЄШ СВІЙ ТОКЕН ВІД BotFather
TOKEN = "8408018195:AAH-jWIIQ8ArxJnsW3vAq_481i0Tzj5fq-8"

# 2) ЯКЩО ХОЧЕШ ВІДПРАВЛЯТИ ФОТО ЧЕРЕЗ file_id,
#    ВСТАВ ЙОГО СЮДИ. Якщо поки не маєш – лиши пустим рядком.
LOCK_PHOTO_FILE_ID = ""  # Наприклад: "AgACAgIAAxkBAAIBGWZ...."

# Головне меню (кнопки)
main_menu = ReplyKeyboardMarkup(
    [
        ["ℹ️ Детальна інформація про замок"],
        ["📞 Контакти"],
        ["🌐 Соц мережі"]
    ],
    resize_keyboard=True
)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Вітаю! Це офіційний бот розумного замка SmartLock.\n"
        "Оберіть, що вас цікавить:",
        reply_markup=main_menu
    )


def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    chat_id = update.message.chat_id

    if text == "ℹ️ Детальна інформація про замок":
        info_text = (
            "SmartLock — це інтелектуальний замок нового покоління для готелів та квартир.\n\n"
            "Основні можливості:\n"
            "- Керування через смартфон\n"
            "- Підтримка NFC-карт та PIN-кодів\n"
            "- Генерація тимчасових цифрових ключів для гостей\n"
            "- Журнал подій у реальному часі\n"
            "- Інтеграція з готельними системами управління\n"
        )

        # Якщо ти вкажеш LOCK_PHOTO_FILE_ID, бот відправить фото + опис
        if LOCK_PHOTO_FILE_ID:
            context.bot.send_photo(
                chat_id=chat_id,
                photo=LOCK_PHOTO_FILE_ID,
                caption=info_text
            )
        else:
            # Якщо фото не налаштоване – просто текст
            update.message.reply_text(info_text)

    elif text == "📞 Контакти":
        update.message.reply_text(
            "Наші контакти:\n"
            "Email: support@smartlock.com\n"
            "Телефон: +380 99 123 45 67\n"
            "Менеджер: Богдан"
        )

    elif text == "🌐 Соц мережі":
        update.message.reply_text(
            "Наші соціальні мережі:\n"
            "Instagram: instagram.com/smartlock\n"
            "Facebook: facebook.com/smartlock\n"
            "YouTube: youtube.com/@smartlock"
        )

    else:
        update.message.reply_text(
            "Будь ласка, оберіть пункт меню нижче.",
            reply_markup=main_menu
        )


def main():
    # 3) СЮДИ НІЧОГО НЕ ТРЕБА МІНЯТИ – ГОЛОВНЕ, ЩОБ TOKEN БУВ ВИЩЕ ПРАВИЛЬНИЙ
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
