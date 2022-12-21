with open("day_21.txt") as file:
    contenido = file.read().splitlines()
import re
def get_root(lines):
    monkey_numbers = dict()
    while not "root" in monkey_numbers:
        for line in lines:
            monkey_name, equation = line.split(": ")
            try: 
                monkey_numbers[monkey_name] = eval(equation)
            except:
                pass
            strings = re.findall(r'[\w]+', equation)
            if all([string in monkey_numbers for string in strings]):
                for string in strings:
                    equation = equation.replace(string, str(monkey_numbers[string]))
                monkey_numbers[monkey_name] = eval(equation)
                if monkey_name == "root":
                    return [monkey_numbers[string] for string in strings], monkey_numbers[monkey_name]
    return None
answer = get_root(contenido)    
print("Part 1:", answer[1])
delta = 1
i = 1
while True:
    i += delta
    lines = [line if not line.startswith("humn") else "humn: " + str(i) for line in contenido]
    (num1, num2), answer = get_root(lines)    
    if num1 == num2:
        print("Part 2:" , i)
        break
    elif num1 > num2:
        delta *= 2
    else: 
        i -= delta
        delta = 1