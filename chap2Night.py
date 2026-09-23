def main():
    #demo1()
    #demo2()
    #demo3()
    #demo4()
    #demo5()
    #demo6()
    #demo7()
    demo8()

def demo8():
    INTEREST_RATE = .0825
    MAX_SIZE = 100
    



def demo7():
    print("Rebbe said 'Go Learn Torah' " )
    print("Rebbe said \"Go Learn Torah\" ")
    print('Don\'t do that')
    print("Backslash is a \\")
    print("AVOS\t\tIMAHOS")
    print("Avraham\t\tSara")
    print("Yitzchak\tRivka")
    print("Yaakov\t\tRachel Leah")
    num1 = 10
    num2 = 3
    print(f"{num1} / {num2} = {(num1 / num2):.2f}")
    print(f"{num1} / {num2} = {(num1 / num2):.4f}")
    num3 = 123456789.9876
    print(f"{num3} formatted is {num3:,.2f}")
    amount = 5678.567
    print(f"Amouunt to pay ${amount:,.2f}")
    f1 = 123.456
    f2 = 12.345
    f3 = 1234.678
    print(f"{f1:10,.2f}")
    print(f"{f2:10,.2f}")
    print(f"{f3:10,.2f}")
    name1 = "Yankel"
    name2 = "Avi"
    name3 = "Fischele"
    print(f"Hello {name1:10}. Nice to meet you.")
    print(f"Hello {name2:10}. Nice to meet you.")
    print(f"Hello {name3:10}. Nice to meet you.")
    print("------------")
    print(f"Hello {name1:>10}. Nice to meet you.")
    print(f"Hello {name2:>10}. Nice to meet you.")
    print(f"Hello {name3:>10}. Nice to meet you.")
    print("----------")
    print(f"Hello {name1:^10}. Nice to meet you.")
    print(f"Hello {name2:^10}. Nice to meet you.")
    print(f"Hello {name3:^10}. Nice to meet you.")
    print(f"**** {num1:<10}*****")
    print(f"**** {num2:<10}*****")
    discount = .2
    print(f"discount is {discount:.0%}")
    discount = .255
    print(f"discount is {discount:.1%}")
    num = 12345678
    print(f"number is {num:15,}")

def demo6():
    total_seconds = int(input("Enter total number of seconds: "))
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60 #OR (total seconds // 60) % 60
    seconds = total_seconds % 60
    print(f"{total_seconds} second equals\n Hours = {hours}\n Minutes = {minutes}\n Seconds = {seconds}")
    print("Totals: Hours = " + str(hours) + " Minutes = " + str(minutes) + " Second = " + str(seconds))
    my_str = 'one' 'two' 'three'
    print(my_str)


def demo5():
    price = float(input("Enter price of item: "))
    discount = .2
    total_price = price - price * discount
    print(f"Total price = {total_price}")



def demo4():
    num1 = 10
    num2 = 6
    print(f"num1 + num2 = {num1 + num2}")
    print(f"num1 - num2 = {num1 - num2}")
    print(f"num1 * num2 = {num1 * num2}")
    print(f"num1 / num2 = {num1 / num2}")
    print(f"num1 // num2 = {num1 // num2}")
    print(f"num1 % num2 = {num1 % num2}")
    print(f"num1 ** num2 = {num1 ** num2}")

def demo3():
    name = input("What is your name? ")
    print("Hello", name)
    age = int(input("How old are you? "))
    print("You are so big, in 5 years you will be", age + 5)
    print("A " + "B")
    print("A " + str(age))


def demo2():
    num = 5
    print("num = ")
    print(num)
    print("num =", num, "okay?")
    dollars = 5.67
    print("Cost is $", dollars, sep="")
    print("Avraham", "Yitzchak", "Yaakov", sep=" **** ")
    print("A", "B", end=" ^^^^ ")
    print("C", "D")
    print("The result is", end= " ")
    result = 90
    print(result)
    #integer, string, float
    print(type(50))
    print(type(3.14))
    print(type("Torah"))




def demo1():
    #examples of prints
    print("hello, world, don't worry")
    print('hello, world, don\'t worry')
    print('''hello, world''')
    num = 10
    print("num is", num)
    num, num2 = 15, 20
    #num = "Yankel"
    pay_rate = 55.50
    interest_rate = .0825




main()