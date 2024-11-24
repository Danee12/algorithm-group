# https://school.programmers.co.kr/learn/courses/30/lessons/12909


s = "(()("


# true

def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(")")
        elif i == ")":
            if len(stack) == 0:
                return False
            elif stack[0] == ")":
                stack.pop()
        else:
            return False
    if len(stack) != 0:
        return False
    return True


print(solution(s))
