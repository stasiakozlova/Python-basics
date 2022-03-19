def solution(n,k):
    people = [i for i in range(1, n+1)]
    circle = [i for i in range(1, n+1)]
    dead = []
    counter = 0
    while True:
        for person in people:
            if len(dead) == n - 1:
                return circle[0]
            counter += 1
            if counter % k == 0:
                    dead.append(person)
                    circle.pop(circle.index(person))
            if person == people[-1]:
                people.extend(circle)
