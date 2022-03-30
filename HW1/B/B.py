def solution(n):
    x1 = '   _~_   '
    x2 = '  (o o)  '
    x3 = ' /  V  \ '
    x4 = '/(  _  )\\'
    x5 = '  ^^ ^^  '
    line1 = (x1 * n)
    line2 = (x2 * n)
    line3 = (x3 * n)
    line4 = (x4 * n)
    line5 = (x5 * n)
    result = f'{line1}\n{line2}\n{line3}\n{line4}\n{line5}'
    return result
