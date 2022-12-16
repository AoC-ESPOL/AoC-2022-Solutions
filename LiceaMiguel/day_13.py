import itertools
import ast
import functools

lines = open('day13.in').read()
lines = lines.split("\n\n")

def compare(left ,right ):
    if isinstance(left, int) and isinstance(right,int):
        if left < right:
            return "good"
        elif left == right:
            return "eq"
        else:
            return "bad"
    elif isinstance(left, list) and isinstance(right, list):
        idx = 0
        while idx<len(left) and idx<len(right):
            r = compare(left[idx], right[idx])
            if r in ("good","bad"):
                return r
            idx += 1
        if idx==len(left) and idx<len(right):
            return "good"
        elif idx==len(right) and idx<len(left):
            return "bad"
        else:
            return "eq"
    elif isinstance(left, int) and not isinstance(right, int):
        left = [left]
    else:
        right = [right]
    return compare(left, right)

s1 = 0
for i,group in enumerate(lines):
    l1,l2 = [ast.literal_eval(x) for x in group.split('\n')]
    r = compare(l1, l2)
    if r=="good":
        s1 += 1+i
print(s1)

def comp(left,right):
    r = comp(left, right)
    if r == "good":
        return -1
    elif r =="bad":
        return 1
    else:
        return 0

lines = open('day13.in').read()
lines = lines.replace("\n\n", "\n")
l = [ast.literal_eval(line) for line in lines.split("\n")]
l.append([[2]])
l.append([[6]])
l = sorted(l, key=functools.cmp_to_key(lambda p1,p2: comp(p1,p2)))
print((l.index([[2]])+1)*(l.index([[6]])+1))

