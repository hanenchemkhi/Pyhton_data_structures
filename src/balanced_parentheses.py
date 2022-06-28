from src.stack_list import Stack
"""
    Check equation for balanced parentheses

    Args:
       equation(linked list): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
"""

def equation_checker(equation):
    paren = []
    while  equation.peek()!= None :
        popped = equation.pop()
        if popped == ")":
            paren.append(popped)
        elif popped == "(":
            if (len(paren) > 0) :
                paren.pop()
            else:
                return False
            
        continue
    if len(paren) == 0 :
        return True
    else :
        return False 
equation = Stack()
equation.push("(")
equation.push("(")
equation.push("Z")
equation.push("+")
equation.push("T")
equation.push(")")
equation.push(")")
print(equation_checker(equation))