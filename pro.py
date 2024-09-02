import random
from tkinter import *
from tkinter import messagebox
import emoji

# Create the main window
window = Tk()
window.title("Rock Paper Scissors")
window.geometry('400x300')

# Game Choices
choices = ["rock", "paper", "scissors"]

# تجديد من الفائز
def determine_winner(player, computer):
    if player == computer:
        result_label.config(text="It's a draw! " + emoji.emojize(":neutral_face:"))
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        result_label.config(text="You win! " + emoji.emojize(":grinning_face:"))
    else:
        result_label.config(text="You lose! " + emoji.emojize(":disappointed_face:"))

# Function for player choice
def player_choice(player):
    computer = random.choice(choices)
    computer_choice_label.config(text=f"Computer chose: {computer}")
    determine_winner(player, computer)

# Function for the game End
def quit_game():
    messagebox.showinfo("Goodbye!", "Thanks for playing! Hope you enjoyed.")
    window.destroy()

# GUI Label
Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

# GUI buttons
rock_button = Button(window, text="Rock", width=10, command=lambda: player_choice("rock"))
rock_button.pack(pady=5)

paper_button = Button(window, text="Paper", width=10, command=lambda: player_choice("paper"))
paper_button.pack(pady=5)

scissors_button = Button(window, text="Scissors", width=10, command=lambda: player_choice("scissors"))
scissors_button.pack(pady=5)

# Computer Choice
computer_choice_label = Label(window, text="", font=("Arial", 12))
computer_choice_label.pack(pady=10)

#result
result_label = Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# quit button
quit_button = Button(window, text="Quit", width=10, command=quit_game)
quit_button.pack(pady=20)

# Run the Game
window.mainloop()