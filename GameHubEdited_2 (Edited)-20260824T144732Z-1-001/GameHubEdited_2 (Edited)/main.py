import sys
import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ui.home import HomeFrame
from ui.gameInfo import GameDetailFrame
from ui.credits import CreditsFrame
from ui.settings import SettingsFrame
from games.guessTheNumber import GuessNumberGame
from games.quiz import QuizGame
from games.memoryGame import MemoryGame
from games.ticTacToe import TicTacToeGame
from games.bouncyBall import BouncyBallGame
from games.carRacing import CarRacingGame
from theme import ThemeManager
from utils.assets import asset

class GameHubApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.theme = ThemeManager()
# -----------Window-----------
        self.title("GameHub")
        self.window_width = 1350
        self.window_height = 690
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.center_x = int(screen_width/2 - self.window_width / 2)
        self.center_y = int(screen_height/2 - self.window_height / 2)

        self.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')
        # window.resizable(False, False)
        self.minsize(self.window_width, self.window_height)
        
        # Use Pillow to load PNG icon
        pil_icon = Image.open(asset("logo.png"))
        icon = ImageTk.PhotoImage(pil_icon)
        self.iconphoto(False, icon)
        self.icon = icon  # Keep a reference

        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

# -----------Frames-----------
        container = ttk.Frame(self)
        container.pack(expand=True, fill="both")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

# -----------GamePages-----------
        # Guess The Number
        guess_game = GuessNumberGame(container, self.show_frame)
        guess_game.grid(row=0, column=0, sticky="nsew")
        self.frames["guess_game"] = guess_game

        # Quiz
        quiz_game = QuizGame(container, self.show_frame)
        quiz_game.grid(row=0, column=0, sticky="nsew")
        self.frames["quiz_game"] = quiz_game

        # Memory
        memory_game = MemoryGame(container, self.show_frame)
        memory_game.grid(row=0, column=0, sticky="nsew")
        self.frames["memory_game"] = memory_game

        # Tic Tac Toe
        tic_tac_toe = TicTacToeGame(container, self.show_frame)
        tic_tac_toe.grid(row=0, column=0, sticky="nsew")
        self.frames["tic_tac_toe"] = tic_tac_toe

        # Bouncy Ball
        bouncy_ball = BouncyBallGame(container, self.show_frame)
        bouncy_ball.grid(row=0, column=0, sticky="nsew")
        self.frames["bouncy_ball"] = bouncy_ball

        # Car Racing
        car_racing = CarRacingGame(container, self.show_frame)
        car_racing.grid(row=0, column=0, sticky="nsew")
        self.frames["car_racing"] = car_racing

# -----------SettingsPage-----------
        settings = SettingsFrame(container, self.show_frame, self.theme, self)
        settings.grid(row=0, column=0, sticky="nsew")
        self.frames["settings"] = settings

# -----------CreditsPage-----------
        credits = CreditsFrame(container, self.show_frame, self.theme)
        credits.grid(row=0, column=0, sticky="nsew")
        self.frames["credits"] = credits

# -----------GameDetailPage-----------
        detail = GameDetailFrame(container, self.show_frame, self.theme)
        detail.grid(row=0, column=0, sticky="nsew")
        self.frames["details"] = detail

# -----------HomePages-----------
        home = HomeFrame(container, self.show_frame, detail, credits)
        home.grid(row=0, column=0, sticky="nsew")
        self.frames["home"] = home

        self.show_frame("home")

        
    def show_frame(self, frame_name):
        frame = self.frames[frame_name]

        if hasattr(frame, "on_show"):
                frame.on_show()

        frame.tkraise()




            
if __name__ == "__main__":
    app = GameHubApp()
    app.mainloop()

