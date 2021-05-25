'''
        This is the code for "Kaleb's garbage version of 'Command-line Slapjack'"
        Date Completed: May 1, 2020

'''
# IMPORTED MODULES

import random
import keyboard     # Installed using 'pip install keyboard' from the command line
import time

# CREATED FUNCTIONS

def display_disclaimer():
    disclaimer_header = print("DISCLAIMER".center(115))
    disclaimer_msg = '''
    -   If you have NOT played Slapjack before, before playing this, I strongly recommend you to
        'Google' how to play the game.
    '''
    return disclaimer_header, print(disclaimer_msg)

def display_rules_and_controls():
    rules_header = print("RULES".center(115))
    rule_msg = print('''
    1. You are the player and you will be playing against the CPU, or computer.
    2. Once you and the CPU places each of your top cards into the center, a play is performed,
    whether you/the CPU choose to slap or not slap either card.
    3. After 5 plays, a round will be complete and the player's and the CPU'S score will be displayed.
    4. And after 4 rounds, the game will finish and will display the winner!
    \n
    ''')
    time.sleep(10)
    controls_header = print("CONTROLS".center(115))
    controls_msg = print('''
    1.  Press and hold 's' on the keyboard, for about three seconds, to slap a card.
    2.  The rest of the required controls will appear on the screen when prompting you to enter them!
    
    *WARNING*: After holding 's', you will have to delete the characters when prompted to enter a new control.
    ''')
    time.sleep(8)
    return rules_header, rule_msg, controls_header, controls_msg

def buildandshuffledeck():
    CARDFACES = []
    ROYALCARDS = ["JACK","KING","QUEEN","ACE"]
    NUMCARDS = ["2","3","4","5","6","7","8","9","10"]
    SUITS = ["DIAMONDS","CLUBS","SPADES","HEARTS"]
    INIT_DECK = []

    for cardnum in range(len(NUMCARDS)):
        CARDFACES.append(NUMCARDS[cardnum])

    for royalcard in range(len(ROYALCARDS)):
        CARDFACES.append(ROYALCARDS[royalcard])

    for suit in range(len(SUITS)):
        for numcard in range(13):
            cardlabel = f"{CARDFACES[numcard]} of {SUITS[suit]}"
            INIT_DECK.append(cardlabel)
    random.shuffle(INIT_DECK)
    return INIT_DECK

def splitdeck(init_deck):
    split_deck_len = len(init_deck) // 2
    PLAYER_DECK = init_deck[:split_deck_len]
    CPU_DECK = init_deck[split_deck_len:]
    return PLAYER_DECK, CPU_DECK

def showcard(user_deck):
    playedcard = user_deck.pop(0)
    return playedcard

def addcardtopile(user_card):
    playedpile = []
    playedpile.append(user_card)
    return playedpile

def slapcard(user_played_Card, played_pile, player_deck, cpu_deck): 
    if (keyboard.is_pressed("s") and user_played_Card.startswith("JACK")):
        for playedcards in played_pile:
            player_deck.append(playedcards)
        print("Great Job! You slapped a jack.\n")
        time_buffer = time.sleep(2.75)
        print(f"Now you have {len(player_deck)} card(s)!")
        time_buffer = time.sleep(2.85)


    elif (keyboard.is_pressed("s") and not(user_played_Card.startswith("JACK"))):
        slapped_card = user_played_Card
        print("Womp, womp! You (Player) slapped the wrong card!")
        time_buffer = time.sleep(2.75)
        print("Your next top card will now be given, face down, to the 'CPU'.")
        time_buffer = time.sleep(2.5)
        cpu_deck.append(player_deck[0])
        print(f"Now you have {len(player_deck)} card(s)")
        time_buffer = time.sleep(3)

    
    if user_played_Card.startswith("JACK"):
        slapped_card = user_played_Card
        for playedcards in played_pile:
            cpu_deck.append(playedcards)
        time_buffer = time.sleep(2.65)
        print("The 'CPU' slapped a jack. It now takes the played pile of cards.")
        

    elif user_played_Card.startswith("QUEEN") or user_played_Card.startswith("KING"):
        print("The 'CPU' slapped the wrong card!") 
        print("You will now be given its top card, face down.")
        player_deck.append(cpu_deck[0])


def scorecount(player_deck, cpu_deck):
    player_score_after_round = 0
    cpu_score_after_round = 0

    if len(player_deck) > len(cpu_deck):
        player_score_after_round += 1
        cpu_score_after_round -= 1
    elif len(cpu_deck) > len(player_deck):
        cpu_score_after_round += 1
        player_score_after_round -= 1

    if player_score_after_round < 0:
        player_score_after_round = 0
    elif cpu_score_after_round < 0:
        cpu_score_after_round = 0
    
    if player_score_after_round > cpu_score_after_round:
        print("You (Player) are winning!")
    elif player_score_after_round < cpu_score_after_round:
        print("The CPU is winning!")
    else:
        print("It is a tied match!")
    
    return player_score_after_round, cpu_score_after_round

def determine_winner(player_final_wins, cpu_final_wins):
    winner = "Blank"
    winnerExists = False
    if player_final_wins > cpu_final_wins:
        winner = "You (The Player)"
        winnerExists = True
    elif cpu_final_wins < player_final_wins:
        winner = "The CPU"
        winnerExists = True
    else:
        winnerExists = False
    return winner, winnerExists
       

