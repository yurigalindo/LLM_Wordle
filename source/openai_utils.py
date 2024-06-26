from openai import OpenAI
import json
import pandas as pd

def game_to_prompt(game_num):
  df = pd.read_csv(f"data/game_examples/game_{game_num}.csv")
  prompt = []
  for _,row in df.iterrows():
    if row['source'] == "feedback":
      prompt.append({"role": "user", "content": row['text']})
    else:
      prompt.append({"role": "assistant", "content": row['text']})
  with open(f"data/game_examples/game_{game_num}.json","w") as file:
    json.dump(prompt,file, indent=4)

class OpenAiPlayer():
  def __init__(self):
    with open("data/prompt_2.json") as file:
      self.prompt = json.load(file)
    self.client = OpenAI()
  
  def update_prompt(self,feedback):
    self.prompt.append({"role": "user", "content": feedback})

  def prompt_guess(self):
    completion = self.client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=self.prompt,
    )
    guess = completion.choices[0].message.content
    self.prompt.append({"role": "assistant", "content": guess})
    return guess