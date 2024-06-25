import re

def calculator(expression: str) -> float:
    """ Evaluates a mathematical expression. """
    
    # Reform the expression.
    expression = expression.replace(' ', '')    # Remove spaces.
    expression = expression.replace('^', '**')  # Replace ^ with **.
    
    # Check if the expression is valid.
    if not re.match(r'^[\d\+\-\*\/\(\)\.]+$', expression):
        return "Error: Invalid expression."
    
    # Evaluate the expression.
    try:
        result = eval(expression
            .replace('sin', 'math.sin')
            .replace('cos', 'math.cos')
            .replace('tan', 'math.tan')
            .replace('sqrt', 'math.sqrt')
            .replace('log', 'math.log')
            .replace('pi', 'math.pi')
            .replace('e', 'math.e'))
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def run(dir, expression: str) -> str:
    """ Evaluates a mathematical expression. """
    return calculator(expression)