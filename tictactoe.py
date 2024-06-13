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
move=""
move1="1"
move2="2"
move3="3"
move4="4"
move5="5"
move6="6"
move7="7"
move8="8"
move9="9"
current_method=""



def game_setup_update():
    """
    Displays the updated Board game after each turn
    """
    global move1 
    global move2 
    global move3 
    global move4
    global move5
    global move6
    global move7
    global move8 
    global move9 
    global open_space
    open_space=[]
    
    print("\nGame Board")
    if move1 in first_player_moves:
        move1=first_player
    elif move2 in first_player_moves:
        move2=first_player
    elif move3 in first_player_moves:
        move3=first_player
    elif move4 in first_player_moves:
        move4=first_player
    elif move5 in first_player_moves:
        move5=first_player
    elif move6 in first_player_moves:
        move6=first_player
    elif move7 in first_player_moves:
        move7=first_player
    elif move8 in first_player_moves:
        move8=first_player
    elif move9 in first_player_moves:
        move9=first_player
    elif move1 in second_player_moves:
        move1=second_player
    elif move2 in second_player_moves:
        move2=second_player
    elif move3 in second_player_moves:
        move3=second_player
    elif move4 in second_player_moves:
        move4=second_player
    elif move5 in second_player_moves:
        move5=second_player
    elif move6 in second_player_moves:
        move6=second_player
    elif move7 in second_player_moves:
        move7=second_player
    elif move8 in second_player_moves:
        move8=second_player
    elif move9 in second_player_moves:
        move9=second_player
    open_space.append(move1)
    open_space.append(move2)
    open_space.append(move3)
    open_space.append(move4)
    open_space.append(move5)
    open_space.append(move6)
    open_space.append(move7)
    open_space.append(move8)
    open_space.append(move9)

    print(f"|_{move1}_|", end ="")
    print(f"|_{move2}_|", end ="")
    print(f"|_{move3}_|")
    print(f"|_{move4}_|", end ="")
    print(f"|_{move5}_|", end ="")
    print(f"|_{move6}_|")
    print(f"|_{move7}_|", end ="")
    print(f"|_{move8}_|", end ="")
    print(f"|_{move9}_|\n", end ="")
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


def spaces_friend_1(player_1):
    """
    Gets user input for first player.
    """
    global current_method
    for space in range(len(open_space)): 
        choice_1=input(player_1+": ")
        if choice_1.isdigit():
            choice_1b=int(choice_1) 
            if choice_1 in open_space:
                first_player_moves.append(choice_1)
                open_space[choice_1b-1]=player_1
                first_player_moves_amount.append(player_1)
                current_method="spaces_friend_1"
                return choice_1
            elif choice_1.lower()=="quit":
                return  leave()
            elif choice_1 not in open_space:
                print(choice_1b,"is not an available number") 
                return spaces_friend_1(player_1)  
        elif choice_1=="quit":
            return leave()        
        else: 
            print("Invalid Input: ", choice_1)     
            return spaces_friend_1(player_1) 
    return choice_1b
                           

def spaces_friend_2(player_2):
    """
    Gets user input for second player.
    """
    global current_method

    for space in range(len(open_space)): 
        choice_2=input(player_2+": ")
        if choice_2.isdigit():
            choice_2b=int(choice_2)
            if choice_2 in open_space:
                second_player_moves.append(choice_2)
                open_space[choice_2b-1]=player_2
                second_player_moves_amount.append(player_2)
                current_method="spaces_friend_2"
                return choice_2
            elif choice_2.lower()=="quit":
                leave()
            elif choice_2 not in open_space:
                print(choice_2b,"is not an available number") 
                return spaces_friend_2(player_2)  
        elif choice_1=="quit":
            return leave()         
        else:        
            print("Invalid Input: ", choice_2)  
            return spaces_friend_2(player_2)             
    return choice_2b


def loop_friend(first_player, second_player):
    """
    Prompts user input until there is a winner or there are no more open
    spaces (there is a tie).
    """

    while won==False or tied==False:
        game_setup_update()
        print( "choose a number from the list of available spaces: ",str(open_space),"... " )     
        spaces_friend_1(first_player)
        winnerAssessment()
        game_setup_update()
        print( "choose a number from the list of available spaces: ",str(open_space),"... " )     
        spaces_friend_2(second_player)
        winnerAssessment()


