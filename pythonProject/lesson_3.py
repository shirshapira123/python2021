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


if __name__ == '__main__':
    four()
