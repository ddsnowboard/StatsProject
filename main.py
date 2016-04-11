#!/usr/bin/python3
import csv
FILENAME = "combined.txt"
home_wins = 0
guest_wins = 0
total_games = 0
with open(FILENAME, newline="") as f:
    reader = csv.reader(f)
    for game in reader:
        # The fields we want are (according to info.txt) 9 (Visiting team score)
        # and 10 (Home team score). Note that these are one less than it says 
        # in the info file because our array is zero-indexed, but theirs is 
        # one-indexed.
        if game[9] and game[10]:
            total_games += 1
            vis = int(game[9])
            home = int(game[10])
            if vis > home:
                guest_wins += 1
            elif home > vis:
                home_wins += 1
    print("Home won {} times and visitors won {} times, out of {} games".format(home_wins, guest_wins, total_games))
