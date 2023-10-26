from random import choice

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def Gameboard(board):
    chars = {1: 'X', -1: 'O', 0: ' '}
    for x in board:
        for y in x:
            ch = chars[y]
            print(f'| {ch} |', end='')
        print('\n' + '---------------')
    print('===============')

def Clearboard(board):
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            board[x][y] = 0

def winningPlayer(board, player):
    conditions = [[board[0][0], board[0][1], board[0][2]],
                  [board[1][0], board[1][1], board[1][2]],
                  [board[2][0], board[2][1], board[2][2]],
                  [board[0][0], board[1][0], board[2][0]],
                  [board[0][1], board[1][1], board[2][1]],
                  [board[0][2], board[1][2], board[2][2]],
                  [board[0][0], board[1][1], board[2][2]],
                  [board[0][2], board[1][1], board[2][0]]]
    if [player, player, player] in conditions:
        return True
    return False

def gameWon(board):
    return winningPlayer(board, 1) or winningPlayer(board, -1)

def printResult(board):
    if winningPlayer(board, 1):
        print('X has won!\n')
    elif winningPlayer(board, -1):
        print('O\'s have won!\n')
    else:
        print('Draw\n')

def blanks(board):
    blank = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if board[x][y] == 0:
                blank.append([x, y])
    return blank

def boardFull(board):
    if len(blanks(board)) == 0:
        return True
    return False

def setMove(board, x, y, player):
    board[x][y] = player

def playerMove(board):
    e = True
    moves = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    while e:
        try:
            move = int(input('Enter a number between 1-9: '))
            if move < 1 or move > 9:
                print('Invalid Move! Try again!')
            elif not (moves[move] in blanks(board)):
                print('Invalid Move! Try again!')
            else:
                setMove(board, moves[move][0], moves[move][1], 1)
                Gameboard(board)
                e = False
        except (KeyError, ValueError):
            print('Enter a number!')

def getScore(board):
    if winningPlayer(board, 1):
        return 10
    elif winningPlayer(board, -1):
        return -10
    else:
        return 0

def abminimax(board, depth, alpha, beta, player):
    if depth == 0 or gameWon(board):
        return [getScore(board), None]

    if player == 1:
        max_score = -float('inf')
        best_move = None
        for cell in blanks(board):
            x, y = cell
            board[x][y] = player
            score, _ = abminimax(board, depth - 1, alpha, beta, -player)
            board[x][y] = 0
            if score > max_score:
                max_score = score
                best_move = cell
            alpha = max(alpha, max_score)
            if alpha >= beta:
                break
        return [max_score, best_move]
    else:
        min_score = float('inf')
        best_move = None
        for cell in blanks(board):
            x, y = cell
            board[x][y] = player
            score, _ = abminimax(board, depth - 1, alpha, beta, -player)
            board[x][y] = 0
            if score < min_score:
                min_score = score
                best_move = cell
            beta = min(beta, min_score)
            if alpha >= beta:
                break
        return [min_score, best_move]

def aiMove(board):
    depth = len(blanks(board))
    if depth == 9:
        return choice([(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)])
    _, best_move = abminimax(board, depth, -float('inf'), float('inf'), -1)
    return best_move

# Main game loop
while True:
    Gameboard(board)
    playerMove(board)
    if gameWon(board) or boardFull(board):
        printResult(board)
        play_again = input('Play again? (yes/no): ')
        if play_again.lower() != 'yes':
            break
        else:
            Clearboard(board)
            continue
    Gameboard(board)
    print("Computer's Turn:")
    x, y = aiMove(board)
    setMove(board, x, y, -1)
    if gameWon(board) or boardFull(board):
        printResult(board)
        play_again = input('Play again? (yes/no): ')
        if play_again.lower() != 'yes':
            break
        else:
            Clearboard(board)
            continue
