def integers():
    i = 1
    while True:
        yield i
        i += 1

def squares():
    for i in integers():
        result = i**2
        yield result

def take(n, generator):
    counter = 0
    result = []
    for i in generator:
        if counter < n:
            result.append(i)
            counter += 1
        else:
            return result
        
