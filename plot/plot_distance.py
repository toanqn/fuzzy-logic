from matplotlib import pyplot as plt
import numpy as np


# distance dependency
# distance dependency
def distance_near_dependency(distance):
    dependency = 0.0
    if 0 <= distance <= 70:
        dependency = 1.0
    if 70 < distance < 140:
        dependency = (140 - distance) / 70.0
    return 0.0 if dependency < 0 else dependency


def distance_medium_dependency(distance):
    dependency = 0.0
    if 70 <= distance < 130:
        dependency = (distance - 70) / 60.0
    if 130 <= distance <= 150:
        dependency = 1.0
    if 150 < distance <= 210:
        dependency = (210 - distance) / 60.0
    return 0.0 if dependency < 0 else dependency


def distance_far_dependency(distance):
    dependency = 0.0
    if 140 <= distance <= 210:
        dependency = (distance - 140) / 70.0
    if distance >= 210:
        dependency = 1.0
    return 0.0 if dependency < 0 else dependency


# evenly sampled time at 200ms intervals
distance_range = np.arange(0., 280., 0.2)

near = [distance_near_dependency(tmp) for tmp in distance_range]
medium = [distance_medium_dependency(tmp) for tmp in distance_range]
far = [distance_far_dependency(tmp) for tmp in distance_range]

# red dashes, blue squares and green triangles

plt.xlabel("Khoảng cách (pixel)")
plt.ylabel("Độ thuộc")

plt.title("Hàm thuộc khoảng cách")

plt.text(40, 1.0, "near")
plt.text(120, 1.0, "medium")
plt.text(230, 1.0, "far")

plt.plot(distance_range, near, distance_range, medium, distance_range, far)
plt.show()

x = 200
print(distance_near_dependency(x), distance_medium_dependency(x), distance_far_dependency(x))
