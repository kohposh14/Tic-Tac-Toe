import random


board = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]


def printboard():
    print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
    print('------')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('------')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])


def isdraw():
    for i in range (0,3):
        for j in range (0,3):
            if board[i][j]==' ':
                return False

    return True


def iswin():
    if board[0][0]==board[0][1] and board[0][0]==board[0][2] and board[0][0] != ' ':
        return True

    if board[1][0]==board[1][1] and board[1][0]==board[1][2] and board[1][0] != ' ':
        return True

    if board[2][0]==board[2][1] and board[2][0]==board[2][2] and board[2][0] != ' ':
        return True

    if board[0][0]==board[1][0] and board[0][0]==board[2][0] and board[0][0] != ' ':
        return True

    if board[0][1]==board[1][1] and board[0][1]==board[2][1] and board[0][1] != ' ':
        return True

    if board[0][2]==board[1][2] and board[0][2]==board[2][2] and board[0][2] != ' ':
        return True

    if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0] !=' ':
        return True

    if board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2] !=' ':
        return True

    return False

def insertmove(pos,move):
    posi=pos//3
    posj=pos%3
    if posi<0 or posj<0 or posi>2 or posj>2 or board[posi][posj]!=' ':
        print('Invalid move, please try again')
        n=int(input())
        insertmove(n,move)

    else:
        board[posi][posj]=move
        printboard()
        if iswin() and move=='X':
            print('Bot wins!')
            exit()
        elif iswin() and move=='O':
            print('Player 2 wins!')
            exit()
        elif isdraw():
            print('Game is a draw!')
            exit()



bot='X'
player='O'


def whowins(charc):
    if board[0][0]==board[0][1] and board[0][0]==board[0][2] and board[0][0] == charc:
        return True

    if board[1][0]==board[1][1] and board[1][0]==board[1][2] and board[1][0] == charc:
        return True

    if board[2][0]==board[2][1] and board[2][0]==board[2][2] and board[2][0] == charc:
        return True

    if board[0][0]==board[1][0] and board[0][0]==board[2][0] and board[0][0] == charc:
        return True

    if board[0][1]==board[1][1] and board[0][1]==board[2][1] and board[0][1] == charc:
        return True

    if board[0][2]==board[1][2] and board[0][2]==board[2][2] and board[0][2] == charc:
        return True

    if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0] == charc:
        return True

    if board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2] == charc:
        return True

    return False


def minimax(ismax):
    if whowins(bot):
        return 100
    if whowins(player):
        return -10000
    if isdraw():
        return 0

    if ismax:
        mscore=-1e8
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] != ' ':
                    continue
                board[i][j] = bot
                s = minimax(False)
                board[i][j] = ' '
                if s > mscore:
                    mscore = s

        return mscore

    else:
        mscore = 1e8
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] != ' ':
                    continue
                board[i][j] = player
                s = minimax(True)
                board[i][j] = ' '
                if s < mscore:
                    mscore = s

        return mscore



def botmove(firstc):

    if firstc==0:
        firstc+=1
        li=[0,1,2,3,4,5,6,7,8]
        insertmove(random.choice(li),bot)
        return


    mscore=-1e8
    mi=-1
    mj=-1
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]!=' ':
                continue
            board[i][j]=bot
            s=minimax(False)
            board[i][j]=' '
            if s>mscore:
                mscore=s
                mi=i
                mj=j

    insertmove(mi*3+mj,bot)



def playgame():
    printboard()
    firstc=0
    while 1:
        print()
        print()

        print('Bot plays:')
        botmove(firstc)
        print()
        print()
        firstc+=1
        print('Player:')
        n = int(input())-1
        insertmove(n, player)
        print()
        print()



playgame()
