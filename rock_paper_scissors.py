import random
import sys

# Game: Rock, Paper, Scissors
class RPS:
    def __init__(self):
        self.moves = {'rock': '🧱', 'paper': '📜', 'scissors': '✂'}
        self.valid_move = list(self.moves.keys())
        self.user_score = 0
        self.ai_score = 0
        self.tie_score = 0
        print('Welcome to Rock, Paper, Scissors')

    def play_game(self):
        user_move = input('Rock, Paper, Scissors (or type "exit" to quit)>>> ').lower()

        if user_move == 'exit':
            self.display_scores()
            print('Thanks for playing!')
            sys.exit()
        if user_move not in self.valid_move:
            print('Invalid move...')
            return self.play_game()

        ai_move = random.choice(self.valid_move)
        self.display_moves(user_move, ai_move)
        result = self.check_moves(user_move, ai_move)
        self.update_scores(result)
        self.display_scores()

    def display_moves(self, user_move, ai_move):
        print("-------")
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]} ')
        print("-------")

    def check_moves(self, user_move, ai_move):
        if user_move == ai_move:
            print("It's a tie!")
            return 'tie'
        elif (
            (user_move == 'rock' and ai_move == 'scissors') or
            (user_move == 'scissors' and ai_move == 'paper') or
            (user_move == 'paper' and ai_move == 'rock')
        ):
            print("You win!")
            return 'win'
        else:
            print("AI wins!")
            return 'lose'

    def update_scores(self, result):
        if result == 'win':
            self.user_score += 1
        elif result == 'lose':
            self.ai_score += 1
        elif result == 'tie':
            self.tie_score += 1

    def display_scores(self):
        print("Scores:")
        print(f'You win: {self.user_score} | AI wins: {self.ai_score} | Ties: {self.tie_score}')

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()        
