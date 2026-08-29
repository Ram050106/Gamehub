import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo
from utils.assets import asset
import random


class BouncyBallGame(ttk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.after_id = None

        # ---------- CONFIRM BACK ----------
        def confirm():
            answer = askyesno(
                title="Exit",
                message="Are you sure you want to go back to the main menu?"
            )
            if answer:
                self.stop_game()
                show_frame("home")

        # ---------- TOP FRAME ----------
        game_top_frame = ttk.Frame(self, padding=10)
        game_top_frame.pack(fill="x", pady=(10, 10))

        ttk.Label(
            game_top_frame,
            text="Bouncy Ball",
            font=("Segoe UI", 30, "bold")
        ).pack()

        self.game_back = tk.PhotoImage(file=asset("back.png"))
        ttk.Button(
            game_top_frame,
            text="Back",
            image=self.game_back,
            compound=tk.LEFT,
            command=confirm
        ).place(relx=0.02, rely=0.2, anchor="nw")

        ttk.Button(
            game_top_frame,
            text="Restart",
            command=self.restart_game
        ).place(relx=0.98, rely=0.2, anchor="ne")

        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=15)

        # ---------- GAME AREA ----------
        self.game_area = ttk.Frame(self, padding=20)
        self.game_area.pack(fill="both", expand=True)

        self.build_game(self.game_area)

    # ======================================================
    def build_game(self, parent):
        self.game_width = 1000
        self.game_height = 500
        self.ball_radius = 15
        self.paddle_width = 500
        self.paddle_height = 20
        self.gravity = 0.5
        self.bounce_strength = -12

        self.score = 0
        self.ball_speed_x = 0
        self.ball_speed_y = 0
        self.game_running = False
        self.game_started = False

        container = tk.Frame(parent)
        container.pack(expand=True)

        self.score_label = tk.Label(
            container,
            text="Score: 0",
            font=("Arial", 18, "bold"),
            bg="#87CEEB",
            fg="white"
        )
        self.score_label.pack(pady=10)

        self.canvas = tk.Canvas(
            container,
            width=self.game_width,
            height=self.game_height,
            bg="#87CEEB",
            highlightthickness=2,
            highlightbackground="#4682B4"
        )
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_click)
        self.bind_all("<Left>", self.move_paddle_left)
        self.bind_all("<Right>", self.move_paddle_right)
        self.bind_all("<a>", self.move_paddle_left)
        self.bind_all("<d>", self.move_paddle_right)

        self.restart_game()

    # ======================================================
    def draw_clouds(self):
        for x, y in [(80, 60), (250, 40), (150, 100), (320, 80)]:
            self.canvas.create_oval(x, y, x+40, y+25, fill="white", outline="")
            self.canvas.create_oval(x+15, y-10, x+55, y+15, fill="white", outline="")
            self.canvas.create_oval(x+30, y, x+70, y+25, fill="white", outline="")

    # ======================================================
    def on_click(self, event):
        if not self.game_started:
            self.game_started = True
            self.game_running = True
            self.canvas.delete("start")
            self.ball_speed_y = self.bounce_strength
            self.game_loop()
        elif self.game_running and self.ball_speed_y > -5:
            self.ball_speed_y = self.bounce_strength

    # ======================================================
    def move_paddle_left(self, event):
        if self.paddle_x > 0:
            self.canvas.move(self.paddle, -20, 0)
            self.paddle_x -= 20

    def move_paddle_right(self, event):
        if self.paddle_x + self.paddle_width < self.game_width:
            self.canvas.move(self.paddle, 20, 0)
            self.paddle_x += 20

    # ======================================================
    def game_loop(self):
        if not self.game_running:
            return

        self.ball_speed_y += self.gravity
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        if self.ball_x <= self.ball_radius or self.ball_x >= self.game_width - self.ball_radius:
            self.ball_speed_x *= -1

        if self.ball_y <= self.ball_radius:
            self.ball_speed_y = abs(self.ball_speed_y)

        if (self.paddle_y <= self.ball_y + self.ball_radius <= self.paddle_y + self.paddle_height and
                self.paddle_x <= self.ball_x <= self.paddle_x + self.paddle_width and
                self.ball_speed_y > 0):

            self.ball_speed_y = self.bounce_strength
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

            self.ball_speed_x += random.randint(-2, 2)
            self.ball_speed_x = max(-8, min(8, self.ball_speed_x))

        if self.ball_y > self.game_height:
            self.game_over()
            return

        self.canvas.coords(
            self.ball,
            self.ball_x - self.ball_radius,
            self.ball_y - self.ball_radius,
            self.ball_x + self.ball_radius,
            self.ball_y + self.ball_radius
        )

        self.canvas.coords(
            self.ball_shine,
            self.ball_x - 5,
            self.ball_y - 8,
            self.ball_x + 3,
            self.ball_y
        )

        self.after_id = self.after(20, self.game_loop)

    # ======================================================
    def game_over(self):
        self.game_running = False
        self.canvas.create_text(
            self.game_width // 2,
            self.game_height // 2,
            text=f"Game Over\nScore: {self.score}",
            font=("Arial", 26, "bold"),
            fill="#8B0000"
        )
        showinfo("Game Over", f"Your score: {self.score}")

    # ======================================================
    def restart_game(self):
        self.stop_game()

        self.canvas.delete("all")
        self.score = 0
        self.ball_speed_x = 0
        self.ball_speed_y = 0
        self.game_running = False
        self.game_started = False

        self.draw_clouds()

        self.canvas.create_rectangle(
            0, self.game_height - 60, self.game_width, self.game_height - 40,
            fill="#90EE90", outline=""
        )
        self.canvas.create_rectangle(
            0, self.game_height - 40, self.game_width, self.game_height,
            fill="#8B4513", outline=""
        )

        self.paddle_x = self.game_width // 2 - self.paddle_width // 2
        self.paddle_y = self.game_height - 150

        self.paddle = self.canvas.create_rectangle(
            self.paddle_x, self.paddle_y,
            self.paddle_x + self.paddle_width,
            self.paddle_y + self.paddle_height,
            fill="#F4A460", outline="#8B4513", width=2
        )

        self.ball_x = self.game_width // 2
        self.ball_y = self.paddle_y - 30

        self.ball = self.canvas.create_oval(
            self.ball_x - self.ball_radius,
            self.ball_y - self.ball_radius,
            self.ball_x + self.ball_radius,
            self.ball_y + self.ball_radius,
            fill="#FF6347", outline="#8B0000", width=2
        )

        self.ball_shine = self.canvas.create_oval(
            self.ball_x - 5,
            self.ball_y - 8,
            self.ball_x + 3,
            self.ball_y,
            fill="white", outline=""
        )

        self.canvas.create_text(
            self.game_width // 2,
            self.game_height // 2 - 50,
            text="Tap to Play",
            font=("Arial", 28, "bold"),
            fill="#8B4513",
            tags="start"
        )

        self.score_label.config(text="Score: 0")

    # ======================================================
    def stop_game(self):
        self.game_running = False
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
