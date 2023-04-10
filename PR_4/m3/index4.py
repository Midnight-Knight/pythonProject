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

class StackVisitor:
    def visit(self, node):
        if isinstance(node, NumNode):
            return f"PUSH {node.value}"
        elif isinstance(node, AddNode):
            return "ADD"
        elif isinstance(node, MulNode):
            return "MUL"
        else:
            return ""

class NumNode:
    def __init__(self, value):
        self.value = value

class AddNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class MulNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right


if __name__ == "__main__":
    num_node1 = NumNode(7)
    num_node2 = NumNode(3)
    num_node3 = NumNode(2)
    add_node = AddNode(num_node1, MulNode(num_node2, num_node3))

    sv = StackVisitor()

    print(sv.visit(add_node))

