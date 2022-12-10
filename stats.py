import pygame

class Stats():
    "statistic research"

    def __init__(self):
        "initialization of statistics"
        self.reset_stats()
        self.run_game = True
        with open("highscore.txt", 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        "dinamic statistics"

        self.snowmen_left = 2
        self.score = 0