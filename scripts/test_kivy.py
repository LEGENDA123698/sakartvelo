from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import requests


class My_App(App):
    def connect(self):
        requests.get("http://127.0.0.1:8000/menu/api/dishes/")
        request = requests.get("http://127.0.0.1:8000/menu/api/dishes/")
        if request.status_code == 200:
            dishes = request.json()
            for dish in dishes:
                box_l2 = BoxLayout(orientation = "vertical")
                label = Label(text = dish["title"])
                img = Image(source = dish["photo"])
                
                box_l2.add_widget(label)
                box_l2.add_widget(img)
                
                app.root.children[0].add_widget(box_l2)
            

    
    def build(self):
        btn = Button(text = 'btn-1')
        box_l = BoxLayout()
        grid_l = GridLayout(cols = 2)
        
        btn.on_press = self.connect
        box_l.add_widget(btn)
        box_l.add_widget(grid_l)
        return box_l
    
app = My_App()


app.run()