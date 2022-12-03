import os

file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'input/input.txt')
file = open(file_name, 'r')
lines = file.read()

scores = {"A X": 1 + 3, # Choose rock, tie
          "A Y": 2 + 6, # Choose paper, win
          "A Z": 3 + 0, # Choose scizzors, loose
          "B X": 1 + 0, # Choose rock, loose
          "B Y": 2 + 3, # Choose paper, tie
          "B Z": 3 + 6, # Choose scizzors, win
          "C X": 1 + 6, # Choose rock, win
          "C Y": 2 + 0, # Choose paper, loose
          "C Z": 3 + 3  # Choose scizzors, tie
}

score = sum([scores[line] for line in lines.split('\n') if line != ''])

print(f"Total: {score}")