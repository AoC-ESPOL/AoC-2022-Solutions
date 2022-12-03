lowercase_item_priorities = range(1, 27)
uppercase_item_priorities = range(27, 53)

def get_data(file):
    try:
        with open(file, 'r') as file:
            lines  = file.readlines()
            rucksacks = []
            for rucksack in lines:
                rucksacks.append(rucksack.strip())
            return rucksacks
    except FileNotFoundError:
        print('File not found')

def get_items_by_compartments(rucksack):
    number_of_items = len(rucksack)
    first_compartment = "".join(rucksack[:int(number_of_items/2)])
    second_compartment = "".join(rucksack[int(number_of_items/2):])
    items = [first_compartment, second_compartment]
    return items

def get_repeated_item(items):
    first_compartment, second_compartment = items
    repeated_item = ""
    for item in first_compartment:
        if item in second_compartment:
            repeated_item = item
            break
    return repeated_item

def get_item_priority(item):
    item_priority = 0
    if item.islower():
        item_priority += lowercase_item_priorities[list(map(chr, range(97, 123))).index(item)]
    elif item.isupper():
        item_priority += uppercase_item_priorities[list(map(chr, range(65, 91))).index(item)]
    return item_priority

def get_groups(rucksacks):
    group_extension = 3
    groups = []
    group = []
    for i in rucksacks:
        group.append(i)
        if len(group) == group_extension:
            groups.append(group.copy())
            group.clear()
    return groups

def get_common_item(rucksacks_group):
    first, second, third = rucksacks_group
    common_item = ""
    for item in first:
        if (item in second) and (item in third):
            common_item = item
            break
    return common_item

# PART 1
sum_of_the_priorities = sum([get_item_priority(get_repeated_item(get_items_by_compartments(i))) for i in get_data("input.txt")])
print(sum_of_the_priorities)
# PART 2
sum_of_the_priorities = sum([get_item_priority(get_common_item(i)) for i in get_groups(get_data("input.txt"))])
print(sum_of_the_priorities)