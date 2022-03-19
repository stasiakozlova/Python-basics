def solution(arr):
    new_list = []
    while arr:
        new_list = new_list + list(arr.pop(0))
        arr = list(zip(*arr))
        arr.reverse()
    return new_list