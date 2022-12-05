def get_data(file):
    try:
        with open(file, 'r') as file:
            lines  = file.readlines()
            section_pairs = []
            for line in lines:
                pair = line.strip().split(",")
                first_elf = pair[0].split("-")
                sections_set_1 = set(range(int(first_elf[0]), int(first_elf[1])+1))
                second_elf = pair[1].split("-")
                sections_set_2 = set(range(int(second_elf[0]), int(second_elf[1]) + 1))
                section_pairs.append([sections_set_1, sections_set_2])
            return section_pairs
    except FileNotFoundError:
        print('File not found')

def is_fully_contain(section_pair):
    return section_pair[0].issubset(section_pair[1]) or section_pair[1].issubset(section_pair[0])

def is_overlap(section_pair):
    return len(get_overlap_sections(section_pair)) != 0

def get_overlap_sections(section_pair):
    return section_pair[0] & section_pair[1]

# PART 1
total_fully_overlap_assignments = sum([1 for section_pair in get_data("input.txt") if is_fully_contain(section_pair)])
print(total_fully_overlap_assignments)

# PART 2
total_overlap_sections = sum([1 for section_pair in get_data("input.txt") if is_overlap(section_pair)])
print(total_overlap_sections)