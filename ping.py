import random
import tkinter as tk
from tkinter import messagebox

class PingPongGame:
    def __init__(self, root):
        self.root = root
        root.title("Ping Pong")
        root.resizable(False, False)

        self.mode = None
        self.score_left = 0
        self.score_right = 0
        self.running = False
        self.ball_dx = 5
        self.ball_dy = 3
        self.paddle_speed = 30
        self.ai_speed = 5

        self.menu_frame = tk.Frame(root, padx=20, pady=20)
        self.menu_frame.pack(fill="both", expand=True)

        tk.Label(self.menu_frame, text="Ping Pong Menu", font=("Segoe UI", 18, "bold")).pack(pady=10)
        tk.Button(self.menu_frame, text="Tutorial", width=20, command=self.show_tutorial).pack(pady=5)
        tk.Button(self.menu_frame, text="Multiplayer", width=20, command=lambda: self.start_game("multiplayer")).pack(pady=5)
        tk.Button(self.menu_frame, text="Singleplayer", width=20, command=lambda: self.start_game("singleplayer")).pack(pady=5)
        tk.Button(self.menu_frame, text="Exit", width=20, command=root.destroy).pack(pady=5)

        self.game_frame = tk.Frame(root)
        self.status_frame = tk.Frame(self.game_frame)
        self.mode_label = tk.Label(self.status_frame, text="Mode: ", font=("Segoe UI", 12))
        self.left_score_label = tk.Label(self.status_frame, text="Left: 0", font=("Segoe UI", 12))
        self.right_score_label = tk.Label(self.status_frame, text="Right: 0", font=("Segoe UI", 12))
        self.mode_label.pack(side="left", padx=10)
        self.left_score_label.pack(side="left", padx=10)
        self.right_score_label.pack(side="left", padx=10)
        self.status_frame.pack(fill="x", pady=5)

        self.canvas = tk.Canvas(self.game_frame, width=600, height=400, bg="#222")
        self.canvas.pack()
        self.canvas.bind("<KeyPress>", self.on_key_down)

        self.btn_back = tk.Button(self.game_frame, text="Back to Menu", command=self.stop_game)
        self.btn_back.pack(pady=5)

        self.ball = None
        self.left_paddle = None
        self.right_paddle = None

    def show_tutorial(self):
        messagebox.showinfo(
            "Tutorial",
            "Multiplayer:\n"
            "- Left paddle: W = up, S = down\n"
            "- Right paddle: Up = up, Down = down\n\n"
            "Singleplayer:\n"
            "- Left paddle: W = up, S = down\n"
            "- Right paddle: AI follows the ball vertically\n\n"
            "Press the button for the mode you want, then use the controls while playing. Scores show on top."
        )

    def start_game(self, mode):
        self.mode = mode
        self.score_left = 0
        self.score_right = 0
        self.menu_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        self.setup_game()
        self.update_score_labels()
        self.canvas.focus_set()
        self.running = True
        self.move_ball()

    def setup_game(self):
        self.canvas.delete("all")
        self.left_paddle = self.canvas.create_rectangle(20, 150, 35, 250, fill="white")
        self.right_paddle = self.canvas.create_rectangle(565, 150, 580, 250, fill="white")
        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="yellow")
        self.ball_dx = random.choice([-5, 5])
        self.ball_dy = random.choice([-3, 3])
        self.mode_label.config(text=f"Mode: {self.mode.capitalize()}")

    def stop_game(self):
        self.running = False
        self.game_frame.pack_forget()
        self.menu_frame.pack(fill="both", expand=True)

    def update_score_labels(self):
        self.left_score_label.config(text=f"Left: {self.score_left}")
        self.right_score_label.config(text=f"Right: {self.score_right}")

    def on_key_down(self, event):
        if not self.running:
            return
        key = event.keysym.lower()
        if key == "w":
            self.move_paddle(self.left_paddle, -self.paddle_speed)
        elif key == "s":
            self.move_paddle(self.left_paddle, self.paddle_speed)
        elif self.mode == "multiplayer":
            if key == "up":
                self.move_paddle(self.right_paddle, -self.paddle_speed)
            elif key == "down":
                self.move_paddle(self.right_paddle, self.paddle_speed)

    def move_paddle(self, paddle, dy):
        x1, y1, x2, y2 = self.canvas.coords(paddle)
        new_y1 = max(0, min(400 - 100, y1 + dy))
        self.canvas.coords(paddle, x1, new_y1, x2, new_y1 + 100)

    def move_ball(self):
        if not self.running:
            return

        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        x1, y1, x2, y2 = self.canvas.coords(self.ball)

        if y1 <= 0 or y2 >= 400:
            self.ball_dy = -self.ball_dy

        if x1 <= 0:
            self.score_right += 1
            self.update_score_labels()
            self.reset_ball()
        elif x2 >= 600:
            self.score_left += 1
            self.update_score_labels()
            self.reset_ball()
        else:
            if self.check_collision(self.left_paddle, (x1, y1, x2, y2)) and self.ball_dx < 0:
                self.ball_dx = -self.ball_dx
            if self.check_collision(self.right_paddle, (x1, y1, x2, y2)) and self.ball_dx > 0:
                self.ball_dx = -self.ball_dx

        if self.mode == "singleplayer":
            self.move_ai_paddle()

        self.root.after(30, self.move_ball)

    def reset_ball(self):
        self.canvas.coords(self.ball, 290, 190, 310, 210)
        self.ball_dx = random.choice([-5, 5])
        self.ball_dy = random.choice([-3, 3])

    def move_ai_paddle(self):
        px1, py1, px2, py2 = self.canvas.coords(self.right_paddle)
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)
        paddle_center = (py1 + py2) / 2
        ball_center = (by1 + by2) / 2
        if ball_center > paddle_center + 10:
            self.move_paddle(self.right_paddle, self.ai_speed)
        elif ball_center < paddle_center - 10:
            self.move_paddle(self.right_paddle, -self.ai_speed)

    def check_collision(self, paddle, ball_coords):
        px1, py1, px2, py2 = self.canvas.coords(paddle)
        bx1, by1, bx2, by2 = ball_coords
        return not (bx2 < px1 or bx1 > px2 or by2 < py1 or by1 > py2)


if __name__ == "__main__":
    root = tk.Tk()
    app = PingPongGame(root)
    root.mainloop()
