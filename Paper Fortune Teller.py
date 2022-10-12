# Author: Maryam Taj
# Name of program: Paper Fortune Teller
# Description of program: This program in IDLE simulates a paper fortune teller game between the user and the computer. The program allows the user to select a
# colour, number, and another number, upon which the computer reads their fate based on their choices. The user can replay the game, if they so desire.

import time,sys
# Bring in libraries of pre-built code
while True:
    Introduction=print('Double, double toil and trouble. Fire burn and caldron bubble. Welcome, my friend, to the world of mysticism. Let us discover your fortune.')                                                                                                    
    while True:
        Userchoice=input('Choose a colour. "RED", "BLUE", "GREEN", or "YELLOW".')
        # User chooses one of the four given colours
        Colours=['RED','BLUE','GREEN','YELLOW']
        # I created a list that stores all the colours, so instead of writing "if userchoice!= 'Red' and userchoice!='Blue' and userchoice!='Green' and userchoice
        # !='Yellow'", I can just write if userchoice not in Colours
        def IncorrectResponse(x):
                print('Tsk,tsk. You are making me impatient. Remember, respond in uppercase letters and choose from the given options.')
        # I created a function, IncorrectResponse, that prints 'Tsk,tsk....'. This way, I do not have to write the same sentence repeatedly, but I can simply call the
        # function again
        if Userchoice not in Colours:
           IncorrectResponse(Userchoice)
        # if the user types something other than the four options in the Colours list, the 'Tsk,tsk...' statement appears, and they must choose from the four colours
        # again
        else:
            print('You have selected',Userchoice+'.')
        # if the user types one of the four uppercase options, the green statement appears
            Confirmation=input('Print [Y] to confirm your choice, or [N] to change.')
            if Confirmation=='Y':
                print('Excellent!I foresee greatness in your future.')
                for i in range(0,len(Userchoice)):
                    time.sleep(0.5)
                    print(Userchoice[i])   
                break
        # if user confirms their choice and types 'Y', their chosen colour pops up letter by letter, after 0.5 second intervals
            elif Confirmation=='N': 
                print('Try again, but know that this change of heart was pre-ordained.')
        # if user wants to change their choice, the green statement appears and they must choose from the four colours above again
            else:
                print(IncorrectResponse(Userchoice))
        # if user types anything other than 'Y' or 'N', the 'Tsk,tsk..." pops up and they must choose from the four colours above again        

    Length=len(Userchoice)
        # the variable, Length, is equal to the user's colour's length (number of letters)
    def YResponse(x):
        print("Lovely. Let's proceed.")
        for i in range(1, x+1):
            time.sleep(0.5)
            print(i)
        # the function, YResponse, is the new procedure everytime the user confirms their choice. The 'Lovely..' statement appears and the computer counts up to the
        # user's chosen number with 0.5 second intervals
    def NResponse(x):
        print('If you must change, do so, but time is ticking, my friend.')
        # the function, NResponse, is the new procedure everytime the user wants to change their choice. The green statement appears
    def EResponse(x):
        print('No time for mistakes. Try again, quickly!')
        # the function, EResponse, is the new procedure everytime the user types in anything other than 'Y' or 'N'. The green statement appears
    while True:    
        if Length%2==0:
            Userchoice=int(input('Choose a number between 1,2,5 and 6.'))
        # if the user's colour had an even number of letters, they must choose from the following numbers
            ENumbers=[1,2,5,6]
            if Userchoice not in ENumbers:
               IncorrectResponse(Userchoice)
        # if the user types anything outside the ENumbers list, the IncorrectResponse function happens. The 'Tsk,tsk..' statement appears and they must choose from the
        # four numbers again
            else:
                print('You have selected',str(Userchoice)+'.')
        # if the user types in 1,2,5 or 6, the computer repeats their answer to them
                Confirmation=input('Print [Y] to confirm your choice, [N] to change.')
                if Confirmation=='Y':
                    YResponse(Userchoice)
                    break
        # if the user confirms their answer, the YResponse function happens, with the 'Lovely...' statement, and the counting up to the number
                elif Confirmation=='N':
                    NResponse(Userchoice)
        # if the user wants to change their choice, the NResponse function happens, with the 'If you must...' statement, and the user must choose from the four
        # numbers again
                else:
                    EResponse(Userchoice)
        # if the user types anything other than 'Y' or 'N', the EResponse function happens, with the 'No time..' statement, and the user must choose from the four
        # numbers again
        else:
            Userchoice=int(input('Now,choose a number between 3,4,7 and 8.'))
        # if the user's colours had an odd number of letters, the user must choose from the four numbers above
            ONumbers=[3,4,7,8]
            if Userchoice not in ONumbers:
                IncorrectResponse(Userchoice)
        # if the user types anything outside the ONumbers list, the IncorrectResponse function happens. The 'Tsk,tsk..' statement appears and they must choose from the
        # four numbers again 
            else:
                print('You have selected',str(Userchoice)+'.')
        # if the user types in 3,4,7 or 8, the computer repeats their answer to them
                Confirmation=input('Print [Y] to confirm your choice, [N] to change.')
                if Confirmation=='Y':
                    YResponse(Userchoice)
                    break
        # if the user confirms their choice, the YResponse function happens, with the 'Lovely..' statement, and the counting up to the number
                elif Confirmation=='N':
                    NResponse(Userchoice)
        # if the user wants to change their choice, the NResponse function happens, with the 'If you must...' statement, and the user must choose from the four
        # numbers again
                else:
                    EResponse(Userchoice)
        # if the user types in anything other than 'Y' or 'N', the EResponse function happens, with the 'No time..' statement, and the user must choose from the four
        # numbers again

    if int(Userchoice)%2==0:
        Userchoice=int(input('Last step before you discover your fate. Pick another number between 1,2,5 and 6.'))
        EFortunes={1:'when the ground turns liquid, the false leader shall bring an age of anarchy and the rise of mankind.',2:'once the mark of the one becomes \
                the mark of many, a secret meeting shall bring new aggressions.',5:'when the day is longest, your young one shall cause a reunion of friends.',6:\
                'once the dark one returns, children of darkness shall bring an aeon of fortune.'}
        # If the user's chosen number was even, they choose from 1,2,5 and 6. Each number has a corresponding fortune
        print('Your fortune reads,', EFortunes[Userchoice])
        # the computer reads the number's corresponding fortune to the user
    else:
        Userchoice=int(input("We're almost there. Pick another number between 3,4,7, and 8."))
        OFortunes={3:'upon the day lightning strikes twice, a proposition shall bring forth an era of sorrow.',4:'upon the day when the shrouded is revealed,\
                a woman of grey shall cause a strengthening of bonds and an age of failing crops.',7:'when air turns to fire, the foreign one shall bring a country\
                doom.',8:'when the brother becomes the father, a man clad in green shall mark an age of justice and an era of favorable crop yields.'}
        # if the user's chosen number was odd, they choose from 3,4,7 and 8. Each number has a corresponding fortune
        print('Your fortune reads,',OFortunes[Userchoice])
        # the computer reads the number's corresponding fortune to the user

    while True:
        Replay=input('Would you like to read your fortune again? Type [Y] to begin the process again, or [N] to leave.')
        if Replay=='Y':
            print('Very well.')
            break
        # if the user types 'Y' to play the game again, the game restarts from the beginning
        elif Replay=='N':
            print('Farewell, then, and heed my words. Those who ignore, repent.')
            sys.exit()
        # if the user types 'N' to end the game, the game ends
        else:
            print('Speak louder, my friend.')
        # if the user types anything other than 'Y' or 'N', the 'Speak...' statement appears and the user must answer the 'Would you like...' question again
 
        
        
    

    
          
