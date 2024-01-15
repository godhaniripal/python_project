import random , sys
print('ROCK , PAPER , SCISSORS')
print("....................................")
#RESULT TRACKER
wins = 0
losses= 0
ties = 0
while True:
    print('%s wins , %s looses , %s ties' %(wins,losses,ties))
    while True:
        print('enter your move :(r)ock (p)aper (s)cissor or (q)uit')
        playermove=input()
        if playermove == 'q':
            sys.exit()
        if playermove =='r' or playermove == 'p' or playermove =='s' :
            break
        print('type one of r,p,s, or q.')
    #displaying what player have chose
    if playermove == 'r':
        print('rock versus...')
    elif playermove == 'p':
        print('paper versus...')
    elif playermove == 's':
        print('scissor versus...')
    #displaying what comp have chose 
    randomnumber=random.randint(1,3)
    if randomnumber ==1:
        computermove ='r'
        print("rock")
    elif randomnumber ==2:
        computermove ='p'
        print('paper')
    elif randomnumber == 3:
        computermove = 's'
        print('scissor')
    #display and record the win/loss/tie:
    if playermove == computermove:
        print('It is tie!')
        ties = ties + 1
    elif playermove == 'r' and computermove == 's':
        print('you win !')
        wins = wins + 1
    elif playermove == 'p' and computermove == 'r':
        print('you win !')
        wins = wins + 1
    elif playermove == 's' and computermove == 'p':
        print('you win !')
        wins = wins + 1
    elif playermove == 'r' and computermove == 'p':
        print('you lose !')
        losses = losses + 1
    elif playermove == 'p' and computermove == 's':
        print('you lose !')
        losses = losses + 1
    elif playermove == 's' and computermove == 'r':
        print('you lose!')
        losses = losses + 1
