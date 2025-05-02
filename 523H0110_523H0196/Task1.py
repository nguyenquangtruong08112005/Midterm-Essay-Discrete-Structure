def Infix2Postfix(infix):
    """
    Convert a logical expression from infix to postfix (RPN) notation.
    Input: infix string with variables A-Z and operators ~(NOT), &(AND), |(OR), >(IMPLIES), =(IFF).
    Output: postfix string.
    """
    # Define operator precedence (higher number = higher precedence)
    prec = {'~': 5, '&': 4, '|': 3, '>': 2, '=': 1}
    # '~' (NOT) is right-associative; all other operators are left-associative
    right_assoc = {'~'}
    output = []         # list for output tokens
    stack = []          # stack for operators
    
    # Scan each character in the infix expression
    for token in infix:
        if token.isalpha():  
            # Operand (A-Z) -> add directly to output
            output.append(token)
        elif token == '(':
            # Left parenthesis -> push on stack
            stack.append(token)
        elif token == ')':
            # Right parenthesis -> pop until matching '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Discard the '('
        else:
            # Operator encountered
            # Pop higher-precedence operators from stack to output
            # If equal precedence and token is left-associative, also pop
            while stack and stack[-1] != '(':
                top = stack[-1]
                # Compare precedence of top of stack vs current token
                if (prec.get(top, 0) > prec.get(token, 0) or
                    (prec.get(top, 0) == prec.get(token, 0) and token not in right_assoc)):
                    output.append(stack.pop())
                else:
                    break
            # Push the current operator onto stack
            stack.append(token)
    
    # Pop any remaining operators from stack to output
    while stack:
        output.append(stack.pop())
    
    # Return the joined postfix string
    return ''.join(output)

import itertools

def Postfix2Truthtable(postfix):
    """
    Given a postfix logical expression, print its truth table.
    Input: postfix string with variables A-Z and operators ~(NOT), &(AND), |(OR), >(IMPLIES), =(IFF).
    Output: prints table of variable assignments and result.
    """
    # Extract unique variables and sort them for consistent ordering
    variables = sorted({ch for ch in postfix if ch.isalpha()})
    num_vars = len(variables)
    
    # Print header: variable names and the expression
    header = variables + [postfix]  # table columns
    print(' | '.join(header))
    print('-' * (4 * len(header) - 3))  # simple separator line
    
    # Generate all combinations of truth values 
    for values in itertools.product([True, False], repeat=num_vars):
        # Map variable to its truth value in this combination
        env = dict(zip(variables, values))
        
        # Evaluate the postfix expression using a stack
        stack = []
        for token in postfix:
            if token.isalpha():
                # Push the truth value of the variable
                stack.append(env[token])
            else:
                if token == '~':
                    # Unary NOT
                    val = stack.pop()
                    stack.append(not val)
                else:
                    # Binary operators: pop two values (right operand popped first)
                    right = stack.pop()
                    left = stack.pop()
                    if token == '&':
                        stack.append(left and right)
                    elif token == '|':
                        stack.append(left or right)
                    elif token == '>':
                        # Implication: True unless (left is True and right is False)
                        stack.append((not left) or right)
                    elif token == '=':
                        # Biconditional (iff): True if both have same truth value
                        stack.append(left == right)
        
        # The final stack value is the result
        result = stack.pop()
        
        # Print the row: variable values and result (True/False)
        row = [str(v) for v in values] + [str(result)]
        print(' | '.join(row))

testcases = [
        "R|(P&Q)",
        "~P|(Q&R)>R",
        "P|(R&Q)",
        "(P>Q)&(Q>R)",
        "(P|~Q)>~P=(P|(~Q))>~P"
    ]

for expr in testcases:
    print(f"\nInfix: {expr}")
    postfix = Infix2Postfix(expr)
    print(f"Postfix: {postfix}")
    Postfix2Truthtable(postfix)