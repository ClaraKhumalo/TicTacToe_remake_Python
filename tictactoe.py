import random

screen_width=300
screen_height=300
white=(255,255,255)
line_color=(0,0,0)
height=5

player_List=["X","O"]
botnames=["Alicia","Margo","Scott", "Mayson"]
moves1=[]
moves2=[]
amount1=[ ]#5
amount2=[ ]#4
open_Space=[]
open_Space_copy=[]
change_board=0   
firstplayer=""
secondplayer=""
again=True


def Partner():
    partner=input("Play with \"bot\" or a \"friend\": ").lower()
    return partner


def gameSetup(height,   partner):
    
    if  partner=="friend"  : 
        i=0
        for row in range(height):
            for column in range(height):
                if (row == 0) or (row == height-1) or (column == 0) or (column ==  height-1):
                    print("*", end="")
                else:
                    if change_board==0:
                        i+=1
                        open_Space.append(i)
                        print(i, end ="")
                    else:
                        for i in open_Space:
                            print(i, end ="")

            print()            

    elif    partner=="bot" or  partner == "robot":
        print("Great choice! You are playing    partner: ", random.choice(botnames))
        i=0
        for row in range(height):
            for column in range(height):
                if (row == 0) or (row == height-1) or (column == 0) or (column ==  height-1):
                    print("*", end="")
                else:
                    if change_board==0:
                        i+=1
                        open_Space.append(i)
                        open_Space_copy.append(i)
                        print(i, end ="")
                    else:
                        for i in open_Space:
                            print(i, end ="")     

    elif partner=="quit":
        leave()
    
    # else:
    #     print("Invalid choice.\nTry \"bot\" or \"friend\"")    
    #     return gameSetup(height   partner)

    return  partner    


def variableAssignment1():                      
    global player1
    player1=input( "X or O: " ).upper()
    if player1 not in player_List:
        variableAssignment1()

    elif player1 in player_List:
        print("Player 1 is "+player1)

    elif player1.lower()=="quit":
        quit()    
    
    else:
        print("Invalid choice.\nTry \"X\" or \"O\"")      
        variableAssignment1()
    
    return player1


def variableAssignment2(player1):  
    global player2
    player2=""  
    for taken in player_List:         
        if not taken==player1:
            print("Player 2 is "+ taken) 
            player2=taken


    return player2   


def spacesFriend1(player1):
    # global change_board
    # change_board+=1
    print( "choose a number from the list of available spaces: ",str(open_Space),"... " )     
    for space in range(len(open_Space)): 
        global choice1
        choice1=input(player1+": ")
        if choice1.isdigit():
            global choice1b
            choice1b=int(choice1) 
            if choice1b in open_Space:
                moves1.append(choice1b)
                open_Space[choice1b-1]=player1
                amount1.append(player1)
                return choice1b
            elif choice1.lower()=="quit":
                return quit()
            elif choice1b not in open_Space:
                print(choice1b,"is not an available number") 
                return spacesFriend1(player1)  
        else: 
            print("invalid input: ", choice1)     
            return spacesFriend1(player1) 

    return int(choice1)
                           

def spacesFriend2(player2):
    for space in range(len(open_Space)): 
        global choice2
        choice2=input(player2+": ")
        if choice2.isdigit():
            global choice2b
            choice2b=int(choice2)
            if choice2b in open_Space:
                moves2.append(choice2b)
                open_Space[choice2b-1]=player2
                amount2.append(player2)
                return loopFriend()
            elif choice2.lower()=="quit":
                quit()
            elif choice2b not in open_Space:
                print(choice2b,"is not an available number") 
                spacesFriend2(player2)  
        else:        
            print("invalid input: ", choice2)  
            spacesFriend2(player2) 
            
    return int(choice2)


def loopFriend():
    while  len(moves1)<6 and len(moves2)<5:
        firstchoice=spacesFriend1(firstplayer)
        if len(moves1)<5:
            secondchoice= spacesFriend2(secondplayer)
            # else:
            #     print("invalid input")
            #     secondchoice= spacesFriend2(secondplayer)     
        elif ( firstchoice=="quit"):
            leave()
        elif len(moves1)==5 and len(moves2)==4:
            print("Winner assessment... ")
            return winnerAssessment()
        else:
            print("invalid input")
            loopFriend()        
    else:
        return False

def spacesBotFriend(player1):
    print( "choose a number from the list of available spaces: ",str(open_Space),"... " )     
    for space in range(len(open_Space)):  
        global choice1
        choice1=input(player1+" : ")
        if choice1.isdigit():
            global choice1b
            choice1b=int(choice1)
            if choice1b in open_Space:
                moves1.append(choice1)
                open_Space[choice1b-1]=player1 
                open_Space_copy.remove(choice1b) 
                amount1.append(player1)
                return choice1
            elif choice1.lower()=="quit":
                quit()
            elif choice1b not in open_Space:
                print(choice1,"is not an available number") 
                spacesBot(player1)  
            else: 
                print("invalid input: ", choice1) 
                spacesBot(player1)       
        else: 
            print("invalid input: ", choice1)  
            spacesBot(player1)        
    return int( choice1)
      

