import time

import pyautogui as pag


class Status:
    def __init__(self):
        self.list = ["to_play", "in_queue", "to_accept", "loading", "in_game", "to_exit"]
        self.link = {}  # link between button names and status list
        self.counter = 0

    def forward(self):
        if self.list[self.counter] == "to_exit":
            self.counter = 0
        else:
            self.counter += 1

    def backward(self):
        if self.list[self.counter] == "to_accept":
            self.counter -= 1
        else:
            print("Warning! illegal to go backward here!")

    def check(self):
        flag = None
        while not flag:
            for item in ["a", "b", "c"]:
                flag = pag.locateOnScreen(item+".png")
                if flag:
                    self.counter = self.list.index(self.link[item])  # find corresponding counter of the found button
                    break
            time.sleep(5)


if __name__ == "__main__":
    pag.locateOnScreen('test.png')
