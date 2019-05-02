# reference from python programming tutorial

from kivy.app import App # in tutorial kivy was mentioned


from kivy.uix.label import Label

print("import completed !")

class SimpleKivy(App):
    def build(self):
        return Label(text="Hello Kivy!")


if __name__ == "__main__" :
    SimpleKivy().run()
