print("\n¡AoC! - Day 08\n")

print('Part One')

file = open('input_day_08.txt', 'r')

matrix = []

while True:
    line = file.readline()
    if(len(line) == 0):
        break
    
    line = line.replace('\n', '')
    row = []

    for char in line:
        row.append(int(char))
    
    matrix.append(row)

result = set()

for i in range(1, len(matrix)-1):
    aux_list = []
    for j in range(0, len(matrix[0])-2):
        aux_list.append(matrix[i][j])
        if matrix[i][j+1] > max(aux_list):
            result.add((i, j+1))

    aux_list = []
    for j in reversed(range(2, len(matrix[0]))):
        aux_list.append(matrix[i][j])
        if matrix[i][j-1] > max(aux_list):
            result.add((i, j-1))

for j in range(1, len(matrix[0])-1):
    aux_list = []
    for i in range(0, len(matrix)-2):
        aux_list.append(matrix[i][j])
        if matrix[i+1][j] > max(aux_list):
            result.add((i+1, j))

    aux_list = []
    for i in reversed(range(2, len(matrix))):
        aux_list.append(matrix[i][j])
        if matrix[i-1][j] > max(aux_list):
            result.add((i-1, j))

print(f'\n\tAnswer: {len(result) + 2*len(matrix) + 2*(len(matrix[0]) - 2)}')

print('\nPart Two')

scores = []

for i in range(1, len(matrix)-1):
    for j in range(1, len(matrix[0])-1):
        left = 0
        for n in reversed(range(0, j)):
            left += 1
            if matrix[i][n] >= matrix[i][j]:
                break
        right = 0
        for n in (range(j+1, len(matrix[0]))):
            right += 1
            if matrix[i][n] >= matrix[i][j]:
                break
        up = 0
        for n in reversed(range(0, i)):
            up += 1
            if matrix[n][j] >= matrix[i][j]:
                break
        bottom = 0
        for n in (range(i+1, len(matrix))):
            bottom += 1
            if matrix[n][j] >= matrix[i][j]:
                break
        scores.append(left*right*up*bottom)

print(f'\n\tAnswer: {max(scores)}\n')