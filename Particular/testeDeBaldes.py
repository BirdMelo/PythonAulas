from threading import Thread
from time import sleep

bucket = 38


def producting(var):
    while var != 0:
        sleep(10)
        var += 38
        print(var)


Thread(target=producting(bucket)).start()


def consuming(var):
    while var != 0:
        sleep(6)
        var -= 16
        print(var)


consuming(bucket)
