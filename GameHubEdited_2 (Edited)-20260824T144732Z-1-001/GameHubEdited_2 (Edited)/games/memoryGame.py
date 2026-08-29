import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo
from utils.assets import asset


class MemoryGame(ttk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent, style="App.TFrame")
        self.show_frame = show_frame

        # ======================================================
        # TIMER STATE (simple like guess game)
        # ======================================================
        self.timer_id = None
        self.timer_running = False
        self.time_elapsed = 0

        # ======================================================
        # CUSTOM STYLING (UNCHANGED)
        # ======================================================
        style = ttk.Style()

        style.configure(
            "Memory.TButton",
            font=("Segoe UI", 32, "bold"),
            padding=10,
            width=4
        )

        style.configure(
            "Hidden.Memory.TButton",
            background="#2563eb",
            font=("Segoe UI", 32, "bold"),
            padding=10,
            width=4
        )

        # ======================================================
        # GAME STATE
        # ======================================================
        self.fruits = ["🍎", "🍌", "🍒", "🍓", "🍇", "🍍", "🥝", "🍉"]
        self.cards = self.fruits * 2
        random.shuffle(self.cards)

        self.buttons = []
        self.first_card = None
        self.matches = 0
        self.attempts = 0

        # ======================================================
        # TOP BAR (ORIGINAL LOOK)
        # ======================================================
        top = ttk.Frame(self, style="App.TFrame", padding=10)
        top.pack(fill="x", pady=(10, 10))

        top.columnconfigure((0, 1, 2), weight=1)

        self.game_back = tk.PhotoImage(file=asset('back.png'))

        ttk.Button(
            top,
            image=self.game_back,
            text="Back",
            compound=tk.LEFT,
            style="Secondary.TButton",
            command=self.confirm_back
        ).grid(row=0, column=0, sticky="w", padx=10)

        self.time_lbl = ttk.Label(
            top,
            text="Time: 0s",
            style="Sub.TLabel",
            relief="solid",
            padding=(20, 5)
        )
        self.time_lbl.grid(row=0, column=1)

        ttk.Button(
            top,
            text="Restart",
            style="Secondary.TButton",
            command=self.restart_game
        ).grid(row=0, column=2, sticky="e", padx=10)

        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=5)

        # ======================================================
        # GRID
        # ======================================================
        self.grid_frame = ttk.Frame(self, style="App.TFrame")
        self.grid_frame.pack(expand=True, pady=20)

        for i in range(4):
            self.grid_frame.rowconfigure(i, weight=1, uniform="card_grid")
            self.grid_frame.columnconfigure(i, weight=1, uniform="card_grid")

        for i in range(4):
            row_btns = []
            for j in range(4):
                btn = ttk.Button(
                    self.grid_frame,
                    text="",
                    style="Hidden.Memory.TButton",
                    command=lambda r=i, c=j: self.on_card_click(r, c)
                )
                btn.grid(row=i, column=j, padx=8, pady=8, sticky="nsew")
                row_btns.append(btn)
            self.buttons.append(row_btns)

        # ======================================================
        # INFO BOX
        # ======================================================
        self.info_container = ttk.Frame(
            self,
            style="Card.TFrame",
            relief="solid",
            padding=15
        )
        self.info_container.pack(pady=20, side="bottom", fill="x", padx=100)

        self.info_lbl = ttk.Label(
            self.info_container,
            text="Click any card to start!",
            style="Sub.TLabel",
            justify="center"
        )
        self.info_lbl.pack()

        self.reset_timer()

    # ======================================================
    # SIMPLE TIMER (same as guess game)
    # ======================================================
    def start_timer(self):
        if self.timer_running:
            return

        self.timer_running = True
        self.run_timer()

    def run_timer(self):
        if not self.timer_running:
            return

        self.time_elapsed += 1
        self.time_lbl.config(text=f"Time: {self.time_elapsed}s")

        if self.time_elapsed >= 120:
            self.stop_timer()
            self.info_lbl.config(text="Oops! Time up, try again :)")
            showinfo("Game Over", "Oops! Time up, try again :)")
            return

        self.timer_id = self.after(1000, self.run_timer)

    def stop_timer(self):
        self.timer_running = False
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None

    def reset_timer(self):
        self.stop_timer()
        self.time_elapsed = 0
        self.time_lbl.config(text="Time: 0s")

    # ======================================================
    # GAME LOGIC
    # ======================================================
    def on_card_click(self, r, c):
        btn = self.buttons[r][c]

        # ⭐ start timer on first click
        self.start_timer()

        if btn["style"] == "Memory.TButton":
            return

        fruit = self.cards[r * 4 + c]
        btn.config(text=fruit, style="Memory.TButton")

        if self.first_card is None:
            self.first_card = (r, c)
        else:
            r1, c1 = self.first_card
            self.attempts += 1

            if fruit == self.cards[r1 * 4 + c1]:
                self.matches += 1
                self.first_card = None

                if self.matches == 8:
                    self.stop_timer()
                    self.info_lbl.config(
                        text=f"Congrats! Attempts: {self.attempts} | Time: {self.time_elapsed}s"
                    )
            else:
                self.after(500, lambda: self.reset_cards(r, c, r1, c1))
                self.first_card = None

    def reset_cards(self, r1, c1, r2, c2):
        self.buttons[r1][c1].config(text="", style="Hidden.Memory.TButton")
        self.buttons[r2][c2].config(text="", style="Hidden.Memory.TButton")

    # ======================================================
    # RESTART → AUTO START
    # ======================================================
    def restart_game(self):
        random.shuffle(self.cards)

        self.matches = 0
        self.attempts = 0
        self.first_card = None

        for row in self.buttons:
            for btn in row:
                btn.config(text="", style="Hidden.Memory.TButton")

        self.info_lbl.config(text="New Game Started!")

        self.reset_timer()
        self.start_timer()

    # ======================================================
    # BACK → WAIT AGAIN
    # ======================================================
    def confirm_back(self):
        if askyesno("Exit", "Are you sure you want to go back to the main menu?"):
            self.reset_timer()
            self.show_frame("home")