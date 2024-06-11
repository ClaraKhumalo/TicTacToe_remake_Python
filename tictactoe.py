import random

player_list=["X","O"]
bot_names=["Alicia","Margo","Scott", "Mayson"]
first_player_moves=[]
second_player_moves=[]
first_player_moves_amount=[ ]#5
second_player_moves_amount=[ ]#4
open_space=[]
open_space_copy=[]
change_board=0   
first_player=""
second_player=""
current_player=""
tie_func=""
won=False
tied=False
board_position_number=0
first_board_position_number=0

def game_setup(height):
    """
    Displays The Board of the game
    """

    global board_position_number
    global first_board_position_number

    if first_board_position_number==0:
        print("\nGame Board")
        for row in range(height+1):
            for column in range(height):
                if (row == 0):
                    print("_"*5, end="")
                elif (row != 0) or (row != height-1) or (column != 0) or (column !=  height-1):
                    if change_board==0:
                        board_position_number+=1
                        open_space.append( board_position_number)
                        open_space_copy.append( board_position_number)
                        print(f"|_{ board_position_number}_|", end ="")
                    else:
                        for  board_position_number in open_space:
                            print( board_position_number, end ="")
                else:
                    print(" ", end="")

            print() 
            board_position_number=0 
        print()
        first_board_position_number+=1

    else:
        print("\nGame Board")
        for row in range(height+1):
            for column in range(height):
                if (row == 0):
                    print("_"*5, end="")
                elif (row != 0) or (row != height-1) or (column != 0) or (column !=  height-1):
                    if change_board==0:
                        open_space.append( board_position_number)
                        open_space_copy.append( board_position_number)
                        print(f"|_{ board_position_number}_|", end ="")
                    else:
                        for  board_position_number in open_space:
                            print( board_position_number, end ="")
                else:
                    print(" ", end="")

            print()  
            board_position_number=0
        print()


def variable_assignment_1():                  
    """
    Assigns player title (x or o) based on user player_1 input.
    """    
    global player_1
    player_1=input( "X or O: " ).upper()
    if player_1 not in player_list:
        variable_assignment_1()

    elif player_1 in player_list:
        print("Player 1 is "+player_1)

    elif player_1.lower()=="quit":
        leave()    
    
    else:
        print("Invalid choice.\nTry \"X\" or \"O\"")      
        variable_assignment_1()
    
    return player_1


def variable_assignment_2(player_1):  
    """
    Assigns remaining title (x or o)  to player two.
    """  
    global player_2
    player_2=""  
    for taken in player_list:         
        if not taken==player_1:
            print("Player 2 is "+ taken) 
            player_2=taken

    return player_2   


def spaces_friend_1(player_1, player_2):
    """
    Gets user input for first player.
    """

    print( "choose a number from the list of available spaces: ",str(open_space),"... " )     
    for space in range(len(open_space)): 
        global choice_1
        choice_1=input(player_1+": ")
        if choice_1.isdigit():
            global choice_1b
            choice_1b=int(choice_1) 
            if choice_1b in open_space:
                first_player_moves.append(choice_1b)
                open_space[choice_1b-1]=player_1
                second_player_moves_amount.append(player_1)
                board_position_number=choice_1b
                game_setup(height)
                if won!=True or tied!=True:
                    return spaces_friend_2(player_2)   
                return winnerAssessment()
            elif choice_1.lower()=="quit":
                return  leave()
            elif choice_1b not in open_space:
                print(choice_1b,"is not an available number") 
                return spaces_friend_1(player_1, player_2)  
        elif choice_1=="quit":
            return leave()        
        else: 
            print("invalid input: ", choice_1)     
            return spaces_friend_1(player_1, player_2) 

    return choice_1b
                           

def spaces_friend_2(player_2):
    """
    Gets user input for second player.
    """

    for space in range(len(open_space)): 
        global choice_2
        choice_2=input(player_2+": ")
        if choice_2.isdigit():
            global choice_2b
            choice_2b=int(choice_2)
            if choice_2b in open_space:
                second_player_moves.append(choice_2b)
                open_space[choice_2b-1]=player_2
                first_player_moves_amount.append(player_2)
                board_position_number=choice_2b
                game_setup(height)
                return winnerAssessment()
            elif choice_2.lower()=="quit":
                leave()
            elif choice_2b not in open_space:
                print(choice_2b,"is not an available number") 
                return spaces_friend_2(player_2)  
        elif choice_1=="quit":
            return leave()         
        else:        
            print("invalid input: ", choice_2)  
            return spaces_friend_2(player_2) 
            
    return choice_2b


def loop_friend():
    """
    Prompts user input until there is a winner or there are no more open
    spaces (there is a tie).
    """

    while won==False or tied==False:
        first_choice=spaces_friend_1(first_player, second_player)
        return first_choice


def spaces_bot_friend(player_1):
    """
    Gets user input for first player.
    """

    print( "choose a number from the list of available spaces: ",str(open_space),"... " )     
    for space in range(len(open_space)):  
        global choice_1
        choice_1=input(player_1+" : ")
        if choice_1.isdigit():
            global choice_1b
            choice_1b=int(choice_1)
            if choice_1b in open_space:
                first_player_moves.append(choice_1)
                open_space[choice_1b-1]=player_1 
                open_space_copy.remove(choice_1b) 
                second_player_moves_amount.append(player_1)
                return choice_1b
            elif choice_1.lower()=="quit":
                leave()
            elif choice_1b not in open_space:
                print(choice_1,"is not an available number") 
                spaces_bot_friend(player_1)  
            else: 
                print("invalid input: ", choice_1) 
                spaces_bot_friend(player_1)       
        else: 
            print("invalid input: ", choice_1)  
            spaces_bot_friend(player_1)        
    return int(choice_1)
      

