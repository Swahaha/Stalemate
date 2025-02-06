import random

class Random_Agent:
    def __init__(self):
        pass

    def choose_action(self, legal_moves):
        return random.choice(legal_moves)

class Reinforcement_Learning_Agent:
    def __init__(self):
        self.move_history = []

    def update_move_history(self, state, reward):
        self.move_history.append((state, reward))

    def learn(self):
        pass
    
    def choose_action(self, legal_moves): # explore vs exploit
        next_move = None
        pass