def spacesBot(player2):    
    for space in range(len(open_Space)): 
        global choice2
        choice2=random.choice(open_Space_copy)
        if choice2 in open_Space:
            moves2.append(choice2)
            open_Space[int(choice2)-1]=player2
            open_Space_copy.remove(choice2)
            amount2.append(player2)
            print( player2,":",choice2)
            return loopBot()
        elif choice2 not in open_Space:
            print(choice2,"is not an available number") 
            spacesFriend2(player2)  
        else:        
            print("invalid input: ", choice2)  
            spacesFriend2(player2) 

    return choice2


def loopBot():
    while len(moves1)<6 and len(moves2)<5:
        firstchoice=spacesBotFriend(firstplayer)
        if not ( firstchoice=="quit") and len(moves1)!=5:
            secondchoice=spacesBot(secondplayer)
        if ( firstchoice=="quit"):
            return leave()
        elif len(moves1)==5 and len(moves2)==4:
            print("Winner assessment... ")
            return winnerAssessment()
        else:
            print("invalid input")
            return loopBot()
    else:
        return False


def winner():    
    """
    There is winner. 
    Gives player the option to begin a new game or leave the game.
    """  
    global askagain
    print("Prove that you didnt get lucky and play again.")
    askagain=input( "\"accept\" or \"decline\"? ").lower()
    if askagain=="accept":
        again=True
        return again
    elif askagain=="decline":
        print("Sad to see you leave. Come back again soon!")  
        again=False  
        return again
    else:
        print("Invalid Input")    
        winner()


def tie():
    """
    There is no winner. The game resulted in a tie.
    """
    global askagain
    askagain=input("No winner. Try again.\n \"accept\" or \"decline\"? ").lower()
    if askagain=="accept":
        print("Let's try again")  
        again=True
        # return again
    elif askagain=="decline":
        print("Sad to see you leave. Come back again soon!")  
        again=False  
        # return again
    else:
        print("Invalid Input")  
        tie()


def winnerAssessment():
    """
    Asses who the winner is.
    """
    # rows for player1
    if open_Space[0]==open_Space[1]==open_Space[2]==player1:
        winnerIs=player1
        print("The winner is",winnerIs)
        print("Prove that you didnt get lucky and play again.")
        winner() 
    elif open_Space[3]==open_Space[4]==open_Space[5]==player1:
        winnerIs=player1
        print("The winner is",winnerIs)
        print("Prove that you didnt get lucky and play again.")
        winner()     
    elif open_Space[6]==open_Space[7]==open_Space[8]==player1: 
        winnerIs=player1
        print("The winner is",winnerIs)
        print("Prove that you didnt get lucky and play again.")
        winner()
    
    # rows for player2
    elif open_Space[0]==open_Space[1]==open_Space[2]==player2:
        winnerIs=player2
        print("The winner is",winnerIs)
        winner()
    elif open_Space[3]==open_Space[4]==open_Space[5]==player2:
        winnerIs=player2
        print("The winner is",winnerIs)
        winner()
    elif open_Space[6]==open_Space[7]==open_Space[8]==player2:
        winnerIs=player2
        print("The winner is",winnerIs)
        winner()

    # diagonals for player1
    elif open_Space[0]==open_Space[4]==open_Space[8]==player1:
        winnerIs=player1
        print("The winner is",winnerIs)
        winner()
    elif open_Space[2]==open_Space[4]==open_Space[6]==player1:
        winnerIs=player1
        print("The winner is",winnerIs)
        winner()
    
    # diagonals for player2
    elif open_Space[0]==open_Space[4]==open_Space[8]==player1:
        winnerIs=player2
        print("The winner is",winnerIs)
        winner()
    elif open_Space[2]==open_Space[4]==open_Space[6]==player1:
        winnerIs=player2
        print("The winner is",winnerIs)
        winner()

    # columns for player1
    elif open_Space[0]==open_Space[3]==open_Space[6]==player1:
        winnerIs=player1
        print("The winner is",winnerIs)
        winner()
    elif open_Space[1]==open_Space[4]==open_Space[7]==player1:
        winnerIs=player1
        print("The winner is",winnerIs)  
        winner()    
    elif open_Space[2]==open_Space[5]==open_Space[8]==player1:
        winnerIs=player1
        print("The winner is",winnerIs)    
        winner()

    # columns for player2
    elif open_Space[0]==open_Space[3]==open_Space[6]==player1:
        winnerIs=player2
        print("The winner is",winnerIs)
        winner()
    elif open_Space[1]==open_Space[4]==open_Space[7]==player1:
        winnerIs=player2
        print("The winner is",winnerIs)      
        winner()
    elif open_Space[2]==open_Space[5]==open_Space[8]==player1:
        winnerIs=player2
        print("The winner is",winnerIs)
        winner()         
           
    # tie
    else:
        tie()


def leave():
    quit=input("Are you sure you want to leave? All your progress will be lost: Yes or No").lower()
    if quit=="yes":
        again=False
    if quit=="no":
        print("Returning to game")
        again=True
    else :
        print("Inavid input")
        leave()


if __name__=="__main__":
   
    open_Space=[]
    newSpace=open_Space.copy
    partner=input("Play partner \"bot\" or a \"friend\": ").lower()


    while again==True:

        gameSetup(height,   partner)
        if  partner=="friend":
            firstplayer =variableAssignment1()
            secondplayer=variableAssignment2(firstplayer)
            loopFriend()

        elif  partner=="bot":
            firstplayer =variableAssignment1()
            secondplayer=variableAssignment2(firstplayer)
            loopBot()

        elif    partner=="quit":
            leave()

        else:
            Partner()

        break    
