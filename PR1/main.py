def one():
    print("1 import antigravity")
    print("2 import __hello__")
    print("3 from __future__ import braces")
    print("4 assert 1 < 2 или assert 1 > 2")

def two():
    print("42")
    print(42)
    print(int(bin(42)[2:],2))
    print(int(oct(42)[2:],8))
    print(int(hex(42)[2:],16))
    print(chr(52)+chr(50))
    print(21<<1)
    print(84>>1)
    print(~-0b101011)
    print(0b101010 & 0b111111)
    print(0b000000 | 0b101010)
    print(0b100011 ^ 0b001001)

def three():
    print("размер ограничен ОЗУ")
    print("только дробная часть")
    print(" -1.79E308 до 1.79E308, а точность представления составляет около 15-17 цифр после запятой.")

def four():
    return 1, 2

def five():
    a = 10
    while a >= 0.1:
        a -= 0.1
        print(a)

def six():
    z = 1
    z <<= 40
    print(z)
    a = 2 ** z
    print(a)

def seven():
    i = 0
    while i < 10:
        print(i)
        i += 1

def eight():
    print((True * 2 + False) * -True)

def nine():
    x = 5
    print(1 < x < 10) # здесь сравнивается переменная x ,в данном случае будет True
    x = 5
    print(1 < (x < 10)) # здесь сначала в порядке приоритета (из-за скобок) проверяется выражение (x < 10)
    # и получается значение True, а дальше идёт проверка выражения  (1 < True), а так как PY язык с
    # динамической типизацией данных, то True становится 1 и в таком случае результат выражения равен
    # False

if __name__ == '__main__':
    one()
    two()
    three()
    print(four())
    five()
    # six() <<= - это смещение в разрядной сетке с присваиванием значения к смещаемой переменной, если
    # мы сместим число 1 в 10сс (примерно в рс(2сс) = 000...0001) на 40 разрядов, то получится в
    # 10сс 1099511627776, а это очень большое число для возведения в степень
    seven() # в python операторы увеличения и уменьшения (как pre, так и post) в нем не разрешены.
    eight() # python это один из языков с динамической типизацией данных, поэтому при работе с
    # целочисленным значением , булевые значения конвентировались в целые(False в 0, True в 1)
    nine()
