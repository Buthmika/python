import sys
import ast

# back/back.py
# Simple sum / summation calculator
# Usage:
#  - python back.py 1 2 3    -> sums the numbers 1+2+3
#  - python back.py          -> interactive mode: choose list-sum or sigma


# Safe expression checker (allows only arithmetic with variable `i`)
class SafeExpr(ast.NodeVisitor):
    ALLOWED_NODES = {
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant,
        ast.Name, ast.Load,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow,
        ast.UAdd, ast.USub, ast.Subscript, ast.Index, ast.Call  # Call/Subscript/Index kept out by checks below
    }

    def visit(self, node):
        if type(node) not in self.ALLOWED_NODES:
            raise ValueError(f"Disallowed expression element: {type(node).__name__}")
        super().visit(node)

    def visit_Name(self, node):
        if node.id != "i":
            raise ValueError(f"Only variable 'i' is allowed, not '{node.id}'")

    def visit_Call(self, node):
        # disallow function calls for safety
        raise ValueError("Function calls are not allowed in expressions")

    def visit_Subscript(self, node):
        raise ValueError("Subscript is not allowed in expressions")

def eval_expr(expr, i):
    """
    Safely evaluate arithmetic expression using variable i.
    Allowed: + - * / // % ** and numeric literals, parentheses.
    """
    tree = ast.parse(expr, mode="eval")
    SafeExpr().visit(tree)
    code = compile(tree, "<expr>", "eval")
    return eval(code, {}, {"i": i})

def sum_list(nums):
    return sum(nums)

def sigma(expr, start, end):
    step = 1 if start <= end else -1
    total = 0
    for k in range(start, end + step, step):
        total += eval_expr(expr, k)
    return total

def interactive():
    print("Sum / Summation calculator")
    mode = input("Choose mode - (1) sum numbers, (2) summation Σ: ").strip()
    if mode == "1":
        s = input("Enter numbers separated by spaces: ").strip()
        nums = [float(x) for x in s.split()] if s else []
        print("Result:", sum_list(nums))
    elif mode == "2":
        expr = input("Enter expression in i (e.g. i**2 + 1): ").strip()
        start = int(input("Start (integer): ").strip())
        end = int(input("End (integer): ").strip())
        print("Result:", sigma(expr, start, end))
    else:
        print("Unknown mode")

def main(argv):
    if len(argv) > 1:
        # treat all args as numbers to sum
        try:
            nums = [float(x) for x in argv[1:]]
        except ValueError:
            print("Invalid number in arguments.")
            return
        print(sum_list(nums))
    else:
        interactive()

if __name__ == "__main__":
    main(sys.argv)