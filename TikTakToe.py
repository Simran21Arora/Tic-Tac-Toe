def askName():
 player1=input('Enter a name for the X player : ')
 player2=input('Enter a name for the O player : ')
 print('Who plays first, ' , player1 , ' or ' , player2 , '?')
 turn=input()
 if turn==player1 or turn==player2:
     if turn==player1:
         turn2=player2
         a='X'
         b='O'
     else:
         turn2=player1
         a='O'
         b='X'
     begin(turn,turn2,a,b)
 else:
     print(turn , ' is not a registered player.')
     askName()

def begin(turn,turn2,a,b):
    moves=9
    end_check=0
    y=turn
    play=1
    while True:
        print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
        print('___|___|___')
        print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
        print('___|___|___')
        print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
        print('   |   |   ')
        print('**********************************')
        end_check=check(a,b)
        if moves==0:
          print('Game is over:')
          print('It is a tie!!')
          break
        elif end_check==1:
          print('Game is over:')
          print(turn ,' wins!!')
          break
        elif end_check==2:
          print('Game is over:')
          print(turn2, ' wins!!')
          break
        while True:
          print('player of current turn : ', y)
          if play==1:
           r1=chooseRow()
           c1=chooseCol()
           if board[r1][c1]=='.':
             board[r1][c1]=a
             moves=moves-1
             play=2
             y=turn2
             break
           else:
             print('Wrong input! Space already occupied.')
             continue
          else:
              r2 = chooseRow()
              c2 = chooseCol()
              if board[r2][c2] == '.':
                  board[r2][c2] = b
                  moves = moves - 1
                  play = 1
                  y = turn
                  break
              else:
                  print('Wrong input! Space already occupied.')
                  continue
    answer=input('Would you like to play again ? (Y/N)')
    if answer=='Y':
        for i in range(rows):
            for j in range(cols):
                board[i][j] = '.'
        askName()
    elif answer=='N':
        print('Thanks for playing!! Bye.')
    else:
      while answer!='Y' or answer!='N':
         print(answer, ' is not a valid answer.')
         answer = input('Would you like to play again ? (Y/N)')
         if answer == 'Y':
          for i in range(rows):
           for j in range(cols):
            board[i][j]='.'
          askName()
         elif answer == 'N':
          print('Thanks for playing!! Bye.')
          break

def chooseRow():
    r=int(input('Choose a row number (0 to 2) :'))
    while r!=0 and r!=1 and r!=2:
        print(r , ' is not a valid row.')
        r = int(input('Choose a row number (0 to 2) :'))
    return r

def chooseCol():
    c=int(input('Choose a column number (0 to 2) :'))
    while c!=0 and c!=1 and c!=2:
        print(c, ' is not a valid column.')
        c=int(input('Choose a column number (0 to 2) :'))
    return c

def check(p1,p2):
    #to check if player one has won
    #horizontal
    if board[0][0] == board[0][1] == board[0][2] == p1:
        return 1
    if board[1][0] == board[1][1] == board[1][2] == p1:
        return 1
    if board[2][0] == board[2][1] == board[2][2] == p1:
        return 1
    #diagonal
    if board[0][0] == board[1][1] == board[2][2] == p1:
        return 1
    if board[0][2] == board[1][1] == board[2][0] == p1:
        return 1
    #verticle
    if board[0][0] == board[1][0] == board[2][0] == p1:
        return 1
    if board[0][1] == board[1][1] == board[2][1] == p1:
        return 1
    if board[0][2] == board[1][2] == board[2][2] == p1:
        return 1

    #to check if player two has won
    if board[0][0] == board[0][1] == board[0][2] == p2:
        return 2
    if board[1][0] == board[1][1] == board[1][2] == p2:
        return 2
    if board[2][0] == board[2][1] == board[2][2] == p2:
        return 2
    if board[0][0] == board[1][1] == board[2][2] == p2:
        return 2
    if board[0][2] == board[1][1] == board[2][0] == p2:
        return 2
    if board[0][0] == board[1][0] == board[2][0] == p2:
        return 2
    if board[0][1] == board[1][1] == board[2][1] == p2:
        return 2
    if board[0][2] == board[1][2] == board[2][2] == p2:
        return 2
    return 0

rows, cols = 3, 3
board = [['.' for i in range(rows)] for j in range(cols)]
askName()