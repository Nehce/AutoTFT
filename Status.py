import time

import pyautogui as pag


class Status:
    def __init__(self):
        self.list = ["find_match", "in_queue", "accept", "loading", "in_game", "exit"]
        self.link = {}  # link between button names and status list
        self.counter = 0
        self.status = "find_match"

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
            for item in ["find_match", "in_queue", "accept", "in_game", "exit", "play_again"]:
                flag = pag.locateOnScreen(item+".png")
                if flag:
                    self.status = item  # find corresponding counter of the found button
                    print(f"Status checked! ----{item}----")
                    break


if __name__ == "__main__":
    pag.locateOnScreen('test.png')
