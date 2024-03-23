import random

def roll_dice(amount):
    if amount <= 0:
        raise ValueError("Number of dice must be greater than 0")
    rolls = []
    for _ in range(amount):
        random_roll = random.randint(1, 6)
        rolls.append(random_roll)
    return rolls

def sum_dice(rolls):
    return sum(rolls)

def main():
    while True:
        try:
            user_input = input("how many dice would you like to roll: ")
            
            if user_input.lower() == 'exit':
                print('Thanks for playing with us')
                break
            
            amount = int(user_input)
            dice_rolls = roll_dice(amount)
            print(f"Rolls: {', '.join(map(str, dice_rolls))}")
            print(f"Sum: {sum_dice(dice_rolls)}")
        except ValueError:
            print('(please enter a valid number)')

main()
print("....")

