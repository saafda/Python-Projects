print('Tic-Tac-Toe spill eller 3 på rad\nSirkel starter med å velge en rute og deretter velger kryss en rute til en har 3 på rad')
""""
numline1 = '      |     |      '
numline2 = '  1   |  2  |   3  '
numline3 = '______|_____|______'
numline5 = '  4   |  5  |   6  '
numline8 = '  7   |  8  |   9  '

line1 = '      |     |      '
line2 = '      |     |      '
line3 = '______|_____|______'
line5 = '      |     |      '
line8 = '      |     |      '



print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')

var = False

move_list = []

while var == False:
    move1 = int(input('(Runde 1) Velg en rute (1-9): '))
    move_list.append(move1)
    
    if move1 == 1:
        line2 = '  ◯   |     |      '
        print(line1, line2, line3, line1, line5, line3, line1, line8, line1, sep = '\n')
    elif move1 == 2:
        line2 = '      |  ◯  |      '
        print(line1, line2, line3, line1, line5, line3, line1, line8, line1, sep = '\n')
    elif move1 == 3:
        line2 = '      |     |   ◯  '
        print(line1, line2, line3, line1, line5, line3, line1, line8, line1, sep = '\n')
    elif move1 == 4:
        line5 = '  ◯   |     |      '
        print(line1, line2, line3, line1, line5, line3, line1, line8, line1, sep = '\n')
    elif move1 == 5:
        line5 = '      |  ◯  |      '
        print(line1, line2, line3, line1, line5, line3, line1, line8, line1, sep = '\n')
    elif move1 == 6:
        line5 = '      |     |   ◯  '
        print(line1, line2, line3, line1, line5, line3, line1, line8, line1, sep = '\n')
    elif move1 == 7:
        line8 = '  ◯   |     |      '
        print(line1, line2, line3, line1, line5, line3, line1, line8, line1, sep = '\n')
    elif move1 == 8:
        line8 = '      |  ◯  |      '
        print(line1, line2, line3, line1, line5, line3, line1, line8, line1, sep = '\n')
    elif move1 == 9:
        line8 = '      |     |   ◯  '
        print(line1, line2, line3, line1, line5, line3, line1, line8, line1, sep = '\n')
    move2 = int(input('(Runde 2) Velg en rute (1-9): '))
    """


vertical_1 = []
vertical_2 = []
vertical_3 = []
horizontal_1 = []
horizontal_2 = []
horizontal_3 = []
diagonal_1 = []
diagonal_2 = []


ruter = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

numline1 = '      |     |      '
numline2 = f'  {ruter[0]}   |  {ruter[1]}  | {ruter[2]}  '
numline3 = '______|_____|______'
numline5 = f'  {ruter[3]}   |  {ruter[4]}  |   {ruter[5]}  '
numline8 = f'  {ruter[6]}   |  {ruter[7]}  |   {ruter[8]}  '


print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')

player_1 = True
player_2 = False

player_1_moves = []
player_2_moves = []

num1 = 1
num2 = -1 

