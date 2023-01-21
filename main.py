import time
from plyer import notification
if __name__ == '__main__':
	while True:
		notification.notify(
			title = "Daily Reminder",
			message = "Amazing things will happen to you!",
			app_icon = "icon.ico",
			timeout = 12
		)
		# delay for 24 hours
		time.sleep(60*60)