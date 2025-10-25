import tkinter as tk
import random

# Function to determine the winner
def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n"

    if user_choice == computer_choice:
        result_text += "It's a Tie!"
        color = "blue"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result_text += "You Win! 🎉"
        color = "green"
    else:
        result_text += "Computer Wins! 💻"
        color = "red"

    result_label.config(text=result_text, fg=color)

# Create main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Instruction label
instruction_label = tk.Label(root, text="Choose your option:", font=("Arial", 12))
instruction_label.pack(pady=10)

# Buttons for user choice
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12),
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12),
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12),
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 14), justify="center")
result_label.pack(pady=30)

# Run the Tkinter event loop
root.mainloop()
