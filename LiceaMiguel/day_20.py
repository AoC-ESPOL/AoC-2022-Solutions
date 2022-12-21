from collections import deque

lines = [int(line) for line in open('day20.in').read().strip().split("\n")]
num_lines = len(lines)
lines = [(i,value) for i, value in enumerate(lines)]

def s1():
    d = deque(lines)
    for i, _ in lines:
        while True:
            if d[0][0] == i:
                break
            d.rotate(-1)
        idx , n = d.popleft()
        d.rotate(-1 * n)
        d.appendleft((idx, n))

    while True:
        if d[0][1] == 0:
            break
        d.rotate(-1)

    return d[1000 % num_lines][1] + d[2000 % num_lines][1] + d[3000 % num_lines][1]

print(s1())

def s2():
    lines = [(i,n * 811589153) for i,n in lines]
    d = deque(lines)

    for _ in range(1, 11):
        for idx, n in lines:
            while True:
                if idx == d[0][0]:
                    break
                d.rotate(-1)
            index, n_init = d.popleft()
            max_rotate = len(lines) - 1
            sign = (n_init // abs(n_init)) if n_init != 0 else 1
            amount_to_rotate = ((abs(n_init) % max_rotate) * sign * -1)

            d.rotate(amount_to_rotate)
            d.appendleft((index, n_init))

        while True:
            if d[0][1] == 0:
                break
            d.rotate(-1)
    while True:
        if d[0][1] == 0:
            break
        d.rotate(-1)

    return sum([d[1000 % num_lines][1], d[2000 % num_lines][1], d[3000 % num_lines][1]])

print(s2)