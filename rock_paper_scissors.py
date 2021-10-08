import random

rps_dictionary = {0: 'ROCK',
                 1: 'PAPER',
                 2: 'SCISSOR'}

possible_list = [(0, 0, 'Tie'), (0, 2, 'Win'), (0, 1, 'Lose'),
                (1, 0, 'Win'), (1, 2, 'Lose'), (1, 1, 'Tie'),
                (2, 0, 'Lose'), (2, 2, 'Tie'), (2, 1, 'Win')]

user_choice = int(input('Chose between rock(0), paper(1), scissor(2): '))
comp_choice = random.randint(0, 2)

curr_choice = [(user_choice, comp_choice)]

for list_loop in possible_list:
    if curr_choice[0][0] == list_loop[0] and curr_choice[0][1] == list_loop[1]:
        print('\nYou chose {0:s}\n'
              'Computer chose {1:s}\n'
              'Game score is: {2:s}'.format(rps_dictionary[curr_choice[0][0]], rps_dictionary[curr_choice[0][1]], list_loop[2]))
