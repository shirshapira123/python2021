import math
import random


def two():
    import random
    lst = []
    for _ in range(100):
        lst.append(random.randint(1, 1000))
    sum = 0
    print(lst)
    max1 = lst[0]
    min1 = lst[0]
    for i in lst:
        max1 = max(i, max1)
        min1 = min(i, min1)
        sum += i
    print("sum = ", sum)
    print("max = ", max1)
    print("min = ", min1)


def three():
    lst1 = [12, 14, 19, 7, 55, 97, 32, 47]
    lst2 = [13, 17, 19, 2, 85, 54, 72, 27]
    counter = 0
    for i in lst1:
        for k in lst2:
            if i == k:
                counter += 1
    if counter == 0:
        print("no")
    else:
        print("yes")


def four():
    board = []
    for i in range(1, 11):
        lines = []
        for k in range(1, 11):
            lines.append(i*k)
        board.append(lines)
    print(" ", board[0])
    for i in board:
        print(i[0], i)


def five():
    names = []
    name = input("enter name: ")
    names_counter = 0
    while name != 'exit':
        names.append(name)
        names_counter += 1
        name = input("enter name: ")
    print(names_counter)


def six():
    female = []
    name = input("enter name: ")
    sex_type = input("enter your sex type:")
    female_counter = 0
    while name != 'exit':
        if sex_type == 'F':
            female.append(name)
            female_counter += 1
        name = input("enter name: ")
        sex_type = input("enter your sex type:")
    print(female_counter)


def seven():
    x_lst = []
    y_lst = []
    for i in range(-100, 100):
        num = i/10
        x_lst.append(num)
        y_lst.append(0.5*num+2.5)
    print(x_lst)
    print(y_lst)


def eight():
    x_randoms = []
    y_randoms = []
    min_distance = math.sqrt(101**2+102**2)
    point = 0
    for i in range(10):
        x_randoms.append(random.randint(1, 101))
        y_randoms.append(random.randint(1, 101))
        print(f"({x_randoms[i]},{y_randoms[i]})")
        distance = math.sqrt(x_randoms[i]**2 + y_randoms[i]**2)
        min_distance = min(min_distance, distance)
        if distance == min_distance:
            point = i
    print(f"({x_randoms[point]},{y_randoms[point]}), distance = {min_distance}")


def nine():
    x_randoms = []
    y_randoms = []
    z_randoms = []
    min_distance = math.sqrt((101-50)**2+(101-50)**2+(102-50)**2)
    point = 0
    for i in range(10):
        x_randoms.append(random.randint(1, 101))
        y_randoms.append(random.randint(1, 101))
        z_randoms.append(random.randint(1, 101))
        print(f"({x_randoms[i]},{y_randoms[i]},{z_randoms[i]})")
        distance = math.sqrt((x_randoms[i]-50)**2+(y_randoms[i]-50)**2+(z_randoms[i]-50)**2)
        min_distance = min(min_distance, distance)
        if distance == min_distance:
            point = i
    print(f"({x_randoms[point]},{y_randoms[point]},{z_randoms[point]}), distance = {min_distance}")


if __name__ == '__main__':
    nine()
