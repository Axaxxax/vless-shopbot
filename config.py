# Структура: 'callback_data': ('Название для кнопки', 'Цена в рублях', 'Кол-во месяцев')
PLANS = {
    "buy_1_month": ("1 месяц", "50.00", 1),
    "buy_3_months": ("3 месяца", "135.00", 3),
    "buy_6_months": ("6 месяцев", "240.00", 6),
    "buy_12_months": ("12 месяцев", "450.00", 12),
}



WELCOME_MESSAGE = (
    "👋 Добро пожаловать в NNVPN Бот!\n\n"
    "Здесь вы можете приобрести быстрый и надежный VPN."
)

CHOOSE_PLAN_MESSAGE = "Выберите подходящий тариф:"

PROFILE_NO_DATA_MESSAGE = (
    "Про вас пока нет информации в нашей системе.\n"
    "Совершите покупку, чтобы создать профиль!"
)

def get_profile_text(username, total_spent, total_months, vpn_status_text):
    return (
        f"👤 <b>Профиль:</b> {username}\n\n"
        f"💰 <b>Потрачено всего:</b> {total_spent:.0f} RUB\n"
        f"📅 <b>Приобретено месяцев:</b> {total_months}\n\n"
        f"{vpn_status_text}"
    )

def get_vpn_active_text(days_left, hours_left):
    return (
        f"✅ <b>Статус VPN:</b> Активен\n"
        f"⏳ <b>Осталось:</b> {days_left} д. {hours_left} ч."
    )

VPN_INACTIVE_TEXT = "❌ <b>Статус VPN:</b> Неактивен (срок истек)"
VPN_NO_DATA_TEXT = "ℹ️ <b>Статус VPN:</b> Нет данных"