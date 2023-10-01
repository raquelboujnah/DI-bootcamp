import random
 
def get_random_word():
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'rush', 'south']
    word = random.choice(wordslist)
    dash_word = "_ " * len(word)
    return dash_word

def player_guesses(word):
    found_word = []
    dash_word_updated = get_random_word()
    while word != found_word:
        print(dash_word_updated)
        player_guess = input('guess a letter')
        if player_guess.isalpha():
            if player_guess in word:
                dash_word_updated
