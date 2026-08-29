import tkinter as tk
import random
from tkinter.messagebox import askyesno

class CarRacingGame(tk.Frame):  # <-- Changed to tk.Frame
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame

        # ---------- CONFIG ----------
        self.game_width = 560
        self.game_height = 600
        self.car_width = 70
        self.car_height = 110
        self.obstacle_width = 50
        self.obstacle_height = 90
        self.base_speed = 8
        self.obstacle_speed = 6
        self.score = 0
        self.frame_count = 0
        self.game_running = False
        self.loop_id = None

        self.configure(bg="#121212")  # <-- Works now

        # ---------- TOP BAR ----------
        top_bar = tk.Frame(self, bg="#1f1f1f", height=50)
        top_bar.pack(fill="x")

        self.back_btn = tk.Button(
            top_bar, text="← Back", bg="#FF4D6D", fg="white",
            font=("Arial", 12, "bold"), relief="flat", command=self.go_back
        )
        self.back_btn.pack(side="left", padx=10, pady=8)

        self.title_label = tk.Label(
            top_bar, text="Car Racing", bg="#1f1f1f", fg="white",
            font=("Arial", 18, "bold")
        )
        self.title_label.pack(side="left", padx=20)

        self.restart_btn = tk.Button(
            top_bar, text="Restart", bg="#4D79FF", fg="white",
            font=("Arial", 12, "bold"), relief="flat", command=self.reset_game
        )
        self.restart_btn.pack(side="right", padx=10, pady=8)

        # ---------- GAME CANVAS ----------
        self.canvas = tk.Canvas(
            self, width=self.game_width, height=self.game_height,
            bg="#2f2f2f", highlightthickness=0
        )
        self.canvas.pack(pady=10)

        # ---------- ROAD ----------
        self.lanes = []
        self.draw_lanes()

        # ---------- PLAYER ----------
        self.player_x = self.game_width // 2 - self.car_width // 2
        self.player_y = self.game_height - 160
        self.draw_player_car()

        # ---------- OBSTACLES ----------
        self.obstacles = []

        # ---------- UI ----------
        self.score_text = self.canvas.create_text(
            80, 30, text="Score: 0", fill="white",
            font=("Arial", 16, "bold")
        )

        self.game_over_text = self.canvas.create_text(
            self.game_width // 2, self.game_height // 2,
            text="", fill="red", font=("Arial", 30, "bold")
        )

        # ---------- CONTROLS ----------
        self.bind_all("<Left>", self.move_left)
        self.bind_all("<Right>", self.move_right)

    # ================= FRAME SHOW =================
    def on_show(self):
        self.reset_game()

    # ================= NAV =================
    def go_back(self):
        if askyesno("Exit", "Are you sure you want to go back to main menu?"):
            self.game_running = False
            self.show_frame("home")

    # ================= ROAD =================
    def draw_lanes(self):
        xs = [self.game_width // 3, (self.game_width * 2) // 3]
        for x in xs:
            for y in range(0, self.game_height + 80, 80):
                self.lanes.append(
                    self.canvas.create_line(
                        x, y, x, y + 50, fill="white", width=6
                    )
                )

    # ================= PLAYER CAR (SUV WITH HEADLIGHTS) =================
    def draw_player_car(self):
        x, y = self.player_x, self.player_y
        self.player_car_parts = [
            # Shadow
            self.canvas.create_oval(
                x + 5, y + 95, x + 65, y + 115, fill="#1a1a1a", outline=""
            ),
            # SUV Body
            self.canvas.create_rectangle(
                x + 10, y + 20, x + 60, y + 100, fill="#C12E2E",
                outline="#1A5276", width=2
            ),
            # Roof
            self.canvas.create_rectangle(
                x + 15, y + 10, x + 55, y + 30, fill="#C12E2E", outline="#122B40"
            ),
            # Windows
            self.canvas.create_rectangle(
                x + 17, y + 25, x + 53, y + 50, fill="#A9CCE3",
                outline="#1B4F72", width=1
            ),
            # Front headlights (yellow)
            self.canvas.create_oval(
                x + 8, y + 40, x + 14, y + 50, fill="#FFF200", outline="#FFD700"
            ),
            self.canvas.create_oval(
                x + 56, y + 40, x + 62, y + 50, fill="#FFF200", outline="#FFD700"
            ),
            # Wheels (left front)
            self.canvas.create_oval(
                x, y + 60, x + 15, y + 85, fill="#1a1a1a", outline="black", width=2
            ),
            self.canvas.create_oval(
                x + 4, y + 64, x + 11, y + 80, fill="#C0C0C0", outline=""
            ),
            # Wheels (right front)
            self.canvas.create_oval(
                x + 55, y + 60, x + 70, y + 85, fill="#1a1a1a", outline="black", width=2
            ),
            self.canvas.create_oval(
                x + 59, y + 64, x + 66, y + 80, fill="#C0C0C0", outline=""
            ),
            # Wheels (left rear)
            self.canvas.create_oval(
                x, y + 80, x + 15, y + 105, fill="#1a1a1a", outline="black", width=2
            ),
            self.canvas.create_oval(
                x + 4, y + 84, x + 11, y + 100, fill="#C0C0C0", outline=""
            ),
            # Wheels (right rear)
            self.canvas.create_oval(
                x + 55, y + 80, x + 70, y + 105, fill="#1a1a1a", outline="black", width=2
            ),
            self.canvas.create_oval(
                x + 59, y + 84, x + 66, y + 100, fill="#C0C0C0", outline=""
            ),
        ]

    # ================= MOVEMENT =================
    def move_left(self, event):
        if self.game_running and self.player_x > 10:
            for part in self.player_car_parts:
                self.canvas.move(part, -self.base_speed, 0)
            self.player_x -= self.base_speed

    def move_right(self, event):
        if self.game_running and self.player_x + self.car_width < self.game_width - 10:
            for part in self.player_car_parts:
                self.canvas.move(part, self.base_speed, 0)
            self.player_x += self.base_speed

    # ================= OBSTACLES =================
    def create_obstacle(self):
        lanes = [
            self.game_width // 6 - self.obstacle_width // 2,
            self.game_width // 2 - self.obstacle_width // 2,
            (self.game_width * 5) // 6 - self.obstacle_width // 2
        ]
        x = random.choice(lanes)
        y = -self.obstacle_height
        obs = self.canvas.create_rectangle(
            x, y, x + self.obstacle_width, y + self.obstacle_height,
            fill="#1e90ff", outline="black", width=2
        )
        self.obstacles.append(obs)

    def move_obstacles(self):
        for obs in self.obstacles[:]:
            self.canvas.move(obs, 0, self.obstacle_speed)
            if self.canvas.coords(obs)[1] > self.game_height:
                self.canvas.delete(obs)
                self.obstacles.remove(obs)
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

    # ================= COLLISION =================
    def check_collision(self):
        px1 = self.player_x
        py1 = self.player_y
        px2 = self.player_x + self.car_width
        py2 = self.player_y + self.car_height

        for obs in self.obstacles:
            ox1, oy1, ox2, oy2 = self.canvas.coords(obs)
            if px1 < ox2 and px2 > ox1 and py1 < oy2 and py2 > oy1:
                self.game_over()

    # ================= LOOP =================
    def game_loop(self):
        if self.loop_id is not None:
            self.after_cancel(self.loop_id)

        if self.game_running:
            self.frame_count += 1
            if self.frame_count % 60 == 0:
                self.create_obstacle()

            self.move_obstacles()
            self.check_collision()

            for line in self.lanes:
                self.canvas.move(line, 0, self.obstacle_speed)
                if self.canvas.coords(line)[1] > self.game_height:
                    self.canvas.move(line, 0, -self.game_height - 80)

        self.loop_id = self.after(30, self.game_loop)

    # ================= STATE =================
    def game_over(self):
        self.game_running = False
        self.canvas.itemconfig(self.game_over_text, text="GAME OVER")

    def reset_game(self):
        if self.loop_id is not None:
            self.after_cancel(self.loop_id)
            self.loop_id = None

        self.game_running = False

        for obs in self.obstacles:
            self.canvas.delete(obs)
        self.obstacles.clear()

        dx = (self.game_width // 2 - self.car_width // 2) - self.player_x
        for part in self.player_car_parts:
            self.canvas.move(part, dx, 0)
        self.player_x = self.game_width // 2 - self.car_width // 2

        self.score = 0
        self.frame_count = 0
        self.canvas.itemconfig(self.score_text, text="Score: 0")
        self.canvas.itemconfig(self.game_over_text, text="")

        self.game_running = True
        self.game_loop()
