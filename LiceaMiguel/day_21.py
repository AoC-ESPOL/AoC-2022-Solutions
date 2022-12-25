import sympy
import functools
inputs = open('day21.in').read()

@functools.lru_cache
def eval_eq(name):
    if isinstance(ops[name], sympy.Symbol):
        return ops[name]
    elif ops[name].isdigit():
        return int(ops[name])
    else:
        op = ops[name].split()
        op1 = eval_eq(op[0])
        op2 = eval_eq(op[2])
        return eval(str(op1) + " " + op[1] +" " + str(op2))

ops = dict(line.split(": ") for line in inputs.split("\n"))

def s1():
    return int(eval_eq("root"))

print(s1())

def s2():
    ops["humn"] = sympy.operations("humn") # cold
    op = ops["root"].split()
    op1 = eval_eq(op[0])
    op2 = eval_eq(op[2])
    ops = sympy.solve(op1 - op2, ops["humn"])
    return int(round(ops[0]))

print(s2())