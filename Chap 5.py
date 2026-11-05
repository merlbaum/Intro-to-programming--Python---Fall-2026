import math
import circle
import random


number = 10
SIZE = 5


def main():
    # demo1()
    # texas()
    # input("Press Enter to continue...")
    # california()
    # demo2()
    # demo3()
    # print(f"Hello {name}")
    # demo4()
    # demo5()
    # demo6()
    # print(number)
    # print(SIZE + 10)
    #demo7()
    #roll_dice(5)
    #coin_flip(4)
    #demo8()
    #demo9()
    #demo10()
    #demo11()
    demo12()

def demo12():
    num = int(input("Enter a number to square root: "))
    print(f"It's square root is {math.sqrt(num)}.")
    num = int(input("Enter radius of circle: "))
    print(f"{math.pi} :Area of circle with a radius of {num} equals {math.pi * num**2:.2f}.")
    print(f"Area of circle with a radius of {num} equals {circle.area(num):.2f}.")
    print(f"Circumference of circle with a radius of {num} equals {circle.circumference(num):2f}.")


def get_name2():
    first = input("What is your first name? ")
    last = input("What is your last name? ")
    return first, last

def swap(x, y):
    return y, x

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return None


def demo11():
    first_name, last_name = get_name2()
    print(f"Hello {first_name} {last_name}.")
    first_name, last_name = swap(first_name, last_name)
    print(f"Hello {first_name}, {last_name}.")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    #print(f"{num1} divided by {num2} is {divide(num1, num2)}.")
    quotient = divide(num1, num2)
    #num = int(quotient) + 5; None not valid for math
    print(f"num = {num}")
    if quotient is None:
        print("Cannot divide by zero!")
    else:
        print(f"{num1} divided by {num2} is {quotient}.")


def is_invalid(mod_num):
    # if mod_num != 100 and mod_num != 200 and mod_num != 300:
    #     return True
    # else:
    #     return False
    return mod_num != 100 and mod_num != 200 and mod_num != 300

def is_even(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
    return num % 2 == 0


def dollar_format(value):
    return f'{value:,.2f}'


def get_name():
    return input("What is your name? ")

def demo10():
    name = get_name()
    print(f"Hello {name}")
    val = float(input("Enter the item's original price: "))
    #val = dollar_format(val)
    #print(f"price is {val}")
    if is_even(int(val)):
        print("That price truncated is even.")
    else:
        print("That price truncated is odd.")

def get_price():
    price = float(input("Enter the item's original price: "))
    return price

def sum_up(n1, n2):
    #result = n1 + n2
    return n1 + n2

def demo9():
    num1 = int(input("Enter first number to sum up: "))
    num2 = int(input("Enter second number to sum up: "))
    print(f"The sum is {sum_up(num1, num2)}", end=" ")
    price = get_price()
    sale_price = price - price * .10
    print(f"Original price: {price:.2f}     Discount price: {sale_price:.2f}.")



def demo8():
    for i in range(5):
        num = random.randrange(5, 100, 5)
        print(num, end=" ")
    print("\n--------------")
    for i in range(5):
        num = random.random()
        print(num, end=" ")
    print("\n--------------")
    for i in range(5):
        num = random.uniform(1.0, 10.0)
        print(num, end=" ")
    print("\n--------------")
    random.seed(10)
    for i in range(5):
        num = random.randint(1, 20)
        print(num, end=" ")


def coin_flip(times):
    HEADS = 0
    TAILS = 1
    for i in range(times):
        if random.randint(HEADS, TAILS) == HEADS:
            print("HEADS")
        else:
            print("TAILS")


def roll_dice(times):
    for i in range(times):
        print(f"{random.randint(1, 6)} {random.randint(1, 6)}")

def demo7():
    for i in range(10):
        num = random.randint(1, 10)
        print(f"{num} {random.randint(1,10)}", end= " ")

def demo6():
    global number
    print(number)
    number = int(input("Enter a number: "))
    print(number)
    print(SIZE)


def display_stars(rows=1, cols=10):
    for r in range(rows):
        for c in range(cols):
            print("*", end="")
        print()


def show_tax(price, tax_rate=.07):
    tax = price * tax_rate
    print(f"The tax is {tax:.2f}")


# no good
# def show_tax2(price=10, tax_rate):
#     tax = price * tax_rate
#     print(f"The tax is {tax:.2f}")

def demo5():
    display_stars()
    print("--------")
    display_stars(2)
    print("--------")
    display_stars(4, 5)
    print("--------")
    display_stars(cols=3)
    show_interest(1000, .01, 10)
    show_interest(rate=.01, periods=10, principal=1000)
    show_interest(1000, periods=10, rate=.01)
    # show_interest(1000, periods=10, .01)
    # show_interest(principal=1000, periods=10, .01)
    # throws error
    # show_interest_2(rate=.01, periods=10, principal=1000)
    # this works
    show_interest_3(1000, periods=10, rate=.01)
    show_tax(100)
    show_tax(100, .08)


def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print(f"The simple interest will be ${interest:,.2f}.")


def show_interest_2(principal, rate, periods, /):
    interest = principal * rate * periods
    print(f"The simple interest will be ${interest:,.2f}.")


def show_interest_3(principal, /, rate, periods):
    interest = principal * rate * periods
    print(f"The simple interest will be ${interest:,.2f}.")


def change_me(value):
    value += 10
    print(f"In change_me, your number changed to {value}.")


def demo4():
    num = int(input("Enter a number to change: "))
    print(f"Your number is {num}.")
    change_me(num)
    print(f"After the call to change_me, your number is {num}.")


def show_sum(n1, n2):
    result = n1 + n2
    print(result)


def demo3():
    # print(name)
    # name = input("What is your name? ")
    # print(name)
    num1 = int(input("Enter first number to sum up: "))
    num2 = int(input("Enter second number to sum up: "))
    print("The sum is", end=" ")
    show_sum(num1, num2)


def demo2():
    pass
    num = 15
    if num <= 10:
        pass
    else:
        print("Over 10!")


# Definition of the texas function. It creates
# a local variable named birds.
def texas():
    birds = 5000
    print(f'texas has {birds} birds.')


# Definition of the california function. It also
# creates a local variable named birds.
def california():
    birds = 8000
    print(f'california has {birds} birds.')


def demo1():
    say_hello("Yankel")
    say_hello("Yossel")
    name = input("What is your name? ")
    say_hello(name)


def say_hello(person):
    print(f"Hello {person}, how are you?")


if __name__ == '__main__':
    main()