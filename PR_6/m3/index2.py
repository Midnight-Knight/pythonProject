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

def calc_expr(expr: Expr) -> float:
    if isinstance(expr, Value):
        return expr.val
    elif isinstance(expr, Add):
        return calc_expr(expr.left) + calc_expr(expr.right)
    elif isinstance(expr, Subtract):
        return calc_expr(expr.left) - calc_expr(expr.right)
    elif isinstance(expr, Multiply):
        return calc_expr(expr.left) * calc_expr(expr.right)
    elif isinstance(expr, Divide):
        return calc_expr(expr.left) / calc_expr(expr.right)

if __name__ == "__main__":
    expr = Add(Value(1), Multiply(Value(2), Divide(Value(4), Value(2))))
    result = calc_expr(expr)
    print(result)
