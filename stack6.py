def func(tokens):
    stack = []
    operators = set(["+", "-", "*", "/"])
    
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
    
    return stack[0]

print(func(["2", "1", "+", "3", "*"]))  
print(func(["4", "13", "5", "/", "+"])) 
print(func(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  