import math

def area(radius):
    return math.pi * radius**2

def circumference(radius):
    return  2 * math.pi * radius

def test():
    print("Name = ", __name__)

test()

if __name__ == '__main__':
    test()
