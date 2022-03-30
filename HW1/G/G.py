def solution(a, b):
    for i in b:
        if i not in a:
            a.append(i)
    a.sort()
    return a
