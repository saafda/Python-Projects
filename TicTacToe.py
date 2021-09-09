
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
numline2 = f'  {ruter[0]}   |  {ruter[1]}  |   {ruter[2]}  '
numline3 = '______|_____|______'
numline5 = f'  {ruter[3]}   |  {ruter[4]}  |   {ruter[5]}  '
numline8 = f'  {ruter[6]}   |  {ruter[7]}  |   {ruter[8]}  '

showcase1 = '      |     |      '
showcase2 = f'   1  |  2  |   2  '
showcase3 = '______|_____|______'
showcase4 = f'  4   |  5  |   6  '
showcase5 = f'  7   |  8  |   9  '

print(showcase1, showcase2, showcase3, showcase1, showcase4, showcase3, showcase1, showcase5, showcase1, sep = '\n' )

player_1 = True
player_2 = False

player_1_moves = []
player_2_moves = []

num1 = 1
num2 = -1

navn1 = input('Player 1 navn: ')
navn2 = input('Player 2 navn: ')
print(f'Tic-Tac-Toe spill eller 3 på rad\n{navn1} starter med å velge en rute og deretter velger {navn2} en rute til en har 3 på rad')

var = True
while var == True:
    while player_1 == True:
        trekk = input(f'{navn1} velg en rute: ')
        feil_input = True
        if trekk == '1' or trekk == '2' or trekk == '3' or trekk == '4' or trekk == '5' or trekk ==  '6' or trekk == '7' or trekk == '8' or trekk == '9':
            feil_input = False
        while feil_input == True:
            if type(trekk) != int:
                trekk = input('Velg en av rutene markert fra 1 til 9 ')
                if trekk == '1' or trekk == '2' or trekk == '3' or trekk == '4' or trekk == '5' or trekk ==  '6' or trekk == '7' or trekk == '8' or trekk == '9':
                    feil_input = False
        trekk = int(trekk)
        player_1_moves.append(trekk)
        if trekk == 1:
            if ruter[0] != ' ':
                print(f'{navn1} ruten er allerede tatt av {navn2}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[0] = ruter[0].replace(' ', 'X')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  |  {ruter[2]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
            vertical_1.append(num1)
            horizontal_1.append(num1)
            diagonal_2.append(num1)
        elif trekk == 2:
            if ruter[1] != ' ':
                print(f'{navn1} ruten er allerede tatt av {navn2}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[1] = ruter[1].replace(' ', 'X')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  |  {ruter[2]}  '
            vertical_2.append(num1)
            horizontal_1.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 3:
            if ruter[2] != ' ':
                print(f'{navn1} ruten er allerede tatt av {navn2}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[2] = ruter[2].replace(' ', 'X')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  |   {ruter[2]}  '
            vertical_3.append(num1)
            horizontal_1.append(num1)
            diagonal_1.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 4: 
            if ruter[3] != ' ':
                print(f'{navn1} ruten er allerede tatt av {navn2}. Velg en annen rute som ikke er tatt! ')
                break    
            ruter[3] = ruter[3].replace(' ', 'X')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            vertical_1.append(num1)
            horizontal_2.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 5:
            if ruter[4] != ' ':
                print(f'{navn1} ruten er allerede tatt av {navn2}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[4] = ruter[4].replace(' ', 'X')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            vertical_2.append(num1)
            horizontal_2.append(num1)
            diagonal_1.append(num1)
            diagonal_2.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 6:
            if ruter[5] != ' ':
                print(f'{navn1} ruten er allerede tatt av {navn2}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[5] = ruter[5].replace(' ', 'X')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            vertical_3.append(num1)
            horizontal_2.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 7:
            if ruter[6] != ' ':
                print(f'{navn1} ruten er allerede tatt av {navn2}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[6] = ruter[6].replace(' ', 'X')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            vertical_1.append(num1)
            horizontal_3.append(num1)
            diagonal_1.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 8:
            if ruter[7] != ' ':
                print(f'{navn1} ruten er allerede tatt av {navn2}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[7] = ruter[7].replace(' ', 'X')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            vertical_2.append(num1)
            horizontal_3.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        elif trekk == 9:
            if ruter[8] != ' ':
                print(f'{navn1} ruten er allerede tatt av {navn2}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[8] = ruter[8].replace(' ', 'X')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            vertical_3.append(num1)
            horizontal_3.append(num1)
            diagonal_2.append(num1)
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
        player_1, player_2 = player_2, player_1

    if ' ' not in ruter:   
         print('Uavgjort! Start på nytt!')
         var = False
         break     

    if sum(vertical_1) == 3 or sum(vertical_2) == 3 or sum(vertical_3) == 3 or sum(horizontal_1) == 3 or sum(horizontal_2) == 3 or sum(horizontal_3) == 3 or sum(diagonal_1) == 3 or sum(diagonal_2) == 3:
        var = False
        print(f'{navn1} er vinneren!!!')
        break
    while player_2 == True:
        trekk = input(f'{navn2} velg en rute: ')
        feil_input = True
        if trekk == '1' or trekk == '2' or trekk == '3' or trekk == '4' or trekk == '5' or trekk ==  '6' or trekk == '7' or trekk == '8' or trekk == '9':
            feil_input = False
        while feil_input == True:
            if type(trekk) != int:
                trekk = input('Velg en av rutene markert fra 1 til 9 ')
                if trekk == '1' or trekk == '2' or trekk == '3' or trekk == '4' or trekk == '5' or trekk ==  '6' or trekk == '7' or trekk == '8' or trekk == '9':
                    feil_input = False
        trekk = int(trekk)
        player_2_moves.append(trekk)
        if trekk == 1:
            if ruter[0] != ' ':
                print(f'{navn2} ruten er allerede tatt av {navn1}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[0] = ruter[0].replace(' ', '◯')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  |   {ruter[2]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
            vertical_1.append(num2)
            horizontal_1.append(num2)
            diagonal_2.append(num2)
        elif trekk == 2:
            if ruter[1] != ' ':
                print(f'{navn2} ruten er allerede tatt av {navn1}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[1] = ruter[1].replace(' ', '◯')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  |  {ruter[2]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
            vertical_2.append(num2)
            horizontal_1.append(num2)
        elif trekk == 3:
            if ruter[2] != ' ':
                print(f'{navn2} ruten er allerede tatt av {navn1}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[2] = ruter[2].replace(' ', '◯')
            numline2 = f'   {ruter[0]}  |  {ruter[1]}  |  {ruter[2]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')
            vertical_3.append(num2)
            horizontal_1.append(num2)
            diagonal_1.append(num2)
        elif trekk == 4:  
            if ruter[3] != ' ':
                print(f'{navn2} ruten er allerede tatt av {navn1}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[3] = ruter[3].replace(' ', '◯')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |  {ruter[5]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')        
            vertical_1.append(num2)
            horizontal_2.append(num2)
        elif trekk == 5:
            if ruter[4] != ' ':
                print(f'{navn2} ruten er allerede tatt av {navn1}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[4] = ruter[4].replace(' ', '◯')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')       
            vertical_2.append(num2)
            horizontal_2.append(num2)
            diagonal_1.append(num2)
            diagonal_2.append(num2)
        elif trekk == 6:
            if ruter[5] != ' ':
                print(f'{navn2} ruten er allerede tatt av {navn1}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[5] = ruter[5].replace(' ', '◯')
            numline5 = f'   {ruter[3]}  |  {ruter[4]}  |   {ruter[5]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')     
            vertical_3.append(num2)
            horizontal_2.append(num2)
        elif trekk == 7:
            if ruter[6] != ' ':
                print(f'{navn2} ruten er allerede tatt av {navn1}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[6] = ruter[6].replace(' ', '◯')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')    
            vertical_1.append(num2)
            horizontal_3.append(num2)
            diagonal_1.append(num2)
        elif trekk == 8:
            if ruter[7] != ' ':
                print(f'{navn2} ruten er allerede tatt av {navn1}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[7] = ruter[7].replace(' ', '◯')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')   
            vertical_2.append(num2)
            horizontal_3.append(num2)
        elif trekk == 9:
            if ruter[8] != ' ':
                print(f'{navn2} ruten er allerede tatt av {navn1}. Velg en annen rute som ikke er tatt! ')
                break
            ruter[8] = ruter[8].replace(' ', '◯')
            numline8 = f'   {ruter[6]}  |  {ruter[7]}  |   {ruter[8]}  '
            print(numline1, numline2, numline3, numline1, numline5, numline3, numline1, numline8, numline1, sep = '\n')   
            vertical_3.append(num2)
            horizontal_3.append(num2)
            diagonal_2.append(num2)
        player_1, player_2 = player_2, player_1

    if sum(vertical_1) == -3 or sum(vertical_2) == -3 or sum(vertical_3) == -3 or sum(horizontal_1) == -3 or sum(horizontal_2) == -3 or sum(horizontal_3) == -3 or sum(diagonal_1) == -3 or sum(diagonal_2) == -3:
        var = False
        print(f'{navn2} er vinneren!!!')
        break
    
