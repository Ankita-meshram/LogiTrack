import threading

class NotificationEngine:

    @staticmethod
    def send_notification(receiver, tracking_id, status):

        def notify():
            print("--------------------------------")
            print("Parcel Notification")
            print("--------------------------------")
            print(f"Receiver : {receiver}")
            print(f"Tracking ID : {tracking_id}")
            print(f"Current Status : {status}")
            print("--------------------------------")

        thread = threading.Thread(target=notify)
        thread.start()