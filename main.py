class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


class Circle:
    pi = 3.1415

    def __init__(self, diameter):
        self.diameter = diameter

    def radius(self):
        return self.diameter / 2

    def line_length(self):
        return self.pi * self.diameter

    def square(self):
        return self.pi * self.radius() * self.radius()


def array_sum(args):
    try:
        summa = 0
        for number in args:
            summa += number
        return summa
    except TypeError:
        print("If array contains string, func return 0")
        return 0


def main():
    a = 4
    b = 7
    diameter = 5
    array = [3, 4, 9]
    print(array)
    circle = Circle(diameter)
    calculator = Calculator(a, b)
    print(str(a) + '+' + str(b) + ' =', calculator.sum())
    print(str(a) + '-' + str(b) + ' =', calculator.sub())
    print(str(a) + '*' + str(b) + ' =', calculator.mul())
    print(str(a) + '/' + str(b) + ' =', calculator.div())
    print("Sum of array :" + str(array) + " = " + str(array_sum(array)))
    print("Operations with circle:")
    print("Diameter = " + str(diameter) + " -> line length = " + str(circle.line_length()))
    print("\t\t\t\t\t radius = " + str(circle.radius()))
    print("\t\t\t\t\t square = " + str(circle.square()))


if __name__ == '__main__':
    main()
