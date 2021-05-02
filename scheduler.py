# import notification
from plyer import notification
import time

if __name__=="__main__":
    while True:
        notification.notify(
        title="REMINDER:",
        message="You have My Hero Academia to watch",
        timeout=1
    )
        time.sleep(5)
