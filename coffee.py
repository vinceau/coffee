import rumps

class CoffeeApp(object):
    def __init__(self):
        self.app = rumps.App("Coffee", "☕️")

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = CoffeeApp()
    app.run()

