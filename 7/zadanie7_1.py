import numpy as np
import matplotlib.pyplot as plt
import threading

BARS_COUNT = 30
bar_high = np.zeros(30)
bar_centre = []
width = 0

def hist(data):
    for x in range(0, BARS_COUNT):
        for i in data:
            if (width * (x + 1) + min(r_arr)) > i > (width * x + min(r_arr)):
                bar_high[x] = bar_high[x] + 1


r_arr = np.random.randn(1000) * 20 + 100

plt.figure(2)
plt.grid(True)

width = (max(r_arr) - min(r_arr)) / BARS_COUNT
thread1 = threading.Thread(target=hist(r_arr[0:250]))
thread2 = threading.Thread(target=hist(r_arr[250:500]))
thread3 = threading.Thread(target=hist(r_arr[500:750]))
thread4 = threading.Thread(target=hist(r_arr[750:1000]))

for x in range(0, BARS_COUNT):
    bar_centre.append(width * x + width / 2 + min(r_arr))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

plt.bar(bar_centre, bar_high, width=width)
plt.show()
