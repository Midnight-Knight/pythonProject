from typing import NamedTuple, Union, List, Tuple

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

def stack_expr(expr: Expr) -> List[Tuple[str, float]]:
    stack = []
    if isinstance(expr, Value):
        stack.append(("value", expr.val))
    elif isinstance(expr, Add):
        stack_expr(expr.left)
        stack_expr(expr.right)
        stack.append(("add", 0))
    elif isinstance(expr, Subtract):
        stack_expr(expr.left)
        stack_expr(expr.right)
        stack.append(("subtract", 0))
    elif isinstance(expr, Multiply):
        stack_expr(expr.left)
        stack_expr(expr.right)
        stack.append(("multiply", 0))
    elif isinstance(expr, Divide):
        stack_expr(expr.left)
        stack_expr(expr.right)
        stack.append(("divide", 0))
    return stack

if __name__ == "__main__":
    expr = Add(Value(1), Multiply(Value(2), Divide(Value(4), Value(2))))
    result = stack_expr(expr)
    print(result)

