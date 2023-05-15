from typing import NamedTuple, Union, List, Tuple
from graphviz import Source

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

def dot_expr(expr: Expr) -> str:
    def dot_expr_helper(expr: Expr, node_num: int) -> Tuple[str, int]:
        if isinstance(expr, Value):
            node_label = str(expr.val)
            return f'n{node_num} [label="{node_label}" shape=circle]', node_num + 1
        elif isinstance(expr, Add):
            left_label, left_node_num = dot_expr_helper(expr.left, node_num + 1)
            right_label, right_node_num = dot_expr_helper(expr.right, left_node_num)
            node_label = '+'
            node_code = f'n{node_num} [label="{node_label}" shape=circle]\n{left_label}\n{right_label}\nn{node_num} -> n{left_node_num}\nn{node_num} -> n{right_node_num}'
            return node_code, right_node_num
        elif isinstance(expr, Subtract):
            left_label, left_node_num = dot_expr_helper(expr.left, node_num + 1)
            right_label, right_node_num = dot_expr_helper(expr.right, left_node_num)
            node_label = '-'
            node_code = f'n{node_num} [label="{node_label}" shape=circle]\n{left_label}\n{right_label}\nn{node_num} -> n{left_node_num}\nn{node_num} -> n{right_node_num}'
            return node_code, right_node_num
        elif isinstance(expr, Multiply):
            left_label, left_node_num = dot_expr_helper(expr.left, node_num + 1)
            right_label, right_node_num = dot_expr_helper(expr.right, left_node_num)
            node_label = '*'
            node_code = f'n{node_num} [label="{node_label}" shape=circle]\n{left_label}\n{right_label}\nn{node_num} -> n{left_node_num}\nn{node_num} -> n{right_node_num}'
            return node_code, right_node_num
        elif isinstance(expr, Divide):
            left_label, left_node_num = dot_expr_helper(expr.left, node_num + 1)
            right_label, right_node_num = dot_expr_helper(expr.right, left_node_num)
            node_label = '/'
            node_code = f'n{node_num} [label="{node_label}" shape=circle]\n{left_label}\n{right_label}\nn{node_num} -> n{left_node_num}\nn{node_num} -> n{right_node_num}'
            return node_code, right_node_num
        else:
            return None
    dot_code, _ = dot_expr_helper(expr, 0)
    return f"digraph G {{\n{dot_code}}}"



if __name__ == "__main__":
    expr = Add(Value(7), Multiply(Value(3), Value(2)))
    dot_code = dot_expr(expr)
    source = Source(dot_code)
    source.render('expr.gv', view=True)


