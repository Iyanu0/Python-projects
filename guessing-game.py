import random



score_list=list()

while True:

    welcome='\nWelcome to this Guessing Game\n\n'

    menu='Select a menu option'

    options='Select an option \n(a) Play\n(b) Scoreboard\n(c) Exit'

    print(welcome,menu,options)
    
    option_input=input('\nPick an option A, B or C: ')

    inp=option_input.lower()

    if inp==('a'):
        
        names=input('\nEnter your name: ')

        counts=dict()
        n=0
        while True and n< 10:
            if names not in counts:
                counts[names]=1
            else:
                counts[names]+=1
            try:
                inp=int(input('Enter a number: '))
            except:
                print('Enter a valid integer!')
            else:
                rand_guess=random.randint(0,30)

                if inp ==rand_guess:
                    print('Correct Guess\n You WIN!')
                    break
                else:
                    print('Wrong Guess\n Try Again')

            n+=1

        print('\nAttempt Inf:\n',counts)


        for key, val in counts.items():
            score_list.append((val,key))

        if len(score_list) >10:break

        score_list.sort(reverse=False)
    
        highscore=score_list[0]

        print('Highscore: ',highscore)
            
                
        scoreboard=open('scores.txt','w')

        scoreboard.write('\nScoreboard:\n' +str(score_list) + ' \n')

        scoreboard.close()

       
        

    elif inp==('b'):
        

        scoreboard=open('scores.txt','r')

        for line in scoreboard:
            print (line,'\n')
        
        

    elif inp==('c'):
        print('\nThanks for Playing this Guessing Game\nExiting.....')
        break

    else:
        print('Enter a valid input')
