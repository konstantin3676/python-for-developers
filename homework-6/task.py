from fastapi import FastAPI, HTTPException
import re
import ast
import operator

app = FastAPI()

_current_expression = ""

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def safe_eval(expr: str):
    expr = re.sub(r'\s+', '', expr)
    
    if not re.match(r'^[0-9+\-*/().]+$', expr):
        raise ValueError("Invalid characters in expression")

    try:
        node = ast.parse(expr, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid syntax")

    def eval_node(node):
        if isinstance(node, ast.Expression):
            return eval_node(node.body)
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            op_type = type(node.op)
            if op_type == ast.Add:
                return left + right
            elif op_type == ast.Sub:
                return left - right
            elif op_type == ast.Mult:
                return left * right
            elif op_type == ast.Div:
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                return left / right
            else:
                raise ValueError("Unsupported operator")
        elif isinstance(node, ast.UnaryOp):
            operand = eval_node(node.operand)
            if isinstance(node.op, ast.USub):
                return -operand
            elif isinstance(node.op, ast.UAdd):
                return +operand
            else:
                raise ValueError("Unsupported unary operator")
        else:
            raise ValueError("Unsupported expression")

    return eval_node(node.body)


@app.post("/calculate/{a}/{op}/{b}")
def simple_operation(a: float, op: str, b: float):
    if op not in OPS:
        raise HTTPException(status_code=400, detail=f"Unsupported operation: {op}")
    if op == '/' and b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    result = OPS[op](a, b)
    return {"expression": f"{a} {op} {b}", "result": result}


@app.post("/expression/set")
def set_expression(expr: str):
    global _current_expression
    try:
        safe_eval(expr)
    except (ValueError, ZeroDivisionError, SyntaxError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid expression: {str(e)}")
    _current_expression = expr
    return {"status": "Expression set", "expression": _current_expression}


@app.get("/expression/get")
def get_expression():
    return {"expression": _current_expression}


@app.post("/expression/evaluate")
def evaluate_expression():
    global _current_expression
    if not _current_expression:
        raise HTTPException(status_code=400, detail="No expression set")
    try:
        result = safe_eval(_current_expression)
        return {"expression": _current_expression, "result": result}
    except (ValueError, ZeroDivisionError, SyntaxError) as e:
        raise HTTPException(status_code=400, detail=f"Evaluation error: {str(e)}")


@app.post("/calculate/complex")
def complex_calculation(expr: str):
    try:
        result = safe_eval(expr)
        return {"expression": expr, "result": result}
    except (ValueError, ZeroDivisionError, SyntaxError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid expression: {str(e)}")