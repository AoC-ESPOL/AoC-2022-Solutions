options = {"rock": ["A", "X", 1], "paper": ["B", "Y", 2], "scissor":["C", "Z", 3]}
score_table = {"loss": 0, "draw": 3, "win": 6}
win_moves = {"rock": "paper", "paper":"scissor", "scissor": "rock" } #  oponent: me
loss_moves = {"rock": "scissor", "paper":"rock", "scissor": "paper" } #  oponent: me

def getData(file, way): # Parameter how_move or how_result
    moves = []
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                play_info = line.strip().split(" ")
                opponent = play_info[0]

                if way == "how_move":
                    me = play_info[1]
                    move = {}

                    for key, value in options.items():
                        if opponent in value:
                            move["opponent"] = key
                        if me in value:
                            move["me"] = key
                        if len(move.keys()) == 2:
                            break
                    moves.append([move["opponent"], move["me"]])
                elif way == "how_result":
                    for key, value in options.items():
                        if opponent in value:
                            opponent = key
                            break
                    result = play_info[1]
                    me = calculeMove(opponent, result)
                    moves.append([opponent, me])

            return moves

    except FileNotFoundError:
        print('File not found')

def getResultForMe(move):
    result = ""
    if move[0] != move[1]:
        if (move[1] == "rock" and move[0] == "scissor") \
                or (move[1] == "paper" and move[0] == "rock") \
                or (move[1] == "scissor" and move[0] == "paper"):
            result = "win"
        else:
            result = "loss"
    else:
        result = "draw"
    return result

def getScores(moves):
    scores = []
    for move in moves:
        score = score_table[getResultForMe(move)]
        score += options[move[1]][-1]
        scores.append(score)
    return scores

def calculeMove(previous_move, expected_result):
    next_move = ""
    if expected_result == "Y":
        next_move = previous_move
    elif expected_result == "X":
        next_move = loss_moves[previous_move]
    elif expected_result == "Z":
        next_move = win_moves[previous_move]
    return next_move
# PART 1
jugadas = getData("input.txt", "how_move")
puntajes = getScores(jugadas)
puntaje_total = sum(puntajes)
print(puntaje_total)
# PART 2
jugadas = getData("input.txt", "how_result")
puntajes = getScores(jugadas)
puntaje_total = sum(puntajes)
print(puntaje_total)