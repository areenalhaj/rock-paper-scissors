#!/usr/bin/env python3
import time
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
modes = ["starter", "easy", "medium", "hard", "exit"]
"""The Player class is the parent class for all of the Players
in this game"""


# ------------------------------------------
# opens new page by printing 41 new lines
def new_page():
    lines(41)


# ------------------------------------------
# printing the number of lines you give
def lines(n):
    print(n * "\n")


# ------------------------------------------
# printing with 1 second sleep time after
def print_slowly(word):
    print(word)
    time.sleep(0.1)


# ------------------------------------------
# takes the question and puts it in input to take the answer
# from user and returns the answer
def answer_this(question):
    choice = input(question)
    return choice


# ------------------------------------------
# takes the input and the valid options and checks if the input
# is included in the given valid options or not
def check_valid(choice, options):
    if choice.lower() in options:
        return True
    else:
        return False


# ------------------------------------------
def enter_this(words, options):
    while (True):
        answer = answer_this("")
        validity = check_valid(
            answer, options)
        if (validity):
            return answer.lower()
        else:
            print_slowly(words)


# ------------------------------------------
def choose_mode(words, modes_list, player):
    mode = enter_this(words, modes_list)
    if mode == modes[0]:
        player = StarterPlayer()
    elif mode == modes[1]:
        player = RandomPlayer()
    elif mode == modes[2]:
        player = ReflectPlayer()
    elif mode == modes[3]:
        player = CyclePlayer()
    elif mode == 'exit':
        lines(1)
        return mode  # .lower()
    return player


# ------------------------------------------
def beats(one, two):
    if ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')):
        return 1
    elif (one == two):
        return 0.5
    else:
        return 0


# ------------------------------------------
def winner(move1, move2):
    if beats(move1, move2) == 1:
        return "ROBOT"
    elif beats(move2, move1) == 1:
        return "Human"
    else:
        return "BOTH PLAYERS"


# >>>>>>>>>>>>>  MAIN PLAYER CLASS   >>>>>>>>>>>>>>>>>>
class Player:
    def __init__(self):
        pass

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


# >>>>>>>>>>>>  STARTER MODE    >>>>>>>>>>>>>>>>>>>
class StarterPlayer(Player):
    def __init__(self):
        pass

    def move(self):
        # Starter player
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# >>>>>>>>>>>>   EASY MODE   >>>>>>>>>>>>>>>>>>>
class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        # random player
        choose = random.choice(range(2))
        return moves[choose]  # Random

    # It desn't learn, it's random
    def learn(self, my_move, their_move):
        pass


# >>>>>>>>>>>>>  MEDIUM MODE   >>>>>>>>>>>>>>>>>>
class ReflectPlayer(Player):

    def __init__(self):
        super().__init__()
        self.their_move = []
        self.round = 0

    def move(self):
        if self.round == 0:
            choose = random.choice(range(3))
            return moves[choose]  # Random
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.round += 1
        self.their_move = their_move
        return my_move


# >>>>>>>>>>>>  HARD MODE   >>>>>>>>>>>>>>>>>>>
class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.roundNum = 0
        self.startChoice = 0
        self.their_move = []
        self.round = 0

    def killer(self, move):
        if move == "rock":
            return "paper"
        elif move == "paper":
            return "scissors"
        else:
            return "rock"

    def move(self):
        if self.round == 0:
            choose = random.choice(range(3))
            self.startChoice = moves[choose]
            return self.startChoice  # Random
        else:
            return self.killer(self.their_move)

    def learn(self, my_move, their_move):
        self.round += 1
        self.my_move = my_move
        self.their_move = their_move
        return my_move


# >>>>>>>>>>>>  HUMAN PLAYER    >>>>>>>>>>>>>>>>>>>
class HumanPlayer(Player):
    def move(self):
        words = "Please type in an option of rock, paper, scissors."
        print_slowly(words)
        move_choice = enter_this(words, moves)
        return move_choice

    def learn(self, my_move, their_move):
        pass


# >>>>>>>>>>>>>>    GAME CLASS   >>>>>>>>>>>>>>>>>
class Game:
    def __init__(self, p1, humP2):
        self.p1 = p1
        self.humP2 = humP2
        self.p1_points = 0
        self.humP2_points = 0
        self.result = []
        self.winner = ""  # could be 1 or 2 or 3 for equalation

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.humP2.move()
        print_slowly(f"""----------------------------------
PLAYS: Robot: {move1} | (You): {move2}""")
        self.p1_points += beats(move1, move2)
        self.humP2_points += beats(move2, move1)
        self.p1.learn(move1, move2)
        self.humP2.learn(move2, move1)
        self.winner = winner(move1, move2)
        print_slowly(f"""
SCORES: Robot: {self.p1_points}  |  (You): {self.humP2_points}
ROUND KILLER: {self.winner} !!
----------------------------------""")
        return self.winner

    def game_winner(self):
        if self.p1_points > self.humP2_points:
            return "ROBOT"
        elif self.humP2_points > self.p1_points:
            return "HUMAN (YOU)"
        else:
            return "BOTH PLAYERS"

    def play_game(self):
        self.Result = 0
        print_slowly("Welcome to Rock Paper Scissors GAME!")
        print_slowly("Type Starter, Easy, Medium, or Hard to Choose the mode")
        print_slowly("Type Exit to quit")
        print_slowly("Please select a game mode to Begin!")

        lines(1)
        self.p1 = choose_mode("Please type in starter, easy, medium, hard or "
                              "exit."
                              "\nPlease select a mode\n", modes, self.p1)
        if self.p1 == "exit":
            return "exit"

        self.result = []
        for round in range(5):
            print_slowly(f"\nRound {round + 1}:")
            self.result.append(self.play_round())
        print_slowly("Game results:\n")
        i = 1
        for res in self.result:
            print_slowly(f"..round {i} winner: {res}")
            i += 1
        print_slowly(f"Final Scores:\n"
                     f" Robot: {self.p1_points} | Human: {self.humP2_points}")
        print_slowly(f"\n>>> GAME WINNER: {self.game_winner()} <<<")
        return True


# >>>>>>>>>>>>>     MAIN CODE    >>>>>>>>>>>>>>>>>>
if __name__ == '__main__':
    play = True
    while (play):
        game = Game(Player(), HumanPlayer())
        new_page()
        Go_Stop = game.play_game()
        if (Go_Stop == "exit"):
            play = False
            break
        print_slowly("Game finished!\n"
                     "Do you want to play again? (enter y/n)")
        Y_N = enter_this("(enter y/n)", ["y", "Y", "n", "N"])
        if Y_N in ["y", "Y"]:
            pass
        elif Y_N in ["n", "N"]:
            play = False
    print_slowly("Goodbye.")
    lines(1)
