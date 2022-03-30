def solution(n):
    x = 1
    results = []
    while x <= n:
        results.append(x)
        x *= 2    
    return results

print(solution(1025))
