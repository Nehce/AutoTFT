import pyautogui as pag
import time


class Button:
    def __init__(self, name):
        self.name = name
        self.location = None  # should be center of the Button box
        self.box = None

    def find_location(self):
        if not self.location:
            self.location = pag.locateCenterOnScreen(f'img/{self.name}.png', confidence=0.9)
            if self.location:
                print(f"{self.name} has been found!")
            else:
                print(f"Warning! {self. name} can't be found")

    def convert_location(self):
        self.location = self.location/2

    def click(self):
        if self.location:
            pag.mouseDown(*self.location, duration=0.2)
            pag.mouseUp(*self.location, duration=0.2)


if __name__ == "__main__":
    time.sleep(3)
    test_button = Button('test')
    test_button.find_location()
    test_button.click()
