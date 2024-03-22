import numpy as np

def get_word():
    """Returns a 5-letter uppercase word as string
    """
    words = np.loadtxt("data/shmookey_common_5.txt", dtype=str)
    return np.random.choice(words).upper()

def check_answer(guess,correct_word):
    """Evaluates the guess, returning a list with the color for each letter
    """
    colors = []
    for i,letter in enumerate(guess):
        if letter.upper() == correct_word[i]:
            colors.append("green")
        elif letter.upper() in correct_word:
            colors.append("yellow")
        else:
            colors.append("dark_grey")
    return colors


