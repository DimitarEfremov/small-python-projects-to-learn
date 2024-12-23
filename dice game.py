from random import randrange

# TODO To be replace with question, what kind of game does the user want to play.
print('Welcome! Do you you want to play a game of dice?')

# TODO extract the game in function
user_answer = input('Please select Y or N: ').lower()
game_code = 0
counter_for_invalid_answers = 0

while game_code == 0:
    if user_answer == 'y':
        print('Lets play dice')
        game_code = 1
    elif user_answer == 'n':
        # to be replace with if the user wants to play another game
        print('See you soon! ;)')
        exit(0)
    else:
        counter_for_invalid_answers += 1
        if counter_for_invalid_answers > 5:
            print('Too many invalid answers')
            exit(0)
        user_answer = input('Invalid input, please select \'Y\' or \'N\': ')

if game_code == 1:
    player_1 = input('Player one, please enter your name: ')
    player_2 = input('Player one, please enter your name: ')
    rounds = int(input('How many rounds do you want to play, maximum round are 6: '))

    counter_for_invalid_answers = 0
    while not 1 <= rounds <= 6:
        if counter_for_invalid_answers >= 4:
            print('Too many invalid answers')
            exit(0)
        rounds = int(input('Rounds must be between 1 and 6: '))
        counter_for_invalid_answers += 1

    wins_player_1_counter = 0
    wins_player_2_counter = 0
    draws_counter = 0

    for r in range(rounds):
        numb_player_1 = randrange(1, 6, 1) + randrange(1, 6, 1)
        print(f'{player_1} rolled {numb_player_1}')
        numb_player_2 = randrange(1, 6, 1) + randrange(1, 6, 1)
        print(f'{player_2} rolled {numb_player_2}')

        if numb_player_1 > numb_player_2:
            print(f'{player_1} won!')
            wins_player_1_counter += 1
        elif numb_player_2 > numb_player_1:
            print(f'{player_2} won!')
            wins_player_2_counter += 1
        else:
            print('Draw!')
            draws_counter += 1

    print(f'{player_1} won {wins_player_1_counter} games.')
    print(f'{player_2} won {wins_player_2_counter} games.')
    print(f'There were {draws_counter} draws.')

    if wins_player_1_counter > wins_player_2_counter:
        print(f'{player_1} is winner')
    elif wins_player_2_counter > wins_player_1_counter:
        print(f'{player_2} is winner')
    else:
        print('DRAW!!!')

