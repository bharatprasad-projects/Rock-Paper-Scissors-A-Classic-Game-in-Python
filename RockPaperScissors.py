# Rock Paper Scissors Game
# ------------------------
# Author: [Bharat Prasad]
# Date: [01-03-2025]
# Description:
#     This is a simple Rock Paper Scissors game implemented in Python.
#     The user plays against the computer, which randomly selects Rock, Paper, or Scissors.
#     The game follows standard rules:
#         - Rock beats Scissors
#         - Scissors beat Paper
#         - Paper beats Rock
#     The program announces the winner after each round.

# Usage:
#     Run the script and follow the on-screen instructions to play.

# Dependencies:
#     - Python 3.x
#     - random (built-in module)
#------------------------------------------------------------------------------------------------------------

# Module Section
from tkinter import * # pip install tkinter
import random # pip install random
#------------------------------------------------------------------------------------------------------------

# Accessing Tkinter
root = Tk() # You can use any variable instead of root
#------------------------------------------------------------------------------------------------------------

# Code
try:
    def error_msg():
        message_frame = Frame(root, relief="solid", bd=2)
        message_frame.place(relx=0.5, rely=0.5, anchor="center") 
        label = Label(message_frame, text="Please select any option or restart the game !", font=("Times New Roman", 12))
        label.pack(pady=20)

        def close_message_box():
            message_frame.destroy()

        button = Button(message_frame, text="Close", command=close_message_box)
        button.pack(pady=10)

    def computer_msg():
        message_frame = Frame(root, relief="solid", bd=2)
        message_frame.place(relx=0.5, rely=0.5, anchor="center") 
        label = Label(message_frame, text="Computer won this match !", font=("Times New Roman", 12))
        label.pack(pady=20)

        def close_message_box():
            message_frame.destroy()

        button = Button(message_frame, text="Close", command=close_message_box)
        button.pack(pady=10)

    def player_msg():
        message_frame = Frame(root, relief="solid", bd=2)
        message_frame.place(relx=0.5, rely=0.5, anchor="center") 
        label = Label(message_frame, text="You won this match !", font=("Times New Roman", 12))
        label.pack(pady=20)

        def close_message_box():
            message_frame.destroy()

        button = Button(message_frame, text="Close", command=close_message_box)
        button.pack(pady=10)

    global computer_score_board , player_score_board
    computer_score_board = 0
    player_score_board = 0
    def click():
        global computer_score_board , player_score_board
        items = ["rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors"
                ,"rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors",
                "rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors",
                "rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors"
                ,"rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors",
                "rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors",
                "rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors"
                ,"rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors",
                "rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors","rock","paper","scissors"]
        computer_guess = random.choice(items)
        player_input = radio_var.get()
        if player_score_board == 10:
            print("Player Won this match")
            player_msg()
            player.config(text="You won the match")
        elif computer_score_board == 10:
            print("Computer Won the match")
            computer_msg()
            computer.config(text="Computer won the match")
        elif player_input == computer_guess :
            print("DRAW")
            computer_result.config(text="DRAW "+str(computer_guess))
            player_result.config(text="DRAW "+ str(player_input))
        elif (player_input=="rock" and computer_guess == "paper"): #computer wins
            print("Computer wins",computer_guess)
            computer_result.config(text="Computer Wins Computer Chose : "+str(computer_guess))
            player_result.config(text="You lose "+ str(player_input))
            computer_score_board = computer_score_board + 1
        elif(player_input=="paper" and computer_guess == "rock"): #player wins
            print("PLayer wins",computer_guess)
            computer_result.config(text="Computer lose Computer Chose : "+str(computer_guess))
            player_result.config(text="You wins "+ str(player_input))
            player_score_board = player_score_board + 1 
        elif (player_input=="rock" and computer_guess == "scissors"): #player wins
            print("Player wins",computer_guess)
            computer_result.config(text="Computer lose Computer Chose : "+str(computer_guess))
            player_result.config(text="You wins "+ str(player_input))
            player_score_board = player_score_board + 1 
        elif(player_input=="scissors" and computer_guess == "rock"): #computer wins
            print("Computer wins",computer_guess)
            computer_result.config(text="Computer Wins Computer Chose : "+str(computer_guess))
            player_result.config(text="You lose "+str(player_input))
            computer_score_board = computer_score_board + 1
        elif (player_input=="paper" and computer_guess == "scissors"): #computer wins
            print("computer wins",computer_guess)
            computer_result.config(text="Computer Wins Computer Chose : "+str(computer_guess))
            player_result.config(text="You lose "+str(player_input))
            computer_score_board = computer_score_board + 1
        elif (player_input=="scissors" and computer_guess == "paper"): #player wins
            print("Player Wins",computer_guess)
            computer_result.config(text="Computer lose Computer Chose : "+str(computer_guess))
            player_result.config(text="You wins "+str(player_input))
            player_score_board = player_score_board + 1 
        else:
            print("something went wrong")
            error_msg()
        player_score.config(text="Score: "+str(player_score_board))
        computer_score.config(text="Score: "+str(computer_score_board))

        print("player score is : ",player_score_board,"computer score is : ",computer_score_board)
except EOFError as e:
    print("error",e)        
        

#------------------------------------------------------------------------------------------------------------

# Setting the Game Layout 
radio_var = StringVar() # To Hold the selected value
welcome = Label(root,text="Welcome to the game Rock, Paper, Scissors",font=("Times New Roman",10))
welcome.place(x=80,y=10)
computer = Label(root, text="COMPUTER",font=("Times New Roman",10))
computer.place(x=160,y=40)
computer_result = Label(root,text=" ",font=("Times New Roman",12))
computer_result.place(x=16,y=80)
computer_score = Label(root,text="Score: ",font=("Times New Roman",12))
computer_score.place(x=290,y=80)
versus = Label(root,text="----------------------------------------------VS-------------------------------------------------",font=("Times New Roman",10))
versus.place(x=0,y=120)
player = Label(root, text="YOU",font=("Times New Roman",10))
player.place(x=178,y=160)
player_result = Label(root,text=" ",font=("Times New Roman",12))
player_result.place(x=146,y=200)
player_score = Label(root,text="Score: ",font=("Times New Roman",12))
player_score.place(x=290,y=200)
clue = Label(root,text="'r' for Rock 'p' for Paper 's' for Scissors")
clue.place(x=130,y=250)
rock = Radiobutton(root, text="Rock", variable=radio_var, value="rock",font=("Times New Roman",10))
rock.place(x=10,y=150)
paper = Radiobutton(root, text="Paper", variable=radio_var, value="paper",font=("Times New Roman",10))
paper.place(x=10,y=180)
scissors = Radiobutton(root, text="Scissors", variable=radio_var, value="scissors",font=("Times New Roman",10))
scissors.place(x=10,y=210)
start = Button(root,text="Play",font=("Times New Roman",10),command=click)
start.place(x=60,y=250)
rules_header = Label(root,text="""--------------------------------------------Rules-----------------------------------------------
                
Rock vs Paper -> Paper wins 
Rock vs Scissors -> Rock wins 
Paper vs Scissors -> Scissors wins
                        """,font=("Times New Roman",10),anchor="center")
rules_header.place(x=0,y=280)
created = Label(root , text="Created by Bharat Prasad",font=("Times New Roman",12))
created.place(x=110,y=370)

#------------------------------------------------------------------------------------------------------------

# Customizing GUI
root.title("Rock Paper Scissors")
root.geometry("400x400")
icon = PhotoImage(file="favicon.png")
root.iconphoto(True, icon)
root.resizable(False,False)
root.mainloop() 
#------------------------------------------------------------------------------------------------------------