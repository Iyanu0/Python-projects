#import secrets

#try:
#    inp1=int(input('How many passwords do you want: '))
#    inp2=int(input('What password length do you want: '))

#except:
#    print('Enter a valid input')
#else:
 #   n=0

  #  while n < inp1: 
   #     print(secrets.token_hex(inp1))
    #    n+=1

#alternative method

import random
try:
    inp1=int(input('How many passwords do you want: '))
    inp2=int(input('What password length do you want: '))
except:
    print('Enter a valid input')

else:
    chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+-,./'

    for pwd in range(inp1):
        passwords=''
        for c in range(inp2):
            passwords+=random.choice(chars)

        print(passwords)