def spaces_bot(player_2):    
    """
    Randomises input for second player (bot).
    """

    for space in range(len(open_space)): 
        global choice_2
        choice_2=random.choice(open_space_copy)
        if choice_2 in open_space:
            choice_2b=int(choice_2)
            second_player_moves.append(choice_2)
            open_space[int(choice_2)-1]=player_2
            open_space_copy.remove(choice_2)
            first_player_moves_amount.append(player_2)
            print( player_2,":",choice_2)
            game_setup(height)
            return choice_2b
        elif choice_2 not in open_space:
            print(choice_2,"is not an available number") 
            spaces_bot(player_2)  
        else:        
            print("invalid input: ", choice_2)  
            spaces_bot(player_2) 

    return choice_2


def loop_bot():
    while won==False or tied==False:
        first_choice=spaces_friend_1(first_player, second_player)
        return first_choice


def winner(): 
    """
    There is winner. 
    Gives player the option to begin a new game or leave the game.
    """  

    global won
    won=True

    global again
    print("Prove that you didnt get lucky and play again.")
    ask_again=input( "\"accept\" or \"decline\"? ").lower()
    if ask_again=="accept":
        print("Let's try again") 
        again=True
        return again
    elif ask_again=="decline":
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

    global tied
    tied=True
    global again
    print("No winner. Try again.")
    ask_again=input( "\"accept\" or \"decline\"? ").lower()
    if ask_again=="accept":
        print("Let's try again")  
        again=True
        return True
    elif ask_again=="decline":
        print("Sad to see you leave. Come back again soon!")  
        again=False  
        return again
    else:
        print("Invalid Input")  
        tie()


def winnerAssessment():
    """
    Asses who the winner is.
    """
    # rows for player_1
    if open_space[0]==open_space[1]==open_space[2]==player_1:
        winner_is=player_1
        print("The winner is",winner_is)
        print("Prove that you didnt get lucky and play again.")
        return winner() 
    elif open_space[3]==open_space[4]==open_space[5]==player_1:
        winner_is=player_1
        print("The winner is",winner_is)
        print("Prove that you didnt get lucky and play again.")
        winner()     
    elif open_space[6]==open_space[7]==open_space[8]==player_1: 
        winner_is=player_1
        print("The winner is",winner_is)
        print("Prove that you didnt get lucky and play again.")
        winner()
    
    # rows for player_2
    elif open_space[0]==open_space[1]==open_space[2]==player_2:
        winner_is=player_2
        print("The winner is",winner_is)
        winner()
    elif open_space[3]==open_space[4]==open_space[5]==player_2:
        winner_is=player_2
        print("The winner is",winner_is)
        winner()
    elif open_space[6]==open_space[7]==open_space[8]==player_2:
        winner_is=player_2
        print("The winner is",winner_is)
        winner()

    # diagonals for player_1
    elif open_space[0]==open_space[4]==open_space[8]==player_1:
        winner_is=player_1
        print("The winner is",winner_is)
        winner()
    elif open_space[2]==open_space[4]==open_space[6]==player_1:
        winner_is=player_1
        print("The winner is",winner_is)
        winner()
    
    # diagonals for player_2
    elif open_space[0]==open_space[4]==open_space[8]==player_2:
        winner_is=player_2
        print("The winner is",winner_is)
        winner()
    elif open_space[2]==open_space[4]==open_space[6]==player_2:
        winner_is=player_2
        print("The winner is",winner_is)
        winner()

    # columns for player_1
    elif open_space[0]==open_space[3]==open_space[6]==player_1:
        winner_is=player_1
        print("The winner is",winner_is)
        winner()
    elif open_space[1]==open_space[4]==open_space[7]==player_1:
        winner_is=player_1
        print("The winner is",winner_is)  
        winner()    
    elif open_space[2]==open_space[5]==open_space[8]==player_1:
        winner_is=player_1
        print("The winner is",winner_is)    
        winner()

    # columns for player_2
    elif open_space[0]==open_space[3]==open_space[6]==player_2:
        winner_is=player_2
        print("The winner is",winner_is)
        winner()
    elif open_space[1]==open_space[4]==open_space[7]==player_2:
        winner_is=player_2
        print("The winner is",winner_is)      
        winner()
    elif open_space[2]==open_space[5]==open_space[8]==player_2:
        winner_is=player_2
        print("The winner is",winner_is)
        winner()         
           
    # tie
    else:
        if len(first_player_moves)==5 and len(second_player_moves)==4:
            tie()
        else:
            if tie_func=="loop_friend":
                loop_friend()
            else:
                loop_bot()    


def leave():
    quit=input("Are you sure you want to leave? All your progress will be lost: Yes or No").lower()
    if quit=="yes":
        again=False
        return again
    if quit=="no":
        print("Returning to game")
        again=True
        return again
    else :
        print("Inavid input")
        return leave()


if __name__ == "__main__":
    height = 3
    open_space = []
    newSpace = open_space.copy
    again = True

    while again:
        partner = input("Play with: \n1. A robot\n or \n2. A friend\n").lower()
        while partner != "1" and partner != "2":
            print("Invalid Input! Please enter the number that corresponds to an available option (i.e. 1 or 2).")
            partner = input("Play with: \n1. A robot\n or \n2. A friend\n").lower()
        game_setup(height)

        if partner == "2":
            tie_func = "loop_friend"
            first_player = variable_assignment_1()
            second_player = variable_assignment_2(first_player)
            loop_friend()
        elif partner == "1":
            print("Great choice! Your playing partner is: ", random.choice(bot_names))
            tie_func = "loop_bot"
            first_player = variable_assignment_1()
            second_player = variable_assignment_2(first_player)
            loop_bot()
        elif partner == "quit":
            leave()
