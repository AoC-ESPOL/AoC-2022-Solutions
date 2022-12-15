lines = [line for line in open("day15.in").read().strip().split("\n")]

def get_value():
    beacons = set()
    sensors = set()
    total_d = 0
    for line in lines:
        line = line.split()
        d = abs(int(line[9][2:])+int(line[3][2:-1]))+ abs(int(line[8][2:-1]) - int(line[2][2:-1]))
        beacons.add((int(line[8][2:-1]), int(line[9][2:])))
        sensors.add((int(line[2][2:-1]), int(line[3][2:-1]), d))
        total_d +=d
    return (beacons, sensors, total_d)

def s1():
    beacons, sensors, _ = get_value()
    s1 = 0
    for x in range(-10000000, 10000000):
        y = 2000000
        v = True
        for (x2,y2,d) in sensors:
            d_b = abs(y-y2) + abs(x-x2)
            v = False if d>=d_b else v
        s1 = s1+1 if (x,y) not in beacons and not v else s1 
    return s1

print(s1())

def s2():
    _, sensors, _ = get_value()
    ds = [(-1,-1),(-1,1),(1,-1),(1,1)]
    s2 = False
    for (x,y,d) in sensors:
        for d1 in range(2+d):
            d2 = (1+d)-d1
            for x1,y1 in ds:
                rx = x+d1*x1
                ry = y+d2*x2
                if rx<0 or rx>4000000 or ry<0 or ry>4000000:
                    continue
                v = True
                for (x2,y2,d) in sensors:
                    d_b = abs(ry-y2) + abs(rx-x2)
                    v = False if d>=d_b else v
                if not s2 and v:
                    return x*4000000 + y

print(s2())