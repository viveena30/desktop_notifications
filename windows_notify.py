from plyer import notification
import time

# run this using """pythonw""" so the application runs in background

if __name__ == '__main__':
    while True:
        notification.notify(
            # update the notification components as per your requirement here.
            title = "Please Drink Water",
            message = "Water is essential for the body to function properly. It helps to regulate body temperature",
            timeout=5,
        )
        # specify the wait period before the next notification comes up. 
        time.sleep(10)