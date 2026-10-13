
def main():
    #demo1()
    #demo2()
    #demo3()
    #demo4()
    #demo5()
    #squares()
    #demo6()
    #demo7()
    #demo8()
    #demo9()
    #demo10()
    #demo11()
    #demo12()
    #demo13()
    demo14()

def demo14():
    for row in range(5):
        for col in range(4):
            print("*", end=" ")
        print()

    for row in range(10):
        for col in range(10 - row):
            print("*", end=" ")
        print()

    for row in range(1, 11):
        for col in range(row):
            print("*", end=" ")
        print()

    star = "*"
    for row in range(1, 11):
        for col in range(row):
            print(f"{star:^10}", end=" ")
        print()

    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{(i * j):3}", end=" ")
        print()


def demo13():
    num_students = int(input("How many students do you have? "))
    num_test_scores = int(input("How many exams do you have? "))
    for student in range(num_students):
        total = 0.0
        print(f"Student #{student + 1}")
        print("------------")
        for test_num in range(num_test_scores):
            score = int(input(f" Exam #{test_num + 1}: "))
            total += score
        average = total / num_test_scores
        print(f'The average for student #{student + 1} is {average:.1f} ')


def demo12():
    for hours in range(24):
        for minutes in range(60):
            for seconds in range(60):
                print(f"{hours:2d}:{minutes:2d}:{seconds:2d}")

def demo11():
    while (score := int(input('Enter score: '))) < 0:
        print("A score cannot be negative!!")

def demo10():
    hours = int(input("How many hours were logged this week? "))
    while hours > 50:
        hours = int(input("Error! How many hours were logged this week? "))

    salary_rate = int(input("What is the pay rate? "))
    salary = hours * salary_rate
    print(f"The salary is ${salary:,.2f}")

def demo9():
    exam = int(input("Enter an exam grade (50-100): "))
    while not(exam >= 50 and exam <=100):
    #while exam < 50 or exam > 100:
        print("ERROR: Exam must be between 50 and 100")
        exam = int(input("Enter an exam grade (50-100: "))

    print(f"Exam score is {exam}")

def demo8():
    total = 0
    total_amount_of_values = 0
    num = int(input(f"Enter number #{total_amount_of_values + 1}: "))
    while num != "STOP":
        total_amount_of_values += 1
        total += num
        num = input(f"Enter number #{total_amount_of_values + 1} (\"STOP\" when done): ")
        if num != "STOP":
            num = int(num)

    print(f"The sum of your numbers is {total}.")
    if total_amount_of_values != 0:
        print(f"The average of your numbers is {total / total_amount_of_values}.")
    else:
        print("No numbers - no average!!")


def demo7():
    total = 0
    total_amount_of_values = 0
    SENTINAL = -999
    num = int(input(f"Enter number #{total_amount_of_values + 1}: "))
    while num != SENTINAL:
        total_amount_of_values += 1
        total += num
        num = int(input(f"Enter number #{total_amount_of_values + 1} (-999 to stop): "))

    print(f"The sum of your numbers is {total}.")
    if total_amount_of_values != 0:
        print(f"The average of your numbers is {total / total_amount_of_values}.")
    else:
        print("No numbers - no average!!")

def demo6():
    numbers_to_enter = int(input("How many values to you want to sum and average: "))
    total = 0
    for i in range(numbers_to_enter):
        num = int(input(f"Enter a number #{i + 1}: "))
        total += num
    print(f"The sum of your numbers is {total}.")
    print(f"The average of your numbers is {total / numbers_to_enter}.")

def squares():
    start = int(input("What number would you like to start from: "))
    end = int(input("What number would you like to end: "))
    print('Number\tSquare')
    print("-------------------")
    for num in range(start, end):
        square = num ** 2
        print(f"{num}\t\t{square}")




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
    print("\n----------")
    for num in range(10, 0, -1):
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
