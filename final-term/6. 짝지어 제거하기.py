def solution(s):
    stack = []
    for i in s:
        if stack == []:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    return int(stack==[])