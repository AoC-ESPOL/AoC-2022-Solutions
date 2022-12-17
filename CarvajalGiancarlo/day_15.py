print("\n¡AoC! - Day 15\n")

print('Part One')

file = open('input_day_15.txt', 'r')

sensor_map = {}

for line in file.readlines():
    line = line.strip('\n')
    sensor, beacon = line.split(':')

    sensor = sensor[sensor.index('x'):]
    beacon = beacon[beacon.index('x'):]

    sensorX, sensorY = sensor.split(',')
    beaconX, beaconY = beacon.split(',')

    sensorX = int(sensorX.strip()[2:])
    sensorY = int(sensorY.strip()[2:])

    beaconX = int(beaconX.strip()[2:])
    beaconY = int(beaconY.strip()[2:])

    sensor = (sensorX, sensorY)
    beacon = (beaconX, beaconY)

    sensor_map[sensor] = beacon

def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

setX = set()
beacons = set(map(lambda x: sensor_map[x], sensor_map))

for sensor in sensor_map:

    distance = manhattan(sensor, sensor_map[sensor])
    sensorX, sensorY = sensor

    difference = abs(sensorY - 2000000)
    
    if difference > distance:
        continue

    for i in range(sensorX - (distance - difference), sensorX + (distance - difference) + 1):
        setX.add(i)

result = len(setX) - len(set(filter(lambda x: x[1] == 2000000, beacons)))

print(f'Answer: {result}\n')