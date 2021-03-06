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
        #  please pay attention to the order of the following list, it matters!!
        #  the first one checked will break the for loop, so items in the front of the list has higher priority.

        for item in ["find_match", "accept", "in_queue", "exit", "play_again", "in_game"]:
            flag = pag.locateOnScreen(f"img/{item}.png", confidence=0.9)
            if flag:
                self.status = item  # find corresponding counter of the found button
                print(f"Status checked! ----{item}----")
                break
        if flag is None:
            print('nothing was found!')


if __name__ == "__main__":
    time.sleep(2)
    s = Status()
    s.check()
    print(s.status)
