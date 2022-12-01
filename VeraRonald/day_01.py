# how many Calories are being carried by the Elf carrying the most Calories

def getData(file):
    try:
        with open(file, 'r') as file:
            lines = file.readlines()

            flag_position = []  # \n

            for i in range(len(lines)):
                line = lines[i]
                if line == "\n":
                    flag_position.append(i)

            calories_info = []

            for i in range(len(flag_position)):
                calories = 0
                if i == 0:
                    for line in lines[:flag_position[i]]:
                        calories += int(line.strip("\n"))
                    calories_info.append(calories)
                elif i == len(flag_position)-1:
                    for line in lines[flag_position[i]+1:]:
                        calories += int(line.strip("\n"))
                    calories_info.append(calories)
                else:
                    for line in lines[flag_position[i-1]+1:flag_position[i]]:
                        calories += int(line.strip("\n"))
                    calories_info.append(calories)
            return calories_info

    except FileNotFoundError:
        print('File not found')

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
# PART 1
max_calories = max(getData("input.txt"))
print(max_calories)

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
# PART 2
general_info = sorted(getData("input.txt"))
cautious_elfs = general_info[-3:]
total_calories = sum(cautious_elfs)
print(total_calories)
