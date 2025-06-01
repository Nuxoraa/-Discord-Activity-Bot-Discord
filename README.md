# Discord VSCode Hours Faker

![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![Discord RPC](https://img.shields.io/badge/Discord-Rich%20Presence-5865F2?logo=discord)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Fake activity in Discord showing that the user has been working in Visual Studio Code for 173 hours and 43 minutes. Uses the official Discord Rich Presence API via   ```pypresence```.
---

## Возможности

- Показывает Visual Studio Code как активное приложение
- Устанавливает старт активности 173 часа и 43 минуты назад ( можно заменить ниже покажу как )
- Отображается как полноценная активность в Discord (со значком, таймером и описанием)
- Работает на любом ПК, где установлен Discord

---

## Код На питоне 

```bash
from pypresence import Presence
import time

CLIENT_ID = "123456789012345678"  # заменить на свой ID

start_timestamp = time.time() - (173 * 3600 + 43 * 60) #на данном моменте вы можете поменять цифры они отвечают за количество врпеменни в игре 

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    state="173 часа 43 минуты без перерыва", # далее сдсь можно поменять статус на что угодно 
    details="Visual Studio Code",            # сдесь тоже можно поменять 
    start=start_timestamp,            
    large_image="vscode",
    large_text="Visual Studio Code"           # и тут тоже 
)

print("Активность запущена")

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    rpc.clear()
    print("Активность остановлена")
```
- что за ID и где его взять ?
- [![Discord Developer Portal](https://img.shields.io/badge/Discord-Developer%20Portal-5865F2?logo=discord&logoColor=white)](https://discord.com/developers/applications)
- Создать новое приложение
- Скопировать Client ID и вставить его в файл  в переменную CLIENT_ID


  ## Нужные библиотеки :
```bash
pip install pypresence

