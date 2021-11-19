OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}

def infix_to_postfix(formula):
    stack = []
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:#operator
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack: 
    	output += stack.pop()
    # print('POSTFIX: {output}')
    print(output)

def infix_to_prefix(formula):
    Stack = []
    Output = []
    for ch in formula:
        if not ch in OPERATORS:
            Output.append(ch)
        elif ch == '(':
            Stack.append(ch)
        elif ch == ')':
            while Stack[-1] != '(':
                op = Stack.pop()
                a = Output.pop()
                b = Output.pop()
                Output.append( op+b+a )
            Stack.pop()
        else:
            while Stack and Stack[-1] != '(' and PRI[ch] <= PRI[Stack[-1]]:
                op = Stack.pop()
                a = Output.pop()
                b = Output.pop()
                Output.append( op+b+a )
            Stack.append(ch)

    while Stack:
        op = Stack.pop()
        a = Output.pop()
        b = Output.pop()
        Output.append( op+b+a )
    # print(f'PREFIX: {Output[-1]}')
    print(Output[-1])

expres = input("INPUT THE EXPRESSION: ")
pre = infix_to_prefix(expres)
pos = infix_to_postfix(expres)