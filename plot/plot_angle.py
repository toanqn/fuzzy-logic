from matplotlib import pyplot as plt
import numpy as np


# angle dependency
def angle_small_dependency(angle):
    dependency = 0.0
    if 0 <= angle <= 7:
        dependency = 1.0
    if 7 <= angle <= 14:
        dependency = (14 - angle) / 7.0
    if dependency < 0:
        return 0
    else:
        return dependency


def angle_medium_dependency(angle):
    dependency = 0.0
    if 7 <= angle < 12:
        dependency = (angle - 7) / 5.0
    if 12 <= angle <= 16:
        dependency = 1.0
    if 16 < angle <= 21:
        dependency = (21 - angle) / 5.0
    if dependency < 0:
        return 0
    else:
        return dependency


def angle_big_dependency(angle):
    dependency = 0.0
    if angle >= 21:
        dependency = 1.0
    if 14 <= angle <= 21:
        dependency = (angle - 14) / 7.0
    if dependency < 0:
        return 0
    else:
        return dependency


angle_range = np.arange(0., 28., 0.1)


small = [angle_small_dependency(tmp) for tmp in angle_range]
medium = [angle_medium_dependency(tmp) for tmp in angle_range]
big = [angle_big_dependency(tmp) for tmp in angle_range]

# red dashes, blue squares and green triangles

plt.xlabel("Góc(độ)")
plt.ylabel("Độ phụ thuộc")

plt.title("Hàm thuộc của góc")

plt.text(3, 1.0, "small")
plt.text(12, 1.0, "medium")
plt.text(22, 1.0, "big")
plt.plot(angle_range, small, angle_range, medium, angle_range, big)
plt.show()

x = 10
print(angle_small_dependency(x), angle_medium_dependency(x), angle_big_dependency(x))
