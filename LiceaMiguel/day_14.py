lines = [line.strip() for line in open('day14.in')]

def obstacles():
    coords = set()
    for line in lines:
        points = [x.strip() for x in line.split('->')]
        bef_x, bef_y = [int(x) for x in points[0].split(",")]
        for point in points[1:]:
            cx,cy = [int(x.strip()) for x in point.split(",")]
            if cx == bef_x:
                for y in range(min(bef_y, cy),max(cy,bef_y)+1):
                    coords.add((cx, y))
            else:
                for x in range(min(bef_x, cx),max(cx, bef_x)+1):
                    coords.add((x,cy))
            bef_x, bef_y = cx,cy
    return coords

def c():
    coords = obstacles()
    higher_coord = max([hg for lg, hg in coords]) #max cordenate for y obstacles
    cont = 0
    while True:
        x,y = 500,0
        while True:
            if (x, y+1) not in coords:
                y+=1
            elif (x-1, y+1) not in coords:
                x -=1
                y +=1
            elif (x+1, y+1) not in coords:
                x+=1
                y+=1
            else:
                coords.add((x,y))
                break
            
            if y>higher_coord:
                return cont
        cont+=1 

def x():
    coords = obstacles()
    higher_coord = max([hg for lg, hg in coords])
    cont = 0
    while True:
        x,y = 500,0
        while True:
            if (x,y) in coords:
                return cont
            elif y ==higher_coord+1:
                coords.add((x,y))
                break
            elif (x, y+1) not in coords:
                y+=1
            elif (x-1, y+1) not in coords:
                x -=1
                y+=1
            elif (x+1, y+1) not in coords:
                x+=1
                y+=1
            else:
                coords.add((x,y))
                break
        cont+=1

print(c())
print(x())