from openai import OpenAI
import json

class OpenAiPlayer():
  def __init__(self):
    with open("data/prompt_0.json") as file:
      self.prompt = json.load(file)
    self.client = OpenAI()
  
  def update_prompt(self,feedback):
    self.prompt.append({"role": "user", "content": feedback})

  def prompt_guess(self):
    for _ in range(5):
      # Tries multiple times if guess is not a 5 letter word
      completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=self.prompt,
        max_tokens=15
      )
      guess = completion.choices[0].message.content
      if len(guess) == 5:
        break
    if len(guess) != 5:
      guess = "soare"
    self.prompt.append({"role": "assistant", "content": guess})
    return guess