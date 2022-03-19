def solution(arr):
    temp = arr[0]
    counter = 0
    final = 0
    for i in arr:
        if i == temp:
            counter +=1
        else:
            if counter > final:
                final = counter
            counter = 1
            temp = i
    return final
