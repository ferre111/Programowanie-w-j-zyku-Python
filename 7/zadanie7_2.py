import threading
from time import sleep
from random import randint

PHILO_COUNT = 5
DEADLOCK_FLAG = 1


class Philosopher(threading.Thread):

    def __init__(self, l_fork, r_fork, name):
        threading.Thread.__init__(self)
        self.l_fork = l_fork
        self.r_fork = r_fork
        self.name = name

    def run(self):
        self.think()

        if DEADLOCK_FLAG:
            sleep(randint(1, 10) / 10)
        else:
            sleep(1)

        self.eat()
        print(self.name, 'end')

    def think(self):
        print(self.name, 'think')

    def eat(self):
        print(self.name, "start eating")
        self.l_fork.acquire()
        self.r_fork.acquire()

        if DEADLOCK_FLAG:
            sleep(randint(1, 10) / 10)
        else:
            sleep(1)

        self.l_fork.release()
        self.r_fork.release()
        print(self.name, "stop eating")


forks = [threading.Lock() for i in range(PHILO_COUNT)]
philo = [Philosopher(forks[i], forks[(i + 1) % PHILO_COUNT], "philosophers" + str(i)) for i in range(PHILO_COUNT)]

for p in philo:
    p.start()
