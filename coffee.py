import pyautogui as pag
import time
import rumps

class CoffeeApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Coffee",
            "start": "Start Timer",
            "pause": "Pause Timer",
            "continue": "Continue Timer",
            "stop": "Stop Timer",
            "break_message": "Time is up! Take a break :)",
            "interval": 10,
        }
        self.app = rumps.App(self.config["app_name"])
        self.timer = rumps.Timer(self.on_tick, 1)
        self.interval = self.config["interval"]
        self.set_up_menu()
        self.start_pause_button = rumps.MenuItem(title=self.config["start"], callback=self.start_timer)
        self.stop_button = rumps.MenuItem(title=self.config["stop"], callback=None)
        self.app.menu = [self.start_pause_button, self.stop_button]

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
        else:
            self.stop_button.set_callback(self.stop_timer)
        sender.count += 1
    
    def on_prevent_sleep(self):
        print("on_prevent_sleep")
        pag.moveRel(1,1)

    def reset_timer(self):
        self.timer.count = 0
        self.timer.end = self.interval

    def start_timer(self, sender):
        if sender.title.lower().startswith(("start", "continue")):
            if sender.title == self.config["start"]:
                self.timer.count = 0
                self.timer.end = self.interval
            sender.title = self.config["pause"]
            self.timer.start()
        else:
            sender.title = self.config["continue"]
            self.timer.stop()

    def stop_timer(self, sender):
        self.set_up_menu()
        self.stop_button.set_callback(None)
        self.start_pause_button.title = self.config["start"]

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = CoffeeApp()
    app.run()
