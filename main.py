from Button import Button
from Status import Status
import time

# def get_the_location():
#     buttons = ['find_match', 'accept', 'exit', 'play_again']


button_find_match = Button('find_match')
button_accept = Button('accept')
button_in_queue = Button('in_queue')
button_in_game = Button('in_game')
button_exit = Button('exit')
button_play_again = Button('play_again')

status = Status()


def find_match():
    # step1. find match
    if button_find_match.location is None:
        button_find_match.find_location()
    button_find_match.click()
    print("finding match!")


def accept():
    # step2. accept
    while not button_accept.location:
        button_accept.find_location()
    if button_accept.location:
        button_accept.click()
    print("accepted!")


def quit_match():
    while not button_exit.location:
        button_exit.find_location()
    if button_exit.location:
        button_exit.click()


def play_again():
    while not button_play_again.location:
        button_play_again.find_location()
    if button_play_again.location:
        button_play_again.click()


def play_game():
    status.check()
    while status.status is None:
        status.check()

    if status.status == "in_queue":
        time.sleep(1)
        print("in queue... waiting to accept...")

    if status.status == "accept":
        accept()
        time.sleep(20)

    if status.status == "find_match":
        play_game()

    if status.status == "in_game":
        print("success!")


def exit_game():
    while True:
        status.check()
        print(f'ready to exit... Status now:{status.status}')
        if status.status == "exit":
            quit_match()
            break
        elif status.status == "play_again":
            play_again()
            break
        elif status.status is None or status.status == "in_game":
            print("game does not end yet")
            time.sleep(30)

        else:
            raise RuntimeError('something was wrong in the progress')


ss = r'''
    _       _      _____ ___ _____ _ 
   /_\ _  _| |_ __|_   _| __|_   _| |
  / _ \ || |  _/ _ \| | | _|  | | |_|
 /_/ \_\_,_|\__\___/|_| |_|   |_| (_)
                                     
'''

i = 1
print(ss)
while True:
    print(f"----------------------{i}st--game---------")
    time.sleep(2)

    find_match()

    while status.status != "in_game":
        play_game()

    print("sleeping...")
    time.sleep(900)
    exit_game()
