import tkinter as tk
import random

# --- 1. Set up the Main Window ---
# This is the main window for our app
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x400") # Set the size of the window (width x height)
root.configure(bg="#f0f0f0") # A light grey background color

# --- 2. Variables to Keep Score ---
# We create variables to hold the score. We will change these later.
player_score = 0
computer_score = 0

# --- 3. The Main Game Function ---
# This function is the "brain" of our game. It runs every time you click a button.
def play(player_choice):
    # 'global' lets our function change the score variables that are outside the function
    global player_score, computer_score
    
    # The computer makes its choice
    choices = ["stone", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    # --- Determine the winner ---
    result = ""
    if player_choice == computer_choice:
        result = "It's a Tie!"
        result_label.config(fg="blue") # Change text color
    elif (player_choice == "stone" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "stone") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You Win! 🎉"
        player_score += 1 # Add 1 to the player's score
        result_label.config(fg="green")
    else:
        result = "You Lose. 😞"
        computer_score += 1 # Add 1 to the computer's score
        result_label.config(fg="red")
        
    # --- Update the Labels on the screen ---
    # We update the text on the labels to show the result and the new score
    result_label.config(text=f"Computer chose {computer_choice}. {result}")
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score}")


# --- 4. Create the Widgets (Labels and Buttons) ---
# These are the visual elements that you see and interact with in the window.

# A simple title label
title_label = tk.Label(root, text="Choose your weapon!", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10) # 'pack' places the widget in the window. pady adds space.

# The label to show the score
score_label = tk.Label(root, text=f"Player: {player_score} | Computer: {computer_score}", font=("Helvetica", 14), bg="#f0f0f0")
score_label.pack(pady=10)

# The label where we will show the game result (Win/Lose/Tie)
result_label = tk.Label(root, text="", font=("Helvetica", 14, "italic"), bg="#f0f0f0", height=4)
result_label.pack(pady=20)

# The button for "Stone"
# The 'command' tells the button what function to run when clicked.
# 'lambda' is a simple way to make sure we can send "stone" to our play function.
stone_button = tk.Button(root, text="Stone 🗿", width=12, height=2, command=lambda: play("stone"))
stone_button.pack(pady=5)

# The button for "Paper"
paper_button = tk.Button(root, text="Paper 📄", width=12, height=2, command=lambda: play("paper"))
paper_button.pack(pady=5)

# The button for "Scissors"
scissors_button = tk.Button(root, text="Scissors ✂️", width=12, height=2, command=lambda: play("scissors"))
scissors_button.pack(pady=5)


# --- 5. Start the App ---
# This line is very important. It tells Tkinter to show the window and wait for you to do something.
# The window will stay open until you close it.
root.mainloop()