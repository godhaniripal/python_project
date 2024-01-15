import random
secretnumber = random.randint(1,10)
print('i am thinking of a number between 1 to 10')
#asking player toguess 6 times.
for guessestaken in range(1,7):
    print('take a guess.')
    guess=int(input())
    if guess < secretnumber:
        print("your guess is too low try again you can")
    elif guess > secretnumber:
        print('your guess is too high try again you can still')
    else:
        break
if guess == secretnumber:
    print('good job! you guessed my number in ' + str(guessestaken) + ' guesses! ')
else:
    print('nope. the number i was thinking of was' + str(secretnumber))