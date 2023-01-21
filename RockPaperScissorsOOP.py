# Rock, Paper Scissors game using OOP


from random import randint


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def user_choice(self):
        pass


class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def user_choice(self):
        choice = input("Rock, Paper, Scissors? ").lower()
        return choice

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def computer_choice(self):
        choice = randint(1, 3)
        if choice == 1:
            return "rock"
        elif choice == 2:
            return "paper"
        else:
            return "scissors"
        

class Game:
    def __init__(self):
        
        self.player1 = Human("Player 1 {self.name}")
        self.player2 = Computer("Computer")

    def find_winner(self, player1, player2):
        if player1 == "rock" and player2 == "scissors":
            return "You!"
        elif player1 == "scissors" and player2 == "paper":
            return "You!"
        elif player1 == "paper" and player2 == "rock":
            return "You!"
        elif player1 == player2:
            return "Tie"
        else:
            return "Computer"
        
    def play_game(self):

        print("Welcome to Rock, Paper, Scissors!")

        self.name = input("What is your name? ")
        print("Hello", self.name)
        print("Let's play!")

        while True:

            player1 = self.player1.user_choice()
            player2 = self.player2.computer_choice()

            print("Computer chose", player2)
            winner = self.find_winner(player1, player2)

            print(winner, "won!")
            if winner == "You!":
                self.player1.score += 1
            elif winner == "Computer":
                self.player2.score += 1

            print("Your score is", self.player1.score)
            print("Computer score is", self.player2.score)
            play_again = input("Would you like to play again? (y/n) ").lower()

            if play_again == "n":

                print("Thanks for playing!")
                print("Your final score is", self.player1.score)
                print("Computer final score is", self.player2.score)

                if self.player1.score > self.player2.score:
                    print("You won!")
                elif self.player1.score < self.player2.score:
                    print("Computer won!")
                else:
                    print("Tie")

                break


game = Game()
game.play_game()
