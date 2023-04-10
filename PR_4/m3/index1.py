class Num:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def eval(self):
        return self.value

    def compile(self):
        return f'PUSH {self.value}'


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f'({str(self.left)} + {str(self.right)})'

    def eval(self):
        return self.left.eval() + self.right.eval()

    def compile(self):
        return f'{self.left.compile()} {self.right.compile()} ADD'


class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f'({str(self.left)} * {str(self.right)})'

    def eval(self):
        return self.left.eval() * self.right.eval()

    def compile(self):
        return f'{self.left.compile()} {self.right.compile()} MUL'

if __name__ == "__main__":
    ast = Add(Num(7), Mul(Num(3), Num(2)))

    print(ast)

    result = ast.eval()
    print(result)

    compiled = ast.compile()
    print(compiled)
