from heapq import merge

def solution(a, b):
    difference = []
    for i in b:
        if i not in a:
            difference.append(i)
    result = list(merge(a, difference))
    return result