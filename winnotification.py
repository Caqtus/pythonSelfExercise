import time
from plyer import notification


def createnotification():


        while True:
            notification.notify(title = "ALERT!!!", message = "Take out break")
            time.sleep(3600)