from random import randint
lower_number,higher_number=1,10
random_number : int = randint(lower_number , higher_number)
print(f' guess the number in the range {lower_number} to {higher_number}')
while True:
    try:
        user_guess : int = int(input('guess: '))
    except ValueError as e:
        print('plese enter the valid number')
        continue

    if user_guess > random_number:
        print('the number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print("you guesses it right")
        break

#adding move limits of 5
from random import randint
lower_number,higher_number=1,10
random_number : int = randint(lower_number , higher_number)
print(f' guess the number in the range {lower_number} to {higher_number}')
limit=0
while limit <5:
    try:
        user_guess : int = int(input('guess: '))
    except ValueError as e:
        print('plese enter the valid number')
        continue

    limit +=1
    if user_guess > random_number:
        print('the number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print("you guessed it right")
        break
        
if limit == 5 and user_guess!=random_number:
    print('you are out of imit the number was',random_number)

