
def main():
    #demo1()
    #demo2()
    #demo3()
    #demo4()
    demo5()

def demo5():
    for num in range(5):
        print(num, end= " ")
    print("\n---------")
    for num in range(5):
        print(num, end= " ")
    print("\n---------")
    for num in range(1, 6):
        print(num, end= " ")
    print("\n----------")
    for num in range(10, 21):
        print(num, end= " ")

    print("\n----------")
    for num in range(10, 21, 2):
        print(num, end=" ")


def demo4():
    for num in [1, 2, 3, 4, 5]:
        print(num, end = ", ")
    print("\n--------")
    for num in [1, 3, 5, 7, 9]:
        print(num, end = ", ")
    print()
    for name in ["Avraham", "Yitzchak", "Yaakov"]:
        print(name)

    print("-----------")
    for random_stuff in [1, 5, "Avi", False, 1.9]:
        print(random_stuff)

def demo3():
    num = 5
    while num > 0:
        print("Have a great Yom Tov!", num)
        num -= 1  # num = num - 1
    print("-------")
    num = 0
    while num < 5:
        print("Have a great Yom Tov!", num)
        num += 1  # num = num + 1

    num = 0
    while num < 10: num += 1
    print(num)

    num = 0
    while num < 10: print(num := num + 1)

def demo1():
    #while loop

    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':
        sales = float(input("Enter amount of sales: "))
        comm_rate = float(input("Enter commission rate: "))
        commission = sales * comm_rate
        print(f"Your commssion is ${commission:,.2f}")

        keep_going = input("Do you wish to calculate another (y/n)? ")



def demo2():
    MAX_TEMP = 102.5

    temp = float(input("Enter the temperature: "))
    while temp > MAX_TEMP:
        print("Temperature is too high.")
        print("Turn the thermostat down and wait 5 minutes.")
        temp = float(input("Enter the new temperature: "))

    print("The temerature is now acceptable.")
    print("Check again in 15 minutes.")


main()
