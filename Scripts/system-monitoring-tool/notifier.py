from win10toast import ToastNotifier

notifier = ToastNotifier()

def notifiy(title, message):
    notifier.show_toast(title, message, duration=8, threaded=True)