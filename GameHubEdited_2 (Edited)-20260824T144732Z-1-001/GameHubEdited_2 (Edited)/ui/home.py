import tkinter as tk
from tkinter import ttk
from utils.assets import asset

# -----------Window-----------
class HomeFrame(ttk.Frame):
    def __init__(self, parent, show_frame, detail_frame, credits_frame):
        super().__init__(parent, style = "App.TFrame")
        self.show_frame = show_frame
        self.detail_frame = detail_frame
        self.credits_frame = credits_frame

# -----------Style-----------
        # style = ttk.Style()
        # style.theme_use('clam')

        # style.configure('Header.TLabel', font=("Segoe UI", 25, "bold"), pady = 10)
        # style.configure('Sub_Header.TLabel', font=("Segoe UI", 15))
        # style.configure('Button.TButton', font=("Segoe UI", 20, "bold"))
        # # style.configure('Header.TLabel', font=("Segoe UI", 20, "bold"))

        # style.configure('Card.TFrame', relief = 'groove', borderwidth = 2, bordercolor = 'black')
        # style.configure('Title.TLabel', font=("Segoe UI", 20, "bold"), pady = 10)
        # style.configure('Play.TButton', font=("Segoe UI", 15))

# -----------Functions-----------
        def open_credits():
            self.show_frame("credits")

        def open_settings():
            self.show_frame("settings")

# -----------Header-----------
        header = ttk.Frame(master = self, style = 'App.TFrame', padding = 15)
        header.pack(fill = 'x')

        # Title
        heading = ttk.Label(
            master = header, 
            text = "GameHub", 
            style = 'Title.TLabel').pack()
        
        # Sub Title
        sub_heading = ttk.Label(
            master = header, 
            text = "All games in one place", 
            style = 'Sub.TLabel').pack()

        # credits
        self.credits_img = tk.PhotoImage(file = asset('credits.png'))
        credits_btn = ttk.Button(
            master = header, 
            text = "Credits", 
            image = self.credits_img, 
            compound=tk.LEFT,
            style = 'Secondary.TButton',
            command = open_credits
        )
        credits_btn.place(relx=0.98, rely=0.2, anchor="ne")

        # settings
        self.settings_img = tk.PhotoImage(file = asset('settings.png'))
        settings_btn = ttk.Button(
            master = header, 
            text = "Settings", 
            image = self.settings_img, 
            compound=tk.LEFT, 
            style = 'Secondary.TButton', 
            command=open_settings
        )
        settings_btn.place(relx=0.02, rely=0.2, anchor="nw")

# -----------MainBody-----------
        body = ttk.Frame(master = self, style = 'App.TFrame')
        body.pack(fill = 'both', expand = True)

        for i in range(3):
            body.columnconfigure(i, weight=1)

        for i in range(2):
            body.rowconfigure(i, weight=1)

# -----------GameCardFunction-----------
        def game_card(parent, game, game_desc):
            
            def open_game():
                self.detail_frame.load_game(
                        name=game,
                        description=game_desc,
                        game_key=self.game_keys[game]   # later change per game
                )
                self.show_frame("details")
                
            card = ttk.Frame(
                parent,
                style="Card.TFrame",
                padding=30,
                width=400,
                height=200
            )
            card.grid_propagate(False)


            card.rowconfigure(0, weight=1)
            card.rowconfigure(1, weight=0)
            card.rowconfigure(2, weight=1)

            card.columnconfigure(0, weight=0)
            card.columnconfigure(1, weight=1)
    # 🔲 Logo placeholder box
            icon = self.game_icons.get(game)

            if icon:
                icon_label = ttk.Label(card, image=icon)
                icon_label.image = icon  # keep reference
                icon_label.grid(row=0, column=0, rowspan=2, sticky="sw", padx=(15, 15) )
            else:
                # fallback if no image (e.g. Coming Soon)
                placeholder = ttk.Frame(card, width=120, height=120, relief="solid")
                placeholder.grid(row=0, column=0, rowspan=2, sticky="s", padx=(15, 15))
                placeholder.grid_propagate(False)

#-----------TITLE-----------
            ttk.Label(
                card, 
                text=game, 
                style="CardTitle.TLabel")\
            .grid(
                row=0, 
                column=1,
                sticky="w",
                padx=(5, 5),
                pady=(5, 0))

#-----------BUTTON-----------
            ttk.Button(
                card, 
                text="Play", 
                style="Primary.TButton", 
                command=open_game)\
            .grid(row=2, 
                  column=0, 
                  columnspan=2, 
                  sticky="sew",
                  padx=(12),
                  pady=(0,5)
            )

            return card


# -----------GameLayout-----------
        games = [
            "Lucky Guess", 
            "Quiz", 
            "Memory Game", 
            "Tic Tac Toe",
            "Bouncy Ball",
            "Car Racing"
        ]

        game_descriptions = [
            "Try to guess the secret number chosen by the computer within the fewest attempts possible.\nThe game gives hints to guide you closer to the correct answer.",

            "Answer multiple-choice questions across various topics and test your knowledge, accuracy, and decision-making speed.\nThis game helps improve logical thinking, memory, concentration, and overall general awareness through an engaging quiz experience.",

            "Match pairs of cards by remembering their positions on the board.\nThe game challenges your focus, memory, and concentration skills.",

            "Take turns marking the grid to align three symbols in a row.\nThe game challenges your logic, focus, and strategic thinking skills.",

            "Control a bouncing ball and avoid incoming obstacles by timing your jumps precisely.\nThis game helps improve hand-eye coordination, focus, reaction speed, and decision-making under pressure.",

            "This is a simple and interactive car racing game built using Python and the Tkinter library. The player controls a car and must avoid incoming obstacles while racing on a dynamic track. The game features smooth controls, increasing difficulty, score tracking, and an engaging UI, making it a fun demonstration of game logic, event handling, and GUI development in Python."
        ]

        self.game_keys = {
            "Lucky Guess": "guess_game",
            "Quiz": "quiz_game",
            "Memory Game": "memory_game",
            "Tic Tac Toe": "tic_tac_toe",
            "Bouncy Ball": "bouncy_ball",
            "Car Racing": "car_racing",
        }

        # ----------- Game Icons -----------
        self.game_icons = {
            "Lucky Guess": tk.PhotoImage(file = asset('guessTheNumber.png')),
            "Quiz": tk.PhotoImage(file = asset('quiz.png')),
            "Memory Game": tk.PhotoImage(file = asset('memoryGame.png')),
            "Tic Tac Toe": tk.PhotoImage(file = asset('ticTacToe.png')),
            "Bouncy Ball": tk.PhotoImage(file = asset('bouncyBall.png')),
            "Car Racing": tk.PhotoImage(file = asset('carRacing.png')),

        }

# For future images
# games = [
#     {"title": "Guess the Number", "icon": "guess.png"},
#     {"title": "Math Solver", "icon": "math.png"},
# ]

        for i, (game, game_desc) in enumerate(zip(games, game_descriptions)):
            r, c = divmod(i,3)
            card = game_card(body, game, game_desc) 
            card.grid(row = r, column = c, sticky = 'nsew', padx = 15, pady = 15)
    

        



