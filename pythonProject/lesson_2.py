def one():
    for i in range(100, 0, -1):
        print(i)
    for i in range(1, 199, 2):
        print(i)
    for i in range(0, 1000, 10):
        print(i)
    x = int(input("enter number: "))
    y = int(input("enter number: "))
    for i in range(x, y, 1):
        print(i)


def two():
    firstnum = int(input("enter the first number of the sequence: "))
    d = int(input("enter the distance of the sequence: "))
    for i in range(10):
        print(firstnum+d*i)


def three():
    x = int(input("enter number: "))
    max1 = x
    min1 = x
    while x > 0:
        x = int(input("enter number: "))
        max1 = max(x, max1)
        min1 = min(x, min1)
    print(max1)
    print(min1)


def four():
    basketwork = int(input("basketwork: "))
    height = float(input("height: "))
    counter = 0
    while basketwork > 0:
        if basketwork > 6 and height > 1.5:
            counter += 1
        basketwork = int(input("basketwork: "))
        height = float(input("height: "))
    print(counter)


def five():
    name = input("name: ")
    vote = int(input("vote: (1 for Hagai 2 for Hadas)"))
    hagai = 0
    hadas = 0
    while name != 'SOF':
        if vote == 1:
            hagai += 1
        else:
            hadas += 1
        name = input("name: ")
        vote = int(input("vote: (1 for Hagai 2 for Hadas)"))
    print(f'hagai got {hagai} votes')
    print(f'hadas got {hadas} votes')


def six():
    name = input("name: ")
    grade = int(input("grade: "))
    counter = 0
    while name != "FINISH":
        if grade > 95:
            counter += 1
        print("name: ", name)
        print("grade: ", grade)
        name = input("name: ")
        grade = int(input("grade: "))
    print(counter)


def seven():
    import random
    counter_ninety = 0
    counter_ten = 0
    for i in range(100):
        rnd = random.randint(1, 100)
        print(rnd)
        if rnd > 90:
            counter_ninety += 1
        elif rnd < 10:
            counter_ten += 1
    print(counter_ten, " numbers are under ten")
    print(counter_ninety, " numbers are above ninety")


def eight():
    x = int(input("enter x: "))
    print(pow(x, 3)-107*x**2-9*x+3)


def nine():
    for i in range(1, 3, 1):
        xi = int(input(f"enter x{i}"))
        #        אני לא יודע איך לחשב את התרגיל הזה גם על דף עם עט


def ten():
    import turtle
    tw = turtle.Screen()
    t = turtle.Turtle()
    for i in range(10):
        t.forward(100)
        t.right(36)
    turtle.mainloop()


if __name__ == '__main__':
    six()
