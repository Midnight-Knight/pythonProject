from typing import NamedTuple, Union, List

class Value(NamedTuple):
    val: float

class Add(NamedTuple):
    left: 'Expr'
    right: 'Expr'

class Subtract(NamedTuple):
    left: 'Expr'
    right: 'Expr'

class Multiply(NamedTuple):
    left: 'Expr'
    right: 'Expr'

class Divide(NamedTuple):
    left: 'Expr'
    right: 'Expr'

Expr = Union[Value, Add, Subtract, Multiply, Divide]

class ExprVisitor:
    def visit(self, expr: Expr) -> float:
        return expr.visit(self)

class ValueVisitor(ExprVisitor):
    def visit(self, expr: Value) -> float:
        return expr.val

class AddVisitor(ExprVisitor):
    def visit(self, expr: Add) -> float:
        return expr.left.visit(self) + expr.right.visit(self)

class SubtractVisitor(ExprVisitor):
    def visit(self, expr: Subtract) -> float:
        return expr.left.visit(self) - expr.right.visit(self)

class MultiplyVisitor(ExprVisitor):
    def visit(self, expr: Multiply) -> float:
        return expr.left.visit(self) * expr.right.visit(self)

class DivideVisitor(ExprVisitor):
    def visit(self, expr: Divide) -> float:
        return expr.left.visit(self) / expr.right.visit(self)

def print_expr(expr: Expr) -> None:
    if isinstance(expr, Value):
        print(expr.val, end="")
    elif isinstance(expr, Add):
        print("(", end="")
        print_expr(expr.left)
        print("+", end="")
        print_expr(expr.right)
        print(")", end="")
    elif isinstance(expr, Subtract):
        print("(", end="")
        print_expr(expr.left)
        print("-", end="")
        print_expr(expr.right)
        print(")", end="")
    elif isinstance(expr, Multiply):
        print("(", end="")
        print_expr(expr.left)
        print("*", end="")
        print_expr(expr.right)
        print(")", end="")
    elif isinstance(expr, Divide):
        print("(", end="")
        print_expr(expr.left)
        print("/", end="")
        print_expr(expr.right)
        print(")", end="")

if __name__ == "__main__":
    expr = Multiply(Add(Value(1), Value(2)), Divide(Value(4), Value(2)))
    print_expr(expr)
    print()

    value_visitor = ValueVisitor()
    print(expr.visit(value_visitor))

    add_visitor = AddVisitor()
    print(expr.visit(add_visitor))

    subtract_visitor = SubtractVisitor()
    print(expr.visit(subtract_visitor))

    multiply_visitor = MultiplyVisitor()
    print(expr.visit(multiply_visitor))

    divide_visitor = DivideVisitor()
    print(expr.visit(divide_visitor))