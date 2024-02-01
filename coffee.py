import pyautogui as pag
import time
import rumps

class CoffeeApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Coffee",
            "start": "Start Timer",
            "stop": "Stop Timer",
            "interval_secs": 120,
        }
        self.app = rumps.App(self.config["app_name"])
        self.timer = rumps.Timer(self.on_tick, 1)
        self.interval_secs = self.config["interval_secs"]
        self.set_up_menu()
        self.start_stop_button = rumps.MenuItem(title=self.config["stop"], callback=self.start_timer)
        self.app.menu = [self.start_stop_button]
        self.reset_timer()
        self.timer.start()

    def set_up_menu(self):
        self.timer.stop()
        self.timer.count = 0
        self.app.title = "☕️"

    def on_tick(self, sender):
        print("tick")
        time_left = sender.end - sender.count
        mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
        secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
        if mins == 0 and time_left < 0:
            self.on_prevent_sleep()
            self.reset_timer()
        sender.count += 1
    
    def on_prevent_sleep(self):
        print("on_prevent_sleep")
        pag.moveRel(1,1)

    def reset_timer(self):
        self.timer.count = 0
        self.timer.end = self.interval_secs

    def start_timer(self, sender):
        if sender.title.lower().startswith("start"):
            self.timer.count = 0
            self.timer.end = self.interval_secs
            sender.title = self.config["stop"]
            self.timer.start()
        else:
            sender.title = self.config["start"]
            self.timer.stop()

    def stop_timer(self, sender):
        self.set_up_menu()
        self.stop_button.set_callback(None)
        self.start_stop_button.title = self.config["start"]

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = CoffeeApp()
    app.run()
