import module_test1

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