from wordle import get_word, check_answer
from termcolor import colored
from LLM_utils import GameLogger, colors_to_prompt
from openai_utils import OpenAiPlayer


def main():
  word = get_word()
  logger = GameLogger()
  logger.log_feedback("Write a 5-letter word to start the game:")
  player = OpenAiPlayer()
  player.update_prompt("Write a 5-letter word to start the game:")

  for _ in range(6):
    # Ask for guess
    guess = player.prompt_guess()
    logger.log_guess(guess)
    guess = guess[-5:]
    guess = guess.upper()

    # Check guess against word
    colors = check_answer(guess,word)
    feedback = colors_to_prompt(guess,colors)
    logger.log_feedback(feedback)
    text = [colored(guess[i],colors[i]) for i in range(5)]
    text = "".join(text)
    print(text)
    if guess.upper() == word:
       print("You have correctly guessed the word, congratulations!")
       logger.log_feedback("You have correctly guessed the word, congratulations!")
       logger.compile_logs()
       return
    player.update_prompt(feedback)
  print(f"You have exhausted your guesses. The correct word was: {word}.")
  logger.log_feedback(f"You have exhausted your guesses. The correct word was: {word}.")
  logger.compile_logs()

if __name__ == '__main__':
    main()