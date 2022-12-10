def get_data(file):
    try:
        with open(file, 'r') as file:
            lines  = file.readlines()
            stacks  = {}
            procedures = []
            info_index = {"rows": {}, "stack_number": {}}
            for line in lines:
                line = line.strip("\n")
                if "move" in line or "from" in line or "to" in line:
                    info_procedure = line.split(" ")
                    procedures.append({"move":int(info_procedure[info_procedure.index("move")+1]),
                                        "from":info_procedure[info_procedure.index("from")+1],
                                        "to":info_procedure[info_procedure.index("to")+1]})
                else:
                    for index in range(len(line)):
                        if line[index].isnumeric():
                            info_index["stack_number"][line[index]] = index
                        elif line[index].isalpha():
                            if index not in info_index["rows"]:
                                info_index["rows"][index] = [line[index]]
                            else:
                                info_index["rows"][index].append(line[index])

                for key, value in info_index["stack_number"].items():
                    stacks[key] = info_index["rows"][value]
            return stacks, procedures
    except FileNotFoundError:
        print('File not found')

def reorganize_with_CrateMover9000(stacks, procedure):
    new_order_of_stacks = stacks
    for movement_repetition in range(procedure["move"]):
        stacks[procedure["to"]].insert(0, stacks[procedure["from"]].pop(0))
    return new_order_of_stacks

def reorganize_with_CrateMover9001(stacks, procedure):
    new_order_of_stacks = stacks

    if procedure["move"] == 1:
        stacks[procedure["to"]].insert(0, stacks[procedure["from"]].pop(0))
    else:
        stacks[procedure["to"]] = stacks[procedure["from"]][:procedure["move"]] + stacks[procedure["to"]]
        del stacks[procedure["from"]][:procedure["move"]]
    return new_order_of_stacks

# PART 1
initial_stacks, all_procedures = get_data("input.txt")
rearranged_stacks = initial_stacks.copy()
for i in all_procedures:
    rearranged_stacks = reorganize_with_CrateMover9000(rearranged_stacks, i)
top_crates = ""
for i in rearranged_stacks.values():
    top_crates += i[0]
print(top_crates)
# PART 2
initial_stacks, all_procedures = get_data("input.txt")
rearranged_stacks = initial_stacks.copy()
for i in all_procedures:
    rearranged_stacks = reorganize_with_CrateMover9001(rearranged_stacks, i)
top_crates = ""
for i in rearranged_stacks.values():
    top_crates += i[0]
print(top_crates)