class ComplexNumber:
    def __init__(self, comp_num):
        self.comp_num = comp_num
        for i in comp_num:
            if i == '-' or i == '+':
                self.real_number = int(comp_num.split(i)[0])
                self.imaginary_number = comp_num.split(i)[-1]
                if i == '-':
                    self.imaginary_number = -int(self.imaginary_number[:len(self.imaginary_number) - 1:])
                else:
                    self.imaginary_number = int(self.imaginary_number[:len(self.imaginary_number) - 1:])
                return
        self.real_number = 0
        self.imaginary_number = int(comp_num[:len(self.comp_num) - 1:])

    def __add__(self, other):
        real_part = self.real_number + other.real_number
        imaginary_part = self.imaginary_number + other.imaginary_number
        if imaginary_part >= 0:
            return f'{real_part}+{imaginary_part}j'
        else:
            return f'{real_part}{imaginary_part}j'

    def __mul__(self, other):
        real_part = (self.real_number * other.real_number - self.imaginary_number * other.imaginary_number)
        imaginary_part = (self.imaginary_number * other.real_number + self.real_number * other.imaginary_number)
        if imaginary_part >= 0:
            return f'{real_part}+{imaginary_part}j'
        else:
            return f'{real_part}{imaginary_part}j'


a = ComplexNumber('0+3j')
print(a.real_number)
b = ComplexNumber('4-7j')
print(b.imaginary_number)
c = ComplexNumber(a + b)
print(c.comp_num)
x = (5+3j) * (4-7j)  # для контроля
print(x)
print(a * b)
