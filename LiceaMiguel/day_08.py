lines = [x for x in open('day8.in').read().split("\n")]

datam = lines
dirs = {
    "1":(0,-1),
    "2":(0,1),
    "3":(1,0),
    "4":(-1,0)
}

s1=0
s2=0
for i in range(99):
    for j in range(99):
        seen = 0
        for  k in dirs.values()[::-1]:
            copy_i, copy_j = i,j
            seen_for = 1
            while 1:
                a,b = k
                copy_i += a
                copy_j += b
                if not (copy_i>=0 and copy_i<99 and copy_j>=0 and copy_j<99): break
                seen_for = False if datam[i][j] <= datam[copy_i][copy_j] else seen_for
            seen = True if seen_for else seen
        s1 = s1+1 if seen else s1

for i in range(99):
    for j in range(99):
        seen = 1
        for  k in dirs.values()[::-1]:
            a,b = k
            copy_i, copy_j = i+a,j+b
            seen_for = 1
            while 1:
                if not (copy_i>=0 and copy_i<99 and copy_j>=0 and copy_j<99):
                    seen_for -= 1
                    break
                if datam[i][j] <= datam[copy_i][copy_j]: break
                seen_for += 1
                copy_i += a
                copy_j += b
            seen *= seen_for
        s2 = s2 if s2>seen else seen
print(s1)
print(s2)
