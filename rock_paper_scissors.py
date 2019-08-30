import random


moves = ['rock', 'paper', 'scissors']


def beats(one, two):
    if one == two:
        return 'tie'
    else:
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class Player:
    score = 0

    def __init__(self):
        self.my_move = random.choice(moves)
        self.their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, Paper, or Scissors?\n").lower()
            if move in moves:
                return move
            print("I don't know what that means")


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == moves[0]:
            return moves[1]
        elif self.my_move == moves[1]:
            return moves[2]
        else:
            return moves[0]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) == 'tie':
            print("It's a tie!")
        if beats(move1, move2) is True:
            print("Player 1 Wins!")
            self.p1.score += 1
        if beats(move1, move2) is False:
            print("Player 2 Wins!")
            self.p2.score += 1
        print(f"Player 1: {self.p1.score}  Player 2: {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        round = 1
        print("Game start! First to 3 wins!")
        while True:
            print(f"Round {round}:")
            self.play_round()
            if self.p1.score == 3:
                print("Player 1 won the game!")
                break
            elif self.p2.score == 3:
                print("Player 2 won the game!")
                break
            round = round + 1


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