# PROGRAM START BELOW

while True:
    welcomemessage = "Welcome to Kaleb's garbage version of 'Command-line Slapjack'!"
    display_msg = welcomemessage.center(130)
    print('-' * 134)
    print(display_msg)
    print('-' * 134)
    time.sleep(0.65)    # Pause the program for 0.65 seconds
    print("1) Play SlapJack")
    print("2) Quit")
    # INPUT VALIDATION CHECK
    validDecision = False
    while validDecision == False:
        decision = input("Choice: ")
        if decision.isdigit():
            if int(decision) != 1 and int(decision) != 2:
                print("You can only enter either a 1 or 2 for the choices.")
            else:
                if int(decision) == 1:
                    validDecision = True
                elif int(decision) == 2:
                    break
        else:
            print("You can only enter an integer whole number.")
    if validDecision == True:
        display_disclaimer()
        time.sleep(4.75)
        display_rules_and_controls()
        corrChoice = False
        while corrChoice == False:
            choice = input("Type 'C' and press enter once you have finished reading the instructions: ")
            if choice.isalpha():
                if choice != 'c' and choice != 'c'.upper():
                    print("Please type 'c' and press enter.")
                else:
                    corrChoice = True
            else:
                print("Please type a character and press enter.")
        initdeck = buildandshuffledeck()
        playerdeck, cpudeck = splitdeck(initdeck)
        print("You and the computer have been dealt your decks.", end='\n')
        assumed_player_react_time = random.randint(4,5)
        set_cpu_react_time = random.randint(2,4)
        playerinput1 = input("(Player), type 'P' and press enter to place down your first card: ")
        if playerinput1 == 'p' or playerinput1 == 'p'.upper():
            numPlays = 0
            roundsPlayed = 0
            num_plays_in_round = 5
            finished_num_plays = 20
            for plays in range(5, finished_num_plays + 1, num_plays_in_round):
                while numPlays < plays:

                        print(f"Current Round #: {roundsPlayed + 1}")
                        print(f"Current Play #: {numPlays + 1}")
                        print('')

                        """ 
                        IT IS FIRST YOUR (THE PLAYER'S) TURN TO PLACE DOWN YOUR CARD AND YOU AND THE CPU HAVE 2, 3, OR 4 SECONDS
                        TO DECIDE TO SLAP YOUR CARD OR NOT!
                        """
                        pcard = showcard(playerdeck)
                        played_deck_pile = addcardtopile(pcard)
                        print(f"You (Player) placed: {'A ' + pcard:^75}")
                        time.sleep(assumed_player_react_time)
                        slapcard(pcard, played_deck_pile, playerdeck, cpudeck)
                        time.sleep(assumed_player_react_time)
                        

                        """
                        IT IS NOW THE CPU'S TURN TO PLACE DOWN ITS CARD AND THE CPU AND THE CPU HAS 2, 3, OR 4 SECONDS
                        TO DECIDE TO SLAP THE CPU'S CARD OR NOT!
                        """
                        cpucard = showcard(cpudeck)
                        played_deck_pile = addcardtopile(cpucard)
                        print(f"The 'CPU' placed: {'A ' + cpucard:^75}")
                        time.sleep(set_cpu_react_time)
                        slapcard(cpucard, played_deck_pile, playerdeck, cpudeck)
                        time.sleep(set_cpu_react_time)

                        numPlays += 1

                        ''' 
                        USING INPUT FOR NEXT PLAY
                        '''
                        playerinputnext = input("(Player), press ENTER to place down your next card and start the NEXT PLAY: ")
                        print('')
                        if playerinputnext == 'p' or playerinputnext == 'p'.upper():
                            continue
                        if numPlays == plays:
                            """
                            AFTER THE FIRST 5 CONSECUTIVE PLAYS, THE FIRST ROUND IS FINISHED.
                            """
                            roundsPlayed += 1
                            numPlays = 0
                            player_score, cpu_score = scorecount(playerdeck, cpudeck)
                            nextroundprompt = input(f"Round {roundsPlayed} has finished. \n" + "(Player) type 'R' and press enter to start the next round: ")
                            continue
            if roundsPlayed == 4:
                final_winner, winner_exists = determine_winner(player_score, cpu_score)
                if winner_exists:
                    print(f"\n The game has finished and {final_winner} has won!")
                    print(f"Thanks for playing {welcomemessage[11:].capitalize()}!")
                    break
                else:
                    print("The game has ended with a stalemate!")
                    print(f"Thanks for playing {welcomemessage[11:].capitalize()}!")

                    playAgain = False
                    while playAgain == False:
                        decision2 = input("Would you like to play again? Enter '1' for yes or '2' for no: ")
                        if decision2.isdigit():
                            if int(decision2) != 1 and int(decision2) != 2:
                                print("You can only enter either a 1 or 2 for the choices.")
                            else:
                                playAgain = True
                        else:
                            print("You can only enter an integer whole number.")

        else:
            playerinput1 = input("(Player), please type 'P' and press enter to place down your first card, OR the program WILL RESTART.")
            continue
    else:
        break

