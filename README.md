# Discord VSCode Hours Faker

![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![Discord RPC](https://img.shields.io/badge/Discord-Rich%20Presence-5865F2?logo=discord)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Фейковая активность в Discord, показывающая, что пользователь работает в Visual Studio Code уже 173 часа 43 минуты. Используется официальный Discord Rich Presence API через `pypresence`.

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

