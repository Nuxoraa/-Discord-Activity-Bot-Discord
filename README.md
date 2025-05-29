# 🕒 Discord Activity Bot

<h2 align="center">✨ Custom Rich Presence with Inflated Hours ✨</h2>

## 📝 Description
This Python script allows you to display custom Discord rich presence with inflated hours. Perfect for those who want to showcase their "dedication"! 😉

## ⚠️ Warning
❗ Using this to artificially inflate hours may violate Discord's ToS. Use at your own risk!

## 🛠️ Installation
```bash
pip install pypresence
🚀 Usage
Make sure Discord is running

Run the script:

bash
python discord_activity.py
Enjoy your inflated activity! 🎉

Press Ctrl+C to stop

⚙️ Configuration
Edit these variables in the code:

CLIENT_ID - Your Discord application ID

state - Status text (e.g., "Coding 24/7" 🧑‍💻)

details - Activity details

large_image - Asset key for large image

🕒 Бот активности для Discord
<h2 align="center">✨ Пользовательская активность с накрученными часами ✨</h2>
📝 Описание
Этот Python-скрипт позволяет отображать пользовательскую активность в Discord с накрученными часами. Идеально для тех, кто хочет показать свою "преданность"! 😉

⚠️ Предупреждение
❗ Искусственное увеличение часов может нарушать правила Discord. Используйте на свой страх и риск!

🛠️ Установка
bash
pip install pypresence
🚀 Использование
Убедитесь, что Discord запущен

Запустите скрипт:

bash
python discord_activity.py
Наслаждайтесь накрученной активностью! 🎉

Нажмите Ctrl+C для остановки

⚙️ Настройка
Изменяемые параметры в коде:

CLIENT_ID - ID вашего приложения Discord

state - Текст статуса (например, "Кодинг 24/7" 🧑‍💻)

details - Детали активности

large_image - Ключ для большого изображения

💻 Код / Code
python
# Import libraries / Импорт библиотек
from pypresence import Presence
import time

# Configuration / Конфигурация
CLIENT_ID = "1363151422618734703"  # Replace with your ID / Замените на свой ID

# Initialize RPC / Инициализация RPC
rpc = Presence(CLIENT_ID)
rpc.connect()

# Calculate start time / Вычисление времени начала
start_time = time.time() - (99999 * 9999 + 99 * 99)

# Update presence / Обновление активности
rpc.update(
    state="debugging in index.html",  # 🔍
    details="Visual Studio Code",     # 💻
    start=start_time,
    large_image="vscode",            # 🖼️
    large_text="VS Code"
)

print("✅ Activity started! / Активность запущена!")

# Keep running / Поддержание активности
try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    rpc.clear()
    print("🛑 Script stopped. / Скрипт остановлен.")
<h3 align="center"> Made with ❤️ and Python 🐍 | Сделано с ❤️ и Python 🐍 </h3> ```
