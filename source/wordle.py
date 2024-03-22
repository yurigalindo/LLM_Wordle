def get_word():
    """Returns a 5-letter uppercase word as string
    """
    # TODO: Add a dictionary of words
    return "WEARY"

def check_answer(guess,correct_word):
    """Evaluates the guess, returning a list with the color for each letter
    """
    colors = []
    for i,letter in enumerate(guess):
        if letter.upper() == correct_word[i]:
            colors.append("green")
        elif letter.upper in correct_word:
            colors.append("yellow")
        else:
            colors.append("gray")
    return colors


