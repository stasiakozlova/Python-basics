def solution(x1, y1, x2, y2):
    flag = False
    if abs(x2 - x1) <= 1:
        if abs(y2 - y1) <= 1:
            flag is True
    return flag
