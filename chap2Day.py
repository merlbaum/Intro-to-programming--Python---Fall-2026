def main():
    #demo1()
    #demo2()
    #demo3()
    #demo4()
    #demo5()
    #demo6()
    #demo7()
    demo8()
"""
This is a paragraph
comment
"""

def demo8():
    INTEREST_RATE = .0012
    deposit = 200
    print(f"Interest earned = {INTEREST_RATE * deposit}")

def demo7():
    amount_due = 5000.55
    monthly_payment = amount_due / 12
    print(f"Monthly Payment = {monthly_payment:.2f}")
    pi = 3.1415926535
    print(f"Pi = {pi:.3f}")
    num = 123456789.9876
    print(f"The number formatted is {num:,}")
    print(f"The number formatted is {num:,.2f}")
    discount = .2
    print(f"The discount is {discount:.0%}")
    num1 = 98123.45
    num2 = 12.345
    num3 = 6.7
    num4 = 7.89
    print(f"The number is ${num1:10,.2f}")
    print(f"The number is ${num2:10,.2f}")
    print(f"The number is ${num3:10,.2f}")
    print(f"The number is ${num4:10,.2f}")
    print("----------")
    name = "Yankel"
    print(f"Hello {name:10}. How are you?")
    print(f"Hello {name:>10}. How are you?")
    print(f"The number is ${num4:<10,.2f}. How is it?")
    print(f"Hello {name:^10}. How are you?")
    num1 = 10
    num2 = 6
    print(f"Adding {num1}" + f" and " + f"{num2} equals {num1 + num2}")

def demo6():
    result = 1 + 2 * 6 - 1 \
    + 8 * 3
    print("Monday = ", 2, "Tuesday = ", 3,
          "Wednesday = ", 4)
    print('Rebbe said "Go to the Bais" ')
    print("Rebbe said 'Go to the Bais' ")
    print('Rebb\\e said \'Go to the Bais\' ')
    print("Avos\t\tImahos")
    print("Avraham\t\tSarah")
    print("Yitz\t\tRivkah")
    print("Yaakov\t\tRachel Leah")



def demo5():
    test1 = float(input("Enter exam#1: "))
    test2 = float(input("Enter exam#2: "))
    test3 = float(input("Enter exam#3: "))
    average = test1 + test2 + test3 / 3
    print(f"Average is {average}")
    random_num = 7
    print(random_num % 2)
    random_num = 18
    print(random_num % 2)

    total_seconds = int(input("Enter number of seconds: "))
    hours = total_seconds // 3600
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60
    print(f"That many seconds equals:")
    print(f"Hours = {hours}")
    print(f"Minutes = {minutes}")
    print(f"Seconds = {seconds}")



def demo4():
    num1 = 10
    num2 = 6
    print(f"Adding {num1} and {num2} equals {num1 + num2}")
    print(f"Subtracting {num2} from {num1} equals {num1 - num2}")
    print(f"Multiplying {num1} and {num2} equals {num1 * num2}")
    print(f"Dividing {num2} into {num1} equals {num1 / num2}")
    print(f"Dividing {num2} into {num1} equals {num1 // num2}")
    print(f"____________ {num2} into {num1} equals {num1 % num2}")
    print(f"____________ {num1} and {num2} equals {num1 ** num2}")
    price = float(input("What is the the price of the item? "))
    tax = float(input("What is the tax on the item?"))
    price = price + (price * tax)
    print(f"Your total cost is {price}")


def demo3():
    name = input("What is your name: ")
    print(f"Hello {name}")
    age = input("How old are you? ")
    #age = int(age)
    print(f"Wow, you are so big! In 5 years you will be {int(age) + 5}")
    num = 5
    print("hello, world " + str(num))
    dollars = 10.67
    print(f"Dollars = {float(dollars)}")

#variables
def demo2():
    """
    This is a multiple
    line comment
    """
    num1 = 5
    num2 = 10
    print(f"num1 = {num1}, num2 = {num2}")
    num1 = 15
    print(num1, num2)
    print(f"num1 = {num1}, num2 = {num2}")
    first_name = "Yankel"
    last_name = "Jones"
    print(first_name, last_name)

#print function examples
def demo1():
    print("hello, world")
    num = 5
    print(num)
    print("hello, world", num)
    #print("hello, world" + num)
    print("hello," + "world")
    dollars = 10.00
    print(f"${dollars}")
    print("$", dollars, sep="")
    print("Avraham" "Yitzchak", "Yaakov", sep="^^^")
    print("Avraham", "Yitzchak", "Yaakov", sep="\n")
    print("--------")
    print("Avraham", end=" * ")
    print("Yitzchak", end=" * ")
    print("Yaakov")

main()