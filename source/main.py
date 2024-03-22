from wordle import get_word, check_answer
from termcolor import colored


def main():
  word = get_word()
  for _ in range(6):
    guess = ""
    while len(guess)!=5:
      guess = input("Write a 5-letter word:")
    guess = guess.upper()
    colors = check_answer(guess,word)
    text = [colored(guess[i],colors[i]) for i in range(5)]
    text = "".join(text)
    print(text)
    if guess.upper() == word:
       print("You have correctly guessed the word, congratulations!")
       return
  print(f"You have exhausted your guesses. The correct word was: {word}")

if __name__ == '__main__':
    main()