import pandas as pd
from os import listdir

def colors_to_prompt(guess,colors):
    prompts = []
    for letter,color in zip(guess,colors):
        prompt = f"{letter} - "
        if color == "green":
            prompt += "This letter is in the correct spot."
        elif color == "yellow":
            prompt += "This letter is present in the word but in another spot."
        else:
            prompt += "This letter is not present in the word."
        prompts.append(prompt)
    return "".join(prompts)

class GameLogger():
    def __init__(self):
        self.logs = []
        self.dir = "data/game_examples/"
    def log_guess(self,guess):
        self.logs.append(("guess",guess))
    def log_feedback(self,feedback):
        self.logs.append(("feedback",feedback))
    def compile_logs(self):
        df = pd.DataFrame(self.logs)
        df.columns = ["source","text"]
        df.to_csv(self.dir + f"game_{len(listdir(self.dir))}.csv",index=False)