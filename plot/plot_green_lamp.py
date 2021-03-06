from matplotlib import pyplot as plt
import numpy as np


def lamp_red_dependency(time):
    if time >= 6:
        return 1.0
    if 3 <= time <= 6:
        return (time - 3) / 3.0
    return 0.0


def lamp_less_red_dependency(time):
    if time <= 3:
        return 1.0
    if 3 <= time <= 6:
        return (6 - time) / 3.0
    return 0.0


time_range = np.arange(0., 15., 0.1)

less_red = [lamp_less_red_dependency(tmp) for tmp in time_range]
red = [lamp_red_dependency(tmp) for tmp in time_range]

# red dashes, blue squares and green triangles

plt.xlabel("Thời gian đèn xanh còn lại (s)")
plt.ylabel("Độ thuộc")

plt.title("Hàm thuộc đèn xanh")

plt.text(0.5, 1.0, "less green")
plt.text(9, 1.0, "green")

plt.plot(time_range, less_red, time_range, red)
plt.show()
