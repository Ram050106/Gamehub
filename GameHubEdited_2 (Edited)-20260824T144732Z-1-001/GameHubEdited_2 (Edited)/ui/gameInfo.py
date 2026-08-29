import tkinter as tk
from tkinter import ttk

class GameDetailFrame(ttk.Frame):
    def __init__(self, parent, show_frame, theme):
        super().__init__(parent, style = "App.TFrame")
        self.show_frame = show_frame
        self.theme = theme

        # Store which game to launch
        self.current_game = None

# ---------- Frames ----------
        top_frame = ttk.Frame(self, style = "App.TFrame", padding=20)
        top_frame.pack(fill="x", pady=(30, 5))

        # Description
        desc_inner = ttk.Frame(
            self,
            padding=25,
            style="Card.TFrame"
        )
        desc_inner.pack(fill="x", padx = 100)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(fill="x", pady=15)

        # Spacer above buttons
        ttk.Frame(self).pack(expand=True)

        bottom_frame = ttk.Frame(self, style = "App.TFrame", padding=20)
        bottom_frame.pack(fill="both", pady=(30, 30))

        # Spacer below buttons
        ttk.Frame(self).pack(expand=True)

# ---------- Style -----------
        # style = ttk.Style()
        # style.theme_use('clam')

        # style.configure("game_Info_Title.TLabel", font=("Segoe UI", 36, "bold"))
        # style.configure("game_Info_SubTitle.TLabel", font=("Segoe UI", 16))
        # style.configure("game_Info_Button.TButton", font=("Segoe UI", 20))

# ---------- UI --------------
        # Title
        self.title_label = ttk.Label(
            top_frame, text="", 
            style="Title.TLabel"
        )
        self.title_label.pack()
        
        self.desc_label = ttk.Label(
            desc_inner, 
            text="", 
            style = "GameDesc.TLabel", 
            wraplength=800, 
            justify="center"
        )
        self.desc_label.pack(pady=(10))

        # Center container for buttons
        center_buttons = ttk.Frame(bottom_frame, style="App.TFrame")
        center_buttons.pack(expand=True)
        # Buttons
        ttk.Button(
            bottom_frame, 
            text="Play", 
            style = "Play.TButton",
            width=24,
            command=self.play_game
        ).pack(pady=(10,20))

        ttk.Button(
            bottom_frame, 
            text="Back",
            style = "Back.TButton",
            width=24,
            command=lambda: self.show_frame("home")
        ).pack()

    # ---------- Update content ----------
    def load_game(self, name, description, game_key):
        self.title_label.config(text=name)
        self.desc_label.config(text=description)
        self.current_game = game_key

    def play_game(self):
        if self.current_game:
            self.show_frame(self.current_game)
