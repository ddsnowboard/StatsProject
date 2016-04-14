#!/usr/bin/python3
import csv
from functools import reduce
from random import randint
FILENAME = "combined.txt"

class Game:
    def __init__(self, away_score, home_score):
        self.home_score = home_score
        self.away_score = away_score
    def homeWon(self):
        return self.home_score > self.away_score
    def awayWon(self):
        return not self.homeWon()

games = []

with open(FILENAME, newline="") as f:
    reader = csv.reader(f)
    for game in reader:
        # The fields we want are (according to info.txt) 9 (Visiting team score)
        # and 10 (Home team score). Note that these are one less than it says 
        # in the info file because our array is zero-indexed, but theirs is 
        # one-indexed.
        if game[9] and game[10]:
            vis = int(game[9])
            home = int(game[10])
            games.append(Game(vis, home))
N = 1000
RUNS = 30
total = 0
for i in range(RUNS):
    p_hat = reduce(lambda x, y: x + (1 if y.homeWon() else 0), (games[randint(0, N - 1)] for i in range(N)), 0)
    total += p_hat
    print(p_hat)
print("The average was {}".format(total / RUNS))
