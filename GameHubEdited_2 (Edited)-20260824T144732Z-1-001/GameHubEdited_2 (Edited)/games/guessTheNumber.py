import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from utils.assets import asset


class GuessNumberGame(ttk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent, style="App.TFrame")
        self.show_frame = show_frame

        # ======================================================
        # STYLES (YOUR ORIGINAL)
        # ======================================================
        style = ttk.Style()

        style.configure(
            "Timer.TLabel",
            font=("Segoe UI", 16, "bold"),
            foreground="black",
            background="#F8FAFC"
        )

        style.configure(
            "Result.TLabel",
            font=("Segoe UI", 14, "bold"),
            background="white",
            foreground="black"
        )

        # ======================================================
        # GAME STATE
        # ======================================================
        self.secret = random.randint(1, 100)
        self.game_active = True

        self.timer_running = False
        self.timer_id = None
        self.time_elapsed = 0

        # ======================================================
        # TOP NAV BAR (ORIGINAL LOOK)
        # ======================================================
        guess_top_frame = ttk.Frame(self, style="App.TFrame", padding=10)
        guess_top_frame.pack(fill="x", pady=(10, 10))

        guess_top_frame.columnconfigure(0, weight=1)
        guess_top_frame.columnconfigure(1, weight=1)
        guess_top_frame.columnconfigure(2, weight=1)

        # Back button
        self.game_back = tk.PhotoImage(file=asset('back.png'))

        ttk.Button(
            guess_top_frame,
            image=self.game_back,
            text="Back",
            compound=tk.LEFT,
            style="Secondary.TButton",
            command=self.confirm_back
        ).grid(row=0, column=0, sticky="w", padx=10)

        # Timer label
        self.time_lbl = ttk.Label(
            guess_top_frame,
            text="Time: 0s",
            style="Timer.TLabel"
        )
        self.time_lbl.grid(row=0, column=1)

        # Restart button
        ttk.Button(
            guess_top_frame,
            text="Restart",
            style="Secondary.TButton",
            command=self.restart_game
        ).grid(row=0, column=2, sticky="e", padx=10)

        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=5)

        # ======================================================
        # MAIN CARD (ORIGINAL LOOK)
        # ======================================================
        card = ttk.Frame(self, style="Card.TFrame", padding=(100, 40))
        card.pack(expand=True, pady=20)

        ttk.Label(
            card,
            text="Guess the number between 1 and 100",
            style="CardTitle.TLabel"
        ).pack(pady=(0, 25))

        self.entry = ttk.Entry(
            card,
            font=("Segoe UI", 14),
            justify="center",
            width=25
        )
        self.entry.pack(pady=10)
        self.entry.focus()

        # ⭐ Start timer only when user clicks entry
        self.entry.bind("<FocusIn>", self.start_timer)

        ttk.Button(
            card,
            text="Guess",
            style="Primary.TButton",
            command=self.check_guess
        ).pack(pady=15)

        self.result_container = ttk.Frame(card, style="Card.TFrame", padding=15)
        self.result_container.pack(pady=20, fill="x")

        self.result_lbl = ttk.Label(
            self.result_container,
            text="Click the box to start!",
            style="Result.TLabel",
            justify="center"
        )
        self.result_lbl.pack()

        self.reset_timer()

    # ======================================================
    # SIMPLE CLEAN TIMER (NEW BUT SAFE)
    # ======================================================
    def start_timer(self, event=None):
        if self.timer_running:
            return

        self.timer_running = True
        self.run_timer()

    def run_timer(self):
        if not self.timer_running:
            return

        self.time_elapsed += 1
        self.time_lbl.config(text=f"Time: {self.time_elapsed}s")

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
    def check_guess(self):
        if not self.game_active:
            return

        value = self.entry.get()

        if not value.isdigit():
            self.result_lbl.config(text="Enter a valid number")
            return

        guess = int(value)

        if guess < self.secret:
            self.result_lbl.config(text="Too low!")
        elif guess > self.secret:
            self.result_lbl.config(text="Too high!")
        else:
            self.result_lbl.config(text="Congrats! You guessed it right!!")
            self.stop_timer()
            self.game_active = False

        self.entry.delete(0, tk.END)

    # ======================================================
    # RESTART → AUTO START
    # ======================================================
    def restart_game(self):
        self.secret = random.randint(1, 100)
        self.game_active = True

        self.entry.delete(0, tk.END)
        self.result_lbl.config(text="Game Restarted!")

        self.reset_timer()
        self.start_timer()   # auto start

    # ======================================================
    # BACK → WAIT FOR CLICK
    # ======================================================
    def confirm_back(self):
        if askyesno("Exit", "Are you sure you want to go back to the main menu?"):
            self.reset_timer()
            self.show_frame("home")