# Discord VSCode Hours Faker

![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![Discord RPC](https://img.shields.io/badge/Discord-Rich%20Presence-5865F2?logo=discord)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Fake activity in Discord showing that the user has been working in Visual Studio Code for 173 hours and 43 minutes. Uses the official Discord Rich Presence API via   ```pypresence```.
---

## Features
Shows Visual Studio Code as the active application

Sets the start of activity to 173 hours and 43 minutes ago (you can change this below, I’ll show how)

Appears as full presence in Discord (with icon, timer, and description)

Works on any PC with Discord installed
---

## Python Code 

```bash
from pypresence import Presence
import time

CLIENT_ID = "123456789012345678"  # replace with your own ID

start_timestamp = time.time() - (173 * 3600 + 43 * 60) # you can change these numbers, they control how much time is shown

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    state="173 hours 43 minutes non-stop",  # here you can change the status to anything
    details="Visual Studio Code",           # here too
    start=start_timestamp,            
    large_image="vscode",
    large_text="Visual Studio Code"         # and here as well
)

print("Activity started")

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    rpc.clear()
    print("Activity stopped")

```
- What is the ID and where to get it?
- [![Discord Developer Portal](https://img.shields.io/badge/Discord-Developer%20Portal-5865F2?logo=discord&logoColor=white)](https://discord.com/developers/applications)
- Create a new application
- Copy the Client ID and paste it into the script in the `CLIENT_ID` variable


  ## Required libraries:
```bash
pip install pypresence

