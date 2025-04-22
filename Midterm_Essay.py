#Task 1
def Infix2Postfix(infix):
    precedence = {'~': 4, '&': 3, '|': 2, '>': 1, '=': 0}
    right_associative = {'~', '>', '='}
    output = []
    stack = []

    for token in infix:
        if token.isalpha():  # Operand
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '('
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   ((token not in right_associative and precedence[token] <= precedence[stack[-1]]) or
                    (token in right_associative and precedence[token] < precedence[stack[-1]]))):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

def eval_postfix(postfix, values):
    stack = []
    for token in postfix:
        if token.isalpha():
            stack.append(values[token])
        elif token == '~':
            val = stack.pop()
            stack.append(not val)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '&':
                stack.append(a and b)
            elif token == '|':
                stack.append(a or b)
            elif token == '>':
                stack.append((not a) or b)
            elif token == '=':
                stack.append(a == b)
    return stack[0]

import itertools

def Postfix2Truthtable(postfix):
    variables = sorted(set(filter(str.isalpha, postfix)))
    print(" | ".join(variables + [postfix]))
    print("-" * (4 * len(variables) + len(postfix)))

    for combo in itertools.product([False, True], repeat=len(variables)):
        values = dict(zip(variables, combo))
        result = eval_postfix(postfix, values)
        line = ' | '.join(['T' if values[v] else 'F' for v in variables])
        print(f"{line} | {'T' if result else 'F'}")

test_cases = [
    "R|(P&Q)",
    "~P|(Q&R)>R",
    "P|(R&Q)",
    "(P>Q)&(Q>R)",
    "(P|~Q)>~P=(P|(~Q))>~P"
]

for expr in test_cases:
    print(f"\nInfix: {expr}")
    postfix = Infix2Postfix(expr)
    print(f"Postfix: {postfix}")
    Postfix2Truthtable(postfix)
