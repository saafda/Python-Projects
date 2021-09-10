import random
import time

print('This is a dice simulator. Regular dice ranging from 1-6 ')
dice_throw = random.randrange(1, 7)

var = True
while var == True:
    dice_throw = random.randrange(1, 7)
    if dice_throw == 1:
        for n in range(30):
            dice_throw = random.randrange(1, 7)
            if dice_throw == 1:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║                 ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║                 ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 2:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 3:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
                question = True
            if dice_throw == 4:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 5:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 6:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║    ●       ●    ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
        row1 = '╔═════════════════╗'
        row2 = '║                 ║'
        row3 = '║                 ║'
        row4 = '║                 ║'
        row5 = '║        ●        ║'
        row6 = '║                 ║'
        row7 = '║                 ║'
        row8 = '║                 ║'
        row9 = '╚═════════════════╝'
        print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}')
        question = True
        while question == True:
            decision = input('Do you want to role the dice again? (Yes/No) ')
            if decision.lower() == 'yes':
                question = False
                break
            elif decision.lower() == 'no':
                question = False
                var = False
                print('Finished rolling the dice.')
                break

        

    if dice_throw == 2:
        for n in range(30):
            dice_throw = random.randrange(1, 7)
            if dice_throw == 1:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║                 ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║                 ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 2:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 3:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
                question = True
            if dice_throw == 4:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 5:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 6:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║    ●       ●    ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
        row1 = '╔═════════════════╗'
        row2 = '║                 ║'
        row3 = '║            ●    ║'
        row4 = '║                 ║'
        row5 = '║                 ║'
        row6 = '║                 ║'
        row7 = '║    ●            ║'
        row8 = '║                 ║'
        row9 = '╚═════════════════╝'
        print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}')
        question = True
        while question == True:
            decision = input('Do you want to role the dice again? (Yes/No) ')
            if decision.lower() == 'yes':
                question = False
            elif decision.lower() == 'no':
                question = False
                var = False
                print('Finished rolling the dice.')
                break

    if dice_throw == 3:
        for n in range(30):
            dice_throw = random.randrange(1, 7)
            if dice_throw == 1:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║                 ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║                 ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 2:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 3:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
                question = True
            if dice_throw == 4:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 5:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 6:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║    ●       ●    ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
        row1 = '╔═════════════════╗'
        row2 = '║                 ║'
        row3 = '║            ●    ║'
        row4 = '║                 ║'
        row5 = '║        ●        ║'
        row6 = '║                 ║'
        row7 = '║    ●            ║'
        row8 = '║                 ║'
        row9 = '╚═════════════════╝'
        print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}')
        question = True
        while question == True:
            decision = input('Do you want to role the dice again? (Yes/No) ')
            if decision.lower() == 'yes':
                question = False
            elif decision.lower() == 'no':
                question = False
                var = False
                print('Finished rolling the dice.')
                break

    if dice_throw == 4:
        for n in range(30):
            dice_throw = random.randrange(1, 7)
            if dice_throw == 1:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║                 ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║                 ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 2:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 3:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
                question = True
            if dice_throw == 4:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 5:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 6:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║    ●       ●    ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
        row1 = '╔═════════════════╗'
        row2 = '║                 ║'
        row3 = '║    ●       ●    ║'
        row4 = '║                 ║'
        row5 = '║                 ║'
        row6 = '║                 ║'
        row7 = '║    ●       ●    ║'
        row8 = '║                 ║'
        row9 = '╚═════════════════╝'
        print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}')
        question = True
        while question == True:
            decision = input('Do you want to role the dice again? (Yes/No) ')
            if decision.lower() == 'yes':
                question = False
            elif decision.lower() == 'no':
                question = False
                var = False
                print('Finished rolling the dice.')
                break
        
    if dice_throw == 5:
        for n in range(30):
            dice_throw = random.randrange(1, 7)
            if dice_throw == 1:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║                 ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║                 ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 2:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 3:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
                question = True
            if dice_throw == 4:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 5:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 6:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║    ●       ●    ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
        row1 = '╔═════════════════╗'
        row2 = '║                 ║'
        row3 = '║    ●       ●    ║'
        row4 = '║                 ║'
        row5 = '║        ●        ║'
        row6 = '║                 ║'
        row7 = '║    ●       ●    ║'
        row8 = '║                 ║'
        row9 = '╚═════════════════╝'
        print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}')
        question = True
        while question == True:
            decision = input('Do you want to role the dice again? (Yes/No) ')
            if decision.lower() == 'yes':
                question = False
            elif decision.lower() == 'no':
                question = False
                var = False
                print('Finished rolling the dice.')
                break

    if dice_throw == 6:
        for n in range(30):
            dice_throw = random.randrange(1, 7)
            if dice_throw == 1:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║                 ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║                 ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 2:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 3:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║            ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●            ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
                question = True
            if dice_throw == 4:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║                 ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 5:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║        ●        ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
            if dice_throw == 6:
                row1 = '╔═════════════════╗'
                row2 = '║                 ║'
                row3 = '║    ●       ●    ║'
                row4 = '║                 ║'
                row5 = '║    ●       ●    ║'
                row6 = '║                 ║'
                row7 = '║    ●       ●    ║'
                row8 = '║                 ║'
                row9 = '╚═════════════════╝'
                print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}') ;time.sleep(0.1)
        row1 = '╔═════════════════╗'
        row2 = '║                 ║'
        row3 = '║    ●       ●    ║'
        row4 = '║                 ║'
        row5 = '║    ●       ●    ║'
        row6 = '║                 ║'
        row7 = '║    ●       ●    ║'
        row8 = '║                 ║'
        row9 = '╚═════════════════╝'
        print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}')
        question = True
        while question == True:
            decision = input('Do you want to role the dice again? (Yes/No) ')
            if decision.lower() == 'yes':
                question = False
            elif decision.lower() == 'no':
                question = False
                var = False
                print('Finished rolling the dice.')
                break
