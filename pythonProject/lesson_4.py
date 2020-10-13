import matplotlib.pyplot as plt


def two():
    lst1 = []
    lst2 = []
    for i in range(-10, 11):
        lst1.append(i)
        lst2.append(i*i)
    plt.plot(lst1, lst2)
    plt.grid()
    #  plt.axis(-5, 5, 0, 10)
    plt.show()


if __name__ == '__main__':
    two()
