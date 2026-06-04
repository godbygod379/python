import random
import tkinter as tk

symbols = ['🍒', '🍊', '🍋', '🍌', '🍉', '⭐']

class SlotMachineApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Slot Machine")
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

        self.reel_values = [tk.StringVar(value='❔') for _ in range(3)]
        self.result_text = tk.StringVar(value='Press SPIN to play!')

        self.create_widgets()
        self.spinning = False
        self.spin_index = 0

    def create_widgets(self):
        title_label = tk.Label(self, text="WELCOME TO THE SLOT MACHINE", font=("Segoe UI Emoji", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 12))

        for col in range(3):
            reel_label = tk.Label(self, textvariable=self.reel_values[col], font=("Segoe UI Emoji", 48), width=2)
            reel_label.grid(row=1, column=col, padx=8, pady=8)

        self.result_label = tk.Label(self, textvariable=self.result_text, font=("Segoe UI", 12), wraplength=320, justify="center")
        self.result_label.grid(row=2, column=0, columnspan=3, pady=(10, 10))

        self.spin_button = tk.Button(self, text="SPIN", font=("Segoe UI", 14, "bold"), command=self.start_spin, width=12)
        self.spin_button.grid(row=3, column=0, columnspan=3, pady=(0, 8))

        self.quit_button = tk.Button(self, text="Quit", font=("Segoe UI", 10), command=self.destroy)
        self.quit_button.grid(row=4, column=0, columnspan=3)

    def start_spin(self):
        if self.spinning:
            return
        self.spinning = True
        self.spin_index = 0
        self.result_text.set("Spinning...")
        self.spin_button.configure(state="disabled")
        self.animate()

    def animate(self):
        if self.spin_index < 15:
            for idx in range(3):
                self.reel_values[idx].set(random.choice(symbols))
            self.spin_index += 1
            self.after(80, self.animate)
        else:
            self.finish_spin()

    def finish_spin(self):
        final_results = [random.choice(symbols) for _ in range(3)]
        for idx, symbol in enumerate(final_results):
            self.reel_values[idx].set(symbol)

        if final_results[0] == final_results[1] == final_results[2]:
            self.result_text.set("🎉 JACKPOT! YOU WIN! 🎉")
        elif final_results[0] == final_results[1] or final_results[1] == final_results[2] or final_results[0] == final_results[2]:
            self.result_text.set("✨ You got a match! Small win! ✨")
        else:
            self.result_text.set("❌ No match. Try again!")

        self.spin_button.configure(state="normal")
        self.spinning = False

if __name__ == "__main__":
    app = SlotMachineApp()
    app.mainloop()
