from math import cos, pi, sin
import matplotlib.pyplot as plt
import numpy as np


# АППРОКСИМАЦІЯ ДВОХ ФУНКЦІЙ:
def approximate_point_first(x):
    res = -4  # a0/2
    for n in range(1, 8, 2):
        res += (40 / ((pi * n) ** 2)) * cos(pi * n * x / 2)
    return res


def approximate_point_second(x):
    res = (pi + 4) / 4  # a0/2
    for n in range(1, 100):
        res += ((-1) ** n / n) * sin(n * x) + (((-1)**n - 1)/(pi * (n**2))) * cos(n * x)
    return res


my_x = []
for i in [i for i in range(4000)]:
    my_x.append(i / 400)
    my_x.append(-i / 400)


my_y = [approximate_point_second(x) for x in my_x]

plt.scatter(my_x, my_y, label="stars", color="green",
            marker="*", s=2)
plt.show()

#############################################################
# ДРУГИЙ ГРАФІК
x = np.arange(-10, 10, 0.05)

new_array = []
for i in x:
    new_array.append(approximate_point_first(i))


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

plt.plot(x, new_array)
plt.show()
