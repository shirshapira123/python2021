def one():
    print("I love learning Python")
    print('I love learning Python')
    print("I love \n learning Python")
    print("I love", "learning Python")
    print()
    print(100)
    print(100 * 100)
    print(100 + 100)
    print(100 - 100)
    print(100 / 100)
    print(3.14159)
    print("I love", 17)
    print("3x3=", 3 * 3)
    print("January ", end='')


def two():
    a = 25
    b = 5
    print(pow(a+b, 2))
    a = 23
    c = 2
    d = 3
    print((d*(c+a))/b)


def three():
    print("I love Python" * 100)


def four():
    a = 4
    print(f"{a}, {a+1}, {a+2}, {a+3}, {a+4}")


def five():
    type(17)
    type(-9.998)
    type("Hi gal")
    type(True)
    type([1, 3, 5, 7, 9])
    type((1, 3, 5, 7, 9))
    type({1, 3, 5, 7, 9})
    type({"gal": 100, "tal": 100})


def six():
    a = int(input("enter num"))
    print(f"{a}, {a+1}, {a+2}, {a+3}, {a+4}")


def seven():
    money = [int(input("how many coins of 10 shekels: ")), int(input("how many coins of 2 shekels: ")), int(input("how many coins of 1 shekels: ")), int(input("how many coins of 0.5 shekels: ")), int(input("how many coins of 0.10 shekels: "))]
    moneysum = money[0]*10, money[1]*2, money[2]*1, money[3]*0.5, money[4]*0.1
    print(moneysum)


def eight():
    price = int(input("price of the console: "))
    price = price*3.45862
    price = price*0.97
    price = price+25*3.45862
    price = price*1.17
    print(price)


def nine():
    a = int(input("first number: "))
    d = int(input("difference: "))
    x = int(input("place of the number: "))
    print(a+(x-1)*d)


def ten():
    noc = int(input("Enter the number of children: "))
    under3 = 0
    more3 = 0
    for i in range(noc):
        age = int(input("Enter the age of child: "))
        if age > 3:
            more3 += 1
        else:
            under3 += 1
    if under3 % 6 == 0:
        print(under3 / 6)
    else:
        print(under3 // 6 + 1)
    if more3 % 10 == 0:
        print(more3 / 10)
    else:
        print(more3 // 10 + 1)


def eleven():
    number = input("number: ")
    check = 0
    for i in range(len(number)):
        if number[i] != number[len(number)-i-1]:
            check += 1
    if check == 0:
        print("the number is palindrom")
    else:
        print("the number is not palindrom")


def twelve():
    orders = int(input("how many orders: "))
    pricePerOrder = int(input("price per order: "))
    prize = False
    if orders < 300:
        price = orders * pricePerOrder
    elif (orders >= 300) and (orders < 400):
        price = 0.9 * pricePerOrder * orders
    else:
        price = 0.9 * pricePerOrder * orders
        prize = True
    print(price)
    if prize:
        print("you entitled to get a prize")
    else:
        print("you don't entitled to get a prize")


def thirteen():
    age = int(input("age: "))
    money = int(input("how much money in the card: "))
    add = int(input("how much money do you want to push: "))
    if (add >= 30) and (add <= 300):
        if age <= 18:
            add = add*2
        else:
            add = add*1.1
        print(money + add)
    else:
        print("you can push between 30 till' 300.")


if __name__ == '__main__':
    thirteen()
