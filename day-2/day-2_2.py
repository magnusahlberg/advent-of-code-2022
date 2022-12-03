import os

file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'input/input.txt')
file = open(file_name, 'r')
lines = file.read()

scores = {"A X": 3 + 0, # Loose, chose scissors (3)
          "A Y": 1 + 3, # Tie, choose rock (1)
          "A Z": 2 + 6, # Win, choose paper (2)
          "B X": 1 + 0, # Loose, chose rock (1)
          "B Y": 2 + 3, # Tie, choose paper (2)
          "B Z": 3 + 6, # Win, choose scissors (3)
          "C X": 2 + 0, # Loose, chose paper (2)
          "C Y": 3 + 3, # Tie, choose scissors (3)
          "C Z": 1 + 6  # Win, choose rock (1)
}

score = sum([scores[line] for line in lines.split('\n') if line != ''])

print(f"Total: {score}")