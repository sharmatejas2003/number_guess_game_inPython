import tkinter as tk
import random

class GuessTheNumberApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number")

        # Initialize difficulty variable
        self.difficulty_var = tk.StringVar(value="1")

        # Create UI elements
        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess)
        self.submit_button.pack()

        self.hint_label = tk.Label(master, text="")
        self.hint_label.pack()

        self.attempts_label = tk.Label(master, text="")
        self.attempts_label.pack()

        self.replay_button = tk.Button(master, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.replay_button.pack()

        self.difficulty_label = tk.Label(master, text="Choose Difficulty:")
        self.difficulty_label.pack()

        # Difficulty radio buttons
        self.difficulty_easy = tk.Radiobutton(master, text="Easy (10 attempts)", variable=self.difficulty_var, value="1", command=self.reset_game)
        self.difficulty_medium = tk.Radiobutton(master, text="Medium (7 attempts)", variable=self.difficulty_var, value="2", command=self.reset_game)
        self.difficulty_hard = tk.Radiobutton(master, text="Hard (5 attempts)", variable=self.difficulty_var, value="3", command=self.reset_game)

        self.difficulty_easy.pack()
        self.difficulty_medium.pack()
        self.difficulty_hard.pack()

        # Set up initial game state
        self.reset_game()

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        difficulty = self.difficulty_var.get()
        
        if difficulty == '1':
            self.attempts = 10
        elif difficulty == '2':
            self.attempts = 7
        elif difficulty == '3':
            self.attempts = 5
        
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")
        self.hint_label.config(text="")
        self.entry.delete(0, tk.END)
        self.submit_button.config(state=tk.NORMAL)
        self.replay_button.config(state=tk.DISABLED)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.hint_label.config(text="Please enter a valid number.")
            return

        guess = int(guess)
        if guess < 1 or guess > 100:
            self.hint_label.config(text="Your guess must be between 1 and 100.")
            return

        self.attempts -= 1
        
        if guess < self.number_to_guess:
            self.hint_label.config(text="Too low!")
        elif guess > self.number_to_guess:
            self.hint_label.config(text="Too high!")
        else:
            self.hint_label.config(text=f"Congratulations! You've guessed the number {self.number_to_guess}!")
            self.submit_button.config(state=tk.DISABLED)
            self.replay_button.config(state=tk.NORMAL)
            return
        
        if self.attempts == 0:
            self.hint_label.config(text=f"Out of attempts! The number was {self.number_to_guess}.")
            self.submit_button.config(state=tk.DISABLED)
            self.replay_button.config(state=tk.NORMAL)
        else:
            self.attempts_label.config(text=f"Attempts left: {self.attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()
