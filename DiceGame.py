import random


class DiceGame:

    def __init__(self):
        self.total_rolls = 0

    # Roll two dice and return the results.
    def roll_dice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1, dice2

    # Get and validate user input.
    def get_user_input(self):
        while True:
            choice = input("Roll the dice? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
                continue

    # Display the dice roll results with additional information.
    def display_roll(self, dice1, dice2):

        total = dice1 + dice2
        self.total_rolls += 1

        print(f"🎲 Roll #{self.total_rolls}: ({dice1}, {dice2}) = {total}")

    # Main game loop.
    def play(self):

        print("🎲 Welcome to the Dice Rolling Game! 🎲")
        print("Roll two dice and see what you get!")

        while True:
            if self.get_user_input():
                dice1, dice2 = self.roll_dice()
                self.display_roll(dice1, dice2)
            else:
                break

        print("Thanks for playing! 👋")


# Usage examples
if __name__ == "__main__":
    # Using the class-based approach
    game = DiceGame()
    game.play()

'''  def dice_rolling_game():
        proceed = ''
        while proceed != 'n':
            proceed = input("Roll the dice? (y/n) : ")

            if proceed == 'y':
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                print(f"({dice1}, {dice2})")
            elif proceed == 'n':
                return ("Thank you for playing")
                break
            else:
                proceed = ''
                print("Try again, enter y or n Only")
                continue

    print(dice_rolling_game())'''
