def isValid(s):
    stack = []
    if len(s) % 2 == 1:
        return(False)
    for l in s:
        if l == '(' or l == '{' or l == '[':
            stack.append(l)
        elif l == ')':
            if len(stack) == 0:
                return(False)
            elif stack.pop() == '(':
                continue
            else:
                return(False)
        elif l == '}':
            if len(stack) == 0:
                return(False)
            elif stack.pop() == '{':
                continue
            else:
                return(False)
        elif l == ']':
            if len(stack) == 0:
                return(False)
            elif stack.pop() == '[':
                continue
            else:
                return(False)  
    if len(stack) == 0:
        return(True)
    else:
        return(False)   

s = "(]"
poop = isValid(s)  
print(poop)