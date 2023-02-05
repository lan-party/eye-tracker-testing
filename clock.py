from datetime import datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from KivyOnTop import register_topmost



class MyApp(App):
    def update_time(self, nap):
        self.root.ids.time.text = datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]
    def on_start(self):
        Window.set_title("Clock")
        register_topmost(Window, "Clock")
        Config.set('graphics', 'resizable', '0')
        Window.size = (200,50)
        Window.top = 850
        Window.left = 1400
        Clock.schedule_interval(self.update_time, 0)
        
if __name__ == '__main__':
    MyApp().run()
