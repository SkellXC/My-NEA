from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window 
"""
                          $$\                     $$\       $$\                                                $$\                     
                          $$ |                    \__|      $$ |                                               \__|                    
 $$$$$$\  $$$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\  $$\  $$$$$$$ |      $$\    $$\  $$$$$$\   $$$$$$\   $$$$$$$\ $$\  $$$$$$\  $$$$$$$\  
 \____$$\ $$  __$$\ $$  __$$ |$$  __$$\ $$  __$$\ $$ |$$  __$$ |      \$$\  $$  |$$  __$$\ $$  __$$\ $$  _____|$$ |$$  __$$\ $$  __$$\ 
 $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ |  \__|$$ /  $$ |$$ |$$ /  $$ |       \$$\$$  / $$$$$$$$ |$$ |  \__|\$$$$$$\  $$ |$$ /  $$ |$$ |  $$ |
$$  __$$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |$$ |  $$ |        \$$$  /  $$   ____|$$ |       \____$$\ $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ |      \$$$$$$  |$$ |\$$$$$$$ |         \$  /   \$$$$$$$\ $$ |      $$$$$$$  |$$ |\$$$$$$  |$$ |  $$ |
 \_______|\__|  \__| \_______|\__|       \______/ \__| \_______|          \_/     \_______|\__|      \_______/ \__| \______/ \__|  \__|
                                                                                                                                       
                                                                                                                                       
android version of the project
moved onto a windows version                                                                                                                               
"""
class BackgroundWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Convert the hex #252525 to RGBA (37/255 = 0.145)
            Color(37/255, 37/255, 37/255, 1)
             # Puts a rectangle with this colour on top of the widget
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Sets the rectangle size to the size of the widget
        self.bind(size=self.updateRect, pos=self.updateRect)

    def updateRect(self, *args):
        # Updates the rectangle size 
        self.rect.size = self.size
        self.rect.pos = self.pos

class WorkoutTrackerApp(App):
    def build(self):
        Window.size = (400, 620)


        root = FloatLayout()
        background = BackgroundWidget(size_hint=(1,1))
        root.add_widget(background)
        # Creates the background widget and adds it to the root widget

        top_bar = BoxLayout(size_hint=(1, 1), height=50)
        # Size hint allows for dynamic resizing of the widget. 10% in this case
        top_bar.pos = (0,550)

        with top_bar.canvas:
            # Set the colour
            Color(28/255, 28/255, 28/255, 1)
            self.topBar = Rectangle(size=top_bar.size, pos=top_bar.pos)
            # Set the initial position
        
        top_bar.bind(size=self.updateBar, pos=self.updateBar)
        # Allows the top bar to be resized and repositioned automatically
        root.add_widget(top_bar)
        

        # Creates the window itself as an object and adds it to the layout
        return root
    

    def updateBar(self, instance, *args):
        self.topBar.size = instance.size
        self.topBar.pos = instance.pos


if __name__ == '__main__':
    WorkoutTrackerApp().run()
