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
    sum = 0
    for number in args:
        sum += number
    return sum


def main():
    a = 4
    b = 7
    calculator = Calculator(a, b)
    print(str(a) + '+' + str(b) + ' =', calculator.sum())
    print(str(a) + '-' + str(b) + ' =', calculator.sub())
    print(str(a) + '*' + str(b) + ' =', calculator.mul())
    print(str(a) + '/' + str(b) + ' =', calculator.div())


if __name__ == '__main__':
    main()