var = True
while var == True:
    while player_1 == True:
        trekk = int(input('Player 1 velg en rute: '))
        player_1_moves.append(trekk)
        if trekk == 1:
            ruter[0] = ruter[0].replace(' ', 'X')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  | {ruter[2]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
            vertical_1.append(num1)
            horizontal_1.append(num1)
            diagonal_2.append(num1)
        elif trekk == 2:
            ruter[1] = ruter[1].replace(' ', 'X')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  | {ruter[2]}  '
            vertical_2.append(num1)
            horizontal_1.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 3:
            ruter[2] = ruter[2].replace(' ', 'X')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  |  {ruter[2]}  '
            vertical_3.append(num1)
            horizontal_1.append(num1)
            diagonal_1.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 4:     
            ruter[3] = ruter[3].replace(' ', 'X')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            vertical_1.append(num1)
            horizontal_2.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 5:
            ruter[4] = ruter[4].replace(' ', 'X')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            vertical_2.append(num1)
            horizontal_2.append(num1)
            diagonal_1.append(num1)
            diagonal_2.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 6:
            ruter[5] = ruter[5].replace(' ', 'X')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            vertical_3.append(num1)
            horizontal_2.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 7:
            ruter[6] = ruter[6].replace(' ', 'X')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            vertical_1.append(num1)
            horizontal_3.append(num1)
            diagonal_1.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 8:
            ruter[7] = ruter[7].replace(' ', 'X')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            vertical_2.append(num1)
            horizontal_3.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 9:
            ruter[8] = ruter[8].replace(' ', 'X')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            vertical_3.append(num1)
            horizontal_3.append(num1)
            diagonal_2.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        player_1, player_2 = player_2, player_1

    if sum(vertical_1) == 3 or sum(vertical_2) == 3 or sum(vertical_3) == 3 or sum(horizontal_1) == 3 or sum(horizontal_2) == 3 or sum(horizontal_3) == 3 or sum(diagonal_1) == 3 or sum(diagonal_2) == 3:
        var = False
        print('Player 1 wins!!!')
        break
    while player_2 == True:
        trekk = int(input('Player 2 velg en rute: '))
        player_2_moves.append(trekk)
        if trekk == 1:
            ruter[0] = ruter[0].replace(' ', '◯')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  | {ruter[2]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
            vertical_1.append(num2)
            horizontal_1.append(num2)
            diagonal_2.append(num2)
            print(vertical_1, horizontal_1, diagonal_2)
        elif trekk == 2:
            ruter[1] = ruter[1].replace(' ', '◯')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  | {ruter[2]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
            vertical_2.append(num2)
            horizontal_1.append(num2)
            print(vertical_2, horizontal_1)
        elif trekk == 3:
            ruter[2] = ruter[2].replace(' ', '◯')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  | {ruter[2]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
            vertical_3.append(num2)
            horizontal_1.append(num2)
            diagonal_1.append(num2)
            print(vertical_3, horizontal_1, diagonal_1)
        elif trekk == 4:  
            ruter[3] = ruter[3].replace(' ', '◯')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')        
            vertical_1.append(num2)
            horizontal_2.append(num2)
            print(vertical_1, horizontal_2)
        elif trekk == 5:
            ruter[4] = ruter[4].replace(' ', '◯')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')       
            vertical_2.append(num2)
            horizontal_2.append(num2)
            diagonal_1.append(num2)
            diagonal_2.append(num2)
            print(vertical_2, horizontal_2, diagonal_1, diagonal_2)
        elif trekk == 6:
            ruter[5] = ruter[5].replace(' ', '◯')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')     
            vertical_3.append(num2)
            horizontal_2.append(num2)
            print(vertical_3, horizontal_2)
        elif trekk == 7:
            ruter[6] = ruter[6].replace(' ', '◯')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')    
            vertical_1.append(num2)
            horizontal_3.append(num2)
            diagonal_1.append(num2)
            print(vertical_1, horizontal_3, diagonal_1)
        elif trekk == 8:
            ruter[7] = ruter[7].replace(' ', '◯')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')   
            vertical_2.append(num2)
            horizontal_3.append(num2)
            print(vertical_2, horizontal_3)
        elif trekk == 9:
            ruter[8] = ruter[8].replace(' ', '◯')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')   
            vertical_3.append(num2)
            horizontal_3.append(num2)
            diagonal_2.append(num2)
            print(vertical_3, horizontal_3, diagonal_2)
        player_1, player_2 = player_2, player_1

    if sum(vertical_1) == -3 or sum(vertical_2) == -3 or sum(vertical_3) == -3 or sum(horizontal_1) == -3 or sum(horizontal_2) == -3 or sum(horizontal_3) == -3 or sum(diagonal_1) == -3 or sum(diagonal_2) == -3:
        var = False
        print('Player 2 wins!!!')
        break