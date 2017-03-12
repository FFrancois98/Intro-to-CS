def GuessTheNumber(mystery_num):
    num_guesses = 0
    user_guess = 0
    place_holder = mystery_num - 1
    while place_holder != mystery_num:
        user_guess = int(input('Enter a guess: '))
        if user_guess < mystery_num:
            print('Too low!')
        elif user_guess > mystery_num:
            print('Too high!')
        place_holder = user_guess
        num_guesses += 1
    if num_guesses == 1:
        if user_guess == mystery_num:
            print('You\'re correct! It took you', num_guesses, 'guess')
    else:
        if user_guess == mystery_num:
            print('You\'re correct! It took you', num_guesses, 'guesses')
GuessTheNumber(13)
