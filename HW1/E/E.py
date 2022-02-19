def solution(x1, y1, x2, y2):
    if abs(x2 - x1) <= 1:
        if abs(y2 - y1) <= 1:
            print('True')
        else:
            print('False')
    return