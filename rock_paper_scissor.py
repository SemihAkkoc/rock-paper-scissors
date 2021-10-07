import random

rpsDictionary = {0: 'ROCK',
                 1: 'PAPER',
                 2: 'SCISSOR'}

possibleList = [(0, 0, 'Tie'), (0, 2, 'Win'), (0, 1, 'Lose'),
                (1, 0, 'Win'), (1, 2, 'Lose'), (1, 1, 'Tie'),
                (2, 0, 'Lose'), (2, 2, 'Tie'), (2, 1, 'Win')]

userChoice = int(input('Chose between rock(0), paper(1), scissor(2): '))
compChoice = random.randint(0, 2)

currChoice = [(userChoice, compChoice)]

for listLoop in possibleList:
    if currChoice[0][0] == listLoop[0] and currChoice[0][1] == listLoop[1]:
        print('\nYou chose {0:s}\n'
              'Computer chose {1:s}\n'
              'Game score is: {2:s}'.format(rpsDictionary[currChoice[0][0]], rpsDictionary[currChoice[0][1]], listLoop[2]))
