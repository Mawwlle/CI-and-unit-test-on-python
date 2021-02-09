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
    array = [3, 4, "3"]
    print(array)
    calculator = Calculator(a, b)
    print(str(a) + '+' + str(b) + ' =', calculator.sum())
    print(str(a) + '-' + str(b) + ' =', calculator.sub())
    print(str(a) + '*' + str(b) + ' =', calculator.mul())
    print(str(a) + '/' + str(b) + ' =', calculator.div())
    print("Sum of array :" + str(array) + " = " + str(array_sum(array)))


if __name__ == '__main__':
    main()
