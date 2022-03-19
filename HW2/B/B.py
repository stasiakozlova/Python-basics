def solution(x):
    new_line = ''
    for i in range(len(x)):
        if (x[i] == 'h') and (i != x.find('h')) and (i != x.rfind('h')):
            x = x[:i] + 'H' + x[i+1:]
        if (i % 3 != 0) or (i == 0):
            new_line = new_line + x[i]
    new_line = new_line.replace('1', 'one')
    return new_line