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
