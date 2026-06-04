import tkinter as tk
from tkinter import messagebox
import random

class RouletteGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Casino Roulette")
        self.root.geometry("400x300")
        self.money = 0
        self.bet_amount = 0
        
        # Initial money input screen
        self.setup_initial_screen()
    
    def setup_initial_screen(self):
        self.clear_window()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        
        label = tk.Label(frame, text="How much money do you have?", font=("Arial", 14))
        label.pack(pady=10)
        
        self.money_entry = tk.Entry(frame, font=("Arial", 12), width=20)
        self.money_entry.pack(pady=10)
        
        button = tk.Button(frame, text="Start Game", command=self.start_game, font=("Arial", 12))
        button.pack(pady=10)
    
    def start_game(self):
        try:
            self.money = float(self.money_entry.get())
            if self.money <= 0:
                messagebox.showerror("Invalid", "Please enter a positive amount")
                return
            self.setup_betting_screen()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    
    def setup_betting_screen(self):
        self.clear_window()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        
        money_label = tk.Label(frame, text=f"Your Money: ${self.money:.2f}", font=("Arial", 12, "bold"))
        money_label.pack(pady=10)
        
        bet_label = tk.Label(frame, text="How much do you want to bet?", font=("Arial", 12))
        bet_label.pack(pady=10)
        
        self.bet_entry = tk.Entry(frame, font=("Arial", 12), width=20)
        self.bet_entry.pack(pady=10)
        
        color_frame = tk.Frame(frame)
        color_frame.pack(pady=15)
        
        tk.Label(color_frame, text="Pick a color:", font=("Arial", 12)).pack()
        
        button_frame = tk.Frame(color_frame)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Red", command=lambda: self.place_bet("Red"), 
                 font=("Arial", 12), bg="red", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Black", command=lambda: self.place_bet("Black"), 
                 font=("Arial", 12), bg="black", fg="white", width=10).pack(side=tk.LEFT, padx=5)
    
    def place_bet(self, color):
        try:
            self.bet_amount = float(self.bet_entry.get())
            if self.bet_amount <= 0 or self.bet_amount > self.money:
                messagebox.showerror("Invalid Bet", "Please enter a valid bet amount")
                return
            self.spin_roulette(color)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    
    def spin_roulette(self, chosen_color):
        colors = ["Red", "Black"]
        result = random.choice(colors)
        
        if result == chosen_color:
            self.money += self.bet_amount
            messagebox.showinfo("Win!", f"You won ${self.bet_amount:.2f}!\nYour total: ${self.money:.2f}")
        else:
            self.money -= self.bet_amount
            messagebox.showinfo("Lose", f"The roulette landed on {result}.\nYou lost ${self.bet_amount:.2f}!\nYour total: ${self.money:.2f}")
        
        if self.money <= 0:
            messagebox.showinfo("Game Over", "You're out of money!")
            self.setup_initial_screen()
        else:
            self.ask_play_again()
    
    def ask_play_again(self):
        if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
            self.setup_betting_screen()
        else:
            messagebox.showinfo("Thanks", f"Thanks for playing! Final amount: ${self.money:.2f}")
            self.setup_initial_screen()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RouletteGame(root)
    root.mainloop()
