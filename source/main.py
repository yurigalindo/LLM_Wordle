from wordle import get_word, check_answer
from termcolor import colored
from LLM_utils import GameLogger, colors_to_prompt


def main():
  word = get_word()
  logger = GameLogger()
  logger.log_feedback("Write a 5-letter word to start the game:")

  for _ in range(6):
    # Ask for guess
    guess = ""
    while len(guess)!=5:
      guess = input("Write a 5-letter word to start the game:")
    guess = guess.upper()
    logger.log_guess(guess)

    # Check guess against word
    colors = check_answer(guess,word)
    logger.log_feedback(colors_to_prompt(guess,colors))
    text = [colored(guess[i],colors[i]) for i in range(5)]
    text = "".join(text)
    print(text)
    if guess.upper() == word:
       print("You have correctly guessed the word, congratulations!")
       logger.log_feedback("You have correctly guessed the word, congratulations!")
       logger.compile_logs()
       return
  print(f"You have exhausted your guesses. The correct word was: {word}")
  logger.log_feedback(f"You have exhausted your guesses. The correct word was: {word}")
  logger.compile_logs()

if __name__ == '__main__':
    main()