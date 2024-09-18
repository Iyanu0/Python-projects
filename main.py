import random   

highscore=[]

leaderboard=[]
while True:

    welcome='\nWelcome to this Guessing Game\n\n'

    menu='Select a menu option'

    options='Select an option \n(a) Play\n(b) Scoreboard\n(c) Exit'

    print(welcome,menu,options)

    
    option_input=str(input('\nSelect an option--->'))
    
   

    low_inp=option_input.lower()


    lst=dict()

    

    if low_inp.startswith('exit'):#exit option
            break

    elif low_inp.startswith('play'):#play option
            
        try:
            name_input=str(input('Enter your name:'))

        except:
            print('Enter a string of words and numbers')
            attempt=0

            exit_code=0     

            while True and attempt < 10: #guess logic

                if name_input not in lst:
                    lst[name_input] = 1
                else:
                    lst[name_input] +=1

                try:
                    inp=int(input('Enter a number: '))
                except:
                    print('Enter a valid number from 0-30')
                else:
                    rand_guess=2 # replace 2 with random.randint(0,30)
                        
                    if inp == rand_guess:

                        print('Correct guess\n You WIN!')

                        break
                            
                    else:
                        print('Wrong guess')

                attempt +=1

            
            

            print('Attempt Info: \n',lst)




    elif low_inp.startswith('scoreboard'):#scoreboard ooption



        highscores=open('highscore.txt', 'r')

    
        for lines in highscores:

            print(lines,'\n')

             

    else:
            print('Enter a valid input \n')
      
print('\nExiting....')        
        


            




