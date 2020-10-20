import matplotlib.pyplot as plt
import numpy as np
import time as t


def two():
    x = np.linspace(-4, 4, 1000)
    y = x*x
    plt.plot(x, y)
    plt.show()


def three():
    t = np.linspace(0, 0.004, 1000)
    y1 = 5 + 5*np.sin(2*np.pi*500*t)
    y2 = 5*np.sin(2*np.pi*1000*t)
    plt.plot(t, y1)
    plt.plot(t, y2)
    plt.show()


def four():
    x = np.arange(-20, 20, 1)
    y1 = 10*x + 6
    y2 = 2*x*x + 2*x - 100
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()


def five():
    xl = list(range(1000000))
    xn = np.arange(1000000)
    startTimeList = t.time()
    for x in range(len(xl)):
        xl[x] = x*5
    endTimeList = t.time()
    listTime = endTimeList - startTimeList
    startTimeNumpy = t.time()
    xn = xn*5
    endTimeNumpy = t.time()
    numpyTime = endTimeNumpy - startTimeNumpy
    print("list: ", listTime, "  numpy:", numpyTime)


def six():
    x = np.ones((5, 5))
    print(x, "\n-----------")
    for i in range(5):
        for k in range(5):
            if i != 0 and i != 4 and k != 0 and k != 4:
                x[i][k] = 0
    print(x)


def seven():
    x1 = np.array([1, 2, 3, 4])
    x2 = np.array([1, 6, 3, 4, 10])
    x3 = np.array([])
    for i in range(0, len(x1)):
        for j in range(0, len(x2)):
            if x1[i] == x2[j]:
                x3 = np.append(x3, x1[i])
    print(x1)
    print(x2)
    print(x3)


def eight():
    x = np.array([
                    [
                        [1, 2],
                        [3, 4]
                    ],
                    [
                        [11, 3],
                        [12, 14]
                    ],
                    [
                        [21, 1],
                        [22, 24]
                    ]
                 ])
    print(x, "\n--------------")
    print(x*2, "\n--------------")
    print(x+10, "\n--------------")


def nine():
    x1 = np.array([[1], [2], [3], [4], [5], [6]])
    x2 = np.array([[7], [8], [9], [10], [11], [12]])
    x3 = np.array([[13], [14], [15], [16], [17], [18]])
    y = np.vstack((x1, x2, x3))
    print(y, "\n\n\n\n")
    print(np.hstack((x1, x2, x3)), "\n\n\n\n")
    y1 = np.hstack((x1[:3], x2[:3], x3[:3]))
    print(y1.reshape(3, 3), "\n\n\n\n")
    print(y.reshape(2, 3, 3))


def ten():
    data = np.zeros([100, 100, 3], dtype=np.uint8)

    data[:50, :50] = [255, 0, 0]
    data[50:, :50] = [0, 255, 0]
    data[:50, 50:] = [0, 0, 255]
    data[50:, 50:] = [255, 255, 255]
    plt.imshow(data, interpolation='nearest')
    plt.show()


if __name__ == '__main__':
    ten()