def spaces_bot_friend(player_1, player_2):
    """
    Gets user input for first player.
    """
    global current_method

    for space in range(len(open_space)):  
        global choice_1
        choice_1=input(player_1+" : ")
        if choice_1.isdigit():
            global choice_1b
            choice_1b=int(choice_1)
            if choice_1 in open_space:
                first_player_moves.append(choice_1)
                open_space[choice_1b-1]=player_1 
                open_space_copy.remove(choice_1) 
                first_player_moves_amount.append(player_1)
                return choice_1
            elif choice_1.lower()=="quit":
                leave()
            elif choice_1 not in open_space:
                print(choice_1,"is not an available number") 
                spaces_bot_friend(player_1, player_2)  
            else: 
                print("invalid input: ", choice_1) 
                spaces_bot_friend(player_1, player_2)       
        else: 
            print("Invalid Input: ", choice_1)  
            spaces_bot_friend(player_1, player_2)        
    return int(choice_1)
      

def spaces_bot(player_2):    
    """
    Randomises input for second player (bot).
    """
    global current_method
    global open_space_copy

    for space in range(len(open_space)): 
        global choice_2
        choice_2=random.choice(open_space_copy)
        if choice_2 in open_space:
            choice_2b=int(choice_2)
            second_player_moves.append(choice_2)
            open_space[choice_2b-1]=player_2
            open_space_copy.remove(choice_2)
            first_player_moves_amount.append(player_2)
            print( player_2,":",choice_2)
            current_method="spaces_bot"
            return choice_2b
        elif choice_2 not in open_space:
            print(choice_2,"is not an available number") 
            spaces_bot(player_2)  
        else:        
            print("Invalid Input: ", choice_2)  
            spaces_bot(player_2) 

    return choice_2



def loop_bot(first_player, second_player):
    """
    Prompts user input until there is a winner or there are no more open
    spaces (there is a tie).
    """

    while won==False or tied==False:
        game_setup_update()
        print( "choose a number from the list of available spaces: ",str(open_space),"... " )     
        spaces_bot_friend(player_1, player_2)        
        winnerAssessment()
        game_setup_update()
        print( "choose a number from the list of available spaces: ",str(open_space),"... " )     
        spaces_bot(player_2)
        winnerAssessment()


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
        reset()
        return again
    elif ask_again=="decline":
        print("Sad to see you leave. Come back again soon!")  
        again=False  
        return again
    else:
        print("Invalid Input: ",ask_again)  
        winner()

def reset():
    global move
    global move1  
    global move2 
    global move3 
    global move4
    global move5
    global move6
    global move7
    global move8 
    global move9 
    global open_space
    global current_method
    global again

    open_space=[]
    move=""
    move1="1"
    move2="2"
    move3="3"
    move4="4"
    move5="5"
    move6="6"
    move7="7"
    move8="8"
    move9="9"
    current_method=""
    again=True

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
        reset()
        return True
    elif ask_again=="decline":
        print("Sad to see you leave. Come back again soon!")  
        again=False  
        return again
    else:
        print("Invalid Input: ", ask_again)  
        tie()


def winnerAssessment():
    """
    Asses who the winner is.
    """
    # rows for player_1
    if open_space[0]==open_space[1]==open_space[2]==player_1:
        winner_is=player_1
        print("The winner is",winner_is)
        print("Prove that it wasn't just luck and play again.")
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
    open_space = []
    open_space_copy=["1","2","3","4","5","6","7","8","9"]
    again = True
    current_method=""

    while again:
        partner = input("Play with: \n1. A robot\n or \n2. A friend\n").lower()
        while partner != "1" and partner != "2":
            print("Invalid Input! Please enter the number that corresponds to an available option (i.e. 1 or 2).")
            partner = input("Play with: \n1. A robot\n or \n2. A friend\n").lower()
        game_setup_update()

        if partner == "2":
            tie_func = "loop_friend"
            first_player = variable_assignment_1()
            second_player = variable_assignment_2(first_player)
            loop_friend(first_player, second_player)
        elif partner == "1":
            print("Great choice! Your playing partner is: ", random.choice(bot_names))
            tie_func = "loop_bot"
            first_player = variable_assignment_1()
            second_player = variable_assignment_2(first_player)
            loop_bot(first_player, second_player)
        elif partner == "quit":
            leave()