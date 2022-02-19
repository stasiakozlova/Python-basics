def solution(total):
    total = total % 3600
    hours = total // 60
    minutes = total % 60
    if minutes < 10:
        minutes = '0' + str(minutes)
    print(f'{hours} {minutes}')
    return