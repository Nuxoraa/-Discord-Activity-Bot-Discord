"""
#################################################
### 🎮 DISCORD ACTIVITY BOOSTER PRO           ###
### ⚠️ Only for educational purposes        ###
### ⚠️ Только для обучения! Не для обмана!  ###
#################################################

⭐ ВСЁ-В-ОДНОМ: код + инструкция + настройки
⭐ Просто скопируйте и запустите!
⭐ Автоматическая накрутка часов в Discord
"""

import time
import sys
from pypresence import Presence

class DiscordBooster:
    def __init__(self):
        #######################################
        ### 🔧 НАСТРОЙКИ (ИЗМЕНИТЕ ПОД СЕБЯ) ###
        #######################################
        
        # 🔑 Получите на https://discord.com/developers/applications
        self.CLIENT_ID = "ВАШ_CLIENT_ID"  
        
        # 📝 Тексты статуса
        self.STATE_TEXT = "Coding 24/7"          # Вторая строка статуса
        self.DETAILS_TEXT = "Visual Studio Code" # Первая строка статуса
        
        # 🖼️ Изображения (загрузите в Discord Dev Portal)
        self.LARGE_IMAGE = "vscode"             # Ключ большого изображения
        self.LARGE_TEXT = "VS Code Pro"          # Текст при наведении
        
        # ⏱️ Настройки времени (можно не менять)
        self.start_time = time.time() - (87600 * 3600)  # ~10 лет "активности"
        
        #######################################
        ### 🖥️ ИНИЦИАЛИЗАЦИЯ ИНТЕРФЕЙСА     ###
        #######################################
        
        print("\n" + "="*48)
        print("🎮 DISCORD ACTIVITY BOOSTER v2.0")
        print("="*48)
        print(f"🔑 Client ID: {self.CLIENT_ID}")
        print(f"📝 Status: {self.STATE_TEXT}")
        print(f"ℹ️ Details: {self.DETAILS_TEXT}")
        print("="*48 + "\n")
        print("⚡ Запуск бота... (Ctrl+C для остановки)")

    def start(self):
        """Основной цикл работы бота"""
        try:
            # Подключение к Discord
            self.rpc = Presence(self.CLIENT_ID)
            self.rpc.connect()
            
            # Первое обновление статуса
            self.update_presence()
            
            # Главный цикл
            while True:
                time.sleep(15)  # Обновление каждые 15 секунд
                self.update_presence()
                
        except Exception as e:
            print(f"❌ Ошибка: {str(e)}")
            self.stop()

    def update_presence(self):
        """Обновление Rich Presence"""
        self.rpc.update(
            state=self.STATE_TEXT,
            details=self.DETAILS_TEXT,
            start=self.start_time,
            large_image=self.LARGE_IMAGE,
            large_text=self.LARGE_TEXT
        )

    def stop(self):
        """Корректное завершение работы"""
        if hasattr(self, 'rpc') and self.rpc:
            self.rpc.clear()
            print("\n" + "="*48)
            print("🛑 Бот остановлен. Активность очищена")
            print("="*48 + "\n")
        sys.exit(0)

if __name__ == "__main__":
    bot = DiscordBooster()
    
    try:
        bot.start()
    except KeyboardInterrupt:
        bot.stop()
    except Exception as e:
        print(f"💥 Критическая ошибка: {str(e)}")
        bot.stop()


#################################################
### 📚 ПОЛНАЯ ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ    ###
#################################################

"""
⭐ КАК ЗАПУСТИТЬ:
1. Установите Python 3.8+ (https://python.org)
2. Установите библиотеку: 
   pip install pypresence
3. Замените настройки в коде (см. раздел НАСТРОЙКИ)
4. Запустите: python bot.py
5. Для остановки: Ctrl+C

⭐ КАК ПОЛУЧИТЬ CLIENT_ID:
1. Откройте https://discord.com/developers/applications
2. Создайте новое приложение
3. Во вкладке "Rich Presence" загрузите изображения
4. Скопируйте Application ID -> это ваш CLIENT_ID

⭐ ВАЖНЫЕ ЗАМЕТКИ:
• Discord должен быть запущен!
• Изображения должны быть 512x512px
• Не используйте для реального обмана!
• Код работает в Windows/MacOS/Linux

⭐ ВОЗМОЖНЫЕ ПРОБЛЕМЫ:
1. Статус не обновляется:
   - Проверьте CLIENT_ID
   - Перезапустите Discord
2. Ошибка подключения:
   - Убедитесь что Discord запущен
   - Попробуйте другой CLIENT_ID
3. Изображения не отображаются:
   - Проверьте ключи изображений
   - Подождите 5-10 минут

Для вопросов: создайте Issue на GitHub
"""
