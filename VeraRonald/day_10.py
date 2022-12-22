def get_signal_strength(file, max_cycle):
    register = {"X":1}
    cycle_number = 0
    try:
        with open(file, 'r') as file:
            lines  = file.readlines()

            for line in lines:
                instruction = line.strip()

                instruction_duration = 0
                if instruction == "noop":
                    cycle_number += 1
                    if cycle_number == max_cycle:
                        signal_strength = register["X"] * cycle_number
                        return signal_strength
                else:
                    instruction_duration = 2

                for i in range(instruction_duration):
                    cycle_number += 1

                    if i == instruction_duration - 1:
                        increment_value = int(instruction.split(" ")[-1])
                        register["X"] += increment_value
                    if cycle_number == max_cycle:
                        signal_strength = register["X"] * cycle_number
                        return signal_strength

    except FileNotFoundError:
        print('File not found')

# PART 1
'''
Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. 
'''
cycles = [i for i in range(20, 221, 40)]
result = sum([get_signal_strength("input.txt", cycle) for cycle in cycles])
print(result)