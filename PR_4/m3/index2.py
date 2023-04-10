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

class PrintVisitor:
    def visit(self, node):
        method_name = f"visit_{node.__class__.__name__}"
        method = getattr(self, method_name, self.default_visit)
        return method(node)

    def default_visit(self, node):
        raise NotImplementedError(f"No visit method found for {node.__class__.__name__}")

    def visit_Num(self, node):
        return str(node.value)

    def visit_Add(self, node):
        return f'({self.visit(node.left)} + {self.visit(node.right)})'

    def visit_Mul(self, node):
        return f'({self.visit(node.left)} * {self.visit(node.right)})'

if __name__ == "__main__":
    pv = PrintVisitor()
    ast = Add(Num(7), Mul(Num(3), Num(2)))

    print(pv.visit(ast))