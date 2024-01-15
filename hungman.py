from random import choice 
def run_game():
    word : str = choice(['apple' , 'secret' , 'banana'])
    username: str = input('what is you name? >>')
    print(f'welcome to hangman {username}')

    #logic
    guessed : str =''
    tries : int = 3

    #the main game logic
    while tries > 0 :
        blanks : int =0
        print('word:',end='')
        for char in word:
            if char in guessed:
                print(char,end='')
            else:
                print('_',end='')
                blanks+=1
    print() # blank line

    if blanks==0:
        print("you got it!")
        break




