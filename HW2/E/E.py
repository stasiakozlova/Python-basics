def solution(a, b):
    if a == 0:
        return b
    else:
        a -= 1
        b += 1
    return solution(a, b)