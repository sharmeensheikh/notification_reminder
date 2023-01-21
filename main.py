import time
from plyer import notification
if __name__ == '__main__':
	while True:
		notification.notify(
			title = "Title",
			message ="Description",
			timeout= 12
		)
		time.sleep(60*60)