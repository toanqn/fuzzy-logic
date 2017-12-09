from matplotlib import pyplot as plt
import numpy as np


# speed dependency
def speed_stop_dependency(speed):
    if speed == 0:
        return 1.0
    if 0 < speed < 0.1:
        return (0.1 - speed) / 0.1
    return 0.0


def speed_slow_dependency(speed):
    if 0 <= speed <= 0.5:
        return min(speed / 0.5, 0.4)
    if 0.5 <= speed <= 1:
        return min((1 - speed) / 0.5, 0.4)
    return 0.0


def speed_slower_dependency(speed):
    if 0.5 <= speed <= 1:
        return min((speed - 0.5) / 0.5, 0.6)
    if 1 <= speed <= 1.5:
        return min((1.5 - speed) / 0.5, 0.6)
    return 0


def speed_fast_dependency(speed):
    if speed >= 1.5:
        return 0.4
    if 1 <= speed <= 1.5:
        return min((speed - 1) / 0.5, 0.4)
    return 0.0


# evenly sampled time at 200ms intervals
speed1 = np.arange(0., 1.1, 0.1)
speed2 = np.arange(0.5, 1.6, 0.1)
speed3 = np.arange(1., 2., 0.1)

slow = [speed_slow_dependency(tmp) for tmp in speed1]
slower = [speed_slower_dependency(tmp) for tmp in speed2]
fast = [speed_fast_dependency(tmp) for tmp in speed3]

# red dashes, blue squares and green triangles

plt.xlabel("Speed")
plt.ylabel("Dependency")

plt.title("Defuzzification")

plt.text(0.4, 0.4, "slow")
plt.text(0.9, 0.6, "slower")
plt.text(1.5, 0.4, "fast")

plt.plot(speed1, slow, speed2, slower, speed3, fast)
plt.show()
