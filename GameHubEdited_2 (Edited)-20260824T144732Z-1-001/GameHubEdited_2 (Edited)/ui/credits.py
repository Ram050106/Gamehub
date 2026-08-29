import tkinter as tk
from tkinter import ttk
from utils.assets import asset


class CreditsFrame(ttk.Frame):
    def __init__(self, parent, show_frame, theme):
        super().__init__(parent, style = "App.TFrame")
        self.show_frame = show_frame
        self.theme = theme


        # ---------- Style --------------
        # style = ttk.Style()
        # style.theme_use('clam')

        # style.configure("Credits_Title.TLabel", font=("Segoe UI", 36, "bold"))
        # style.configure("Credits_Button.TButton", font=("Segoe UI", 20))
        
        # style.configure("Credits_Name.TLabel", font=("Segoe UI", 19, "bold"))
        # style.configure("Credits_Role.TLabel", font=("Segoe UI", 13))

        # ---------- Frames -------------
        # TopFrame
        credits_top_frame = ttk.Frame(self, style="App.TFrame", padding=10)
        credits_top_frame.pack(fill="x", pady=(10, 10))

        # Seperator
        credits_seperator = ttk.Separator(self, orient = "horizontal")
        credits_seperator.pack(fill="x", pady=10)

        # MiddleFrame
        credits_bottom_frame = ttk.Frame(self, style="App.TFrame", padding=10)
        credits_bottom_frame.pack(fill="both", expand=True)
        credits_content = ttk.Frame(credits_bottom_frame, style="App.TFrame")
        credits_content.pack(expand=True)

        # Seperator
        credits_seperator = ttk.Separator(self, orient = "horizontal")
        credits_seperator.pack(fill="x", pady=10)

        # BottomFrame
        credits_footer = ttk.Frame(self, style="App.TFrame", padding=10)
        credits_footer.pack(fill="x", pady=(10, 10))

        # ---------- UI -----------------
        # Credits Title
        self.credits_title = ttk.Label(credits_top_frame, text="Credits", style="Title.TLabel")
        self.credits_title.pack()

        # Credits Back
        self.credits_back = tk.PhotoImage(file = asset('back.png'))
        self.credits_btn = ttk.Button(
            credits_top_frame,
            text="Back",
            image = self.credits_back,
            compound = tk.LEFT,
            style = "Secondary.TButton",
            command=lambda: self.show_frame("home"))
        self.credits_btn.place(relx=0.02, rely=0.2, anchor="nw")

        # Credits Text
        self.add_name(credits_content, "Ram Addagatla", "Car Racing Game: UI, Game Logic, and Implementation\nQuiz Game: Game Logic and Implementation")

        self.add_name(credits_content, "Mehek Lakhamje", "Application structure, navigation and complete UI development\n(Home, Credits, Settings, Game details, Game Pages Framework, Quiz Game UI)")

        self.add_name(credits_content, "Shruti Pandey", "Lucky Guess and Memory Game: Game Logic, UI, and Implementation")

        self.add_name(credits_content, "Tushar Dileep", "Tic Tac Toe and Bouncy Ball: Game Logic, UI, and Implementation")

        # Credits Footer
        ttk.Label(
            credits_footer,
            text="Built using Python • Tkinter (ttk) • VS Code",
            font=("Segoe UI", 11),
            foreground="gray",
            style = "Credits.TLabel"
        ).pack()

        ttk.Label(
            credits_footer,
            text="© 2025 GameHub",
            font=("Segoe UI", 10),
            foreground="gray",
            style = "Credits.TLabel"
        ).pack(pady=(5, 0))

    # Credits Function
    def add_name(self, parent, name, role):
        block = ttk.Frame(parent, style="Credits.TFrame")
        block.pack(pady=(20,20))   

        ttk.Label(
            block, text=name, style="CreditsName.TLabel"
        ).pack(pady=(0, 2))

        ttk.Label(
            block, text=role, style="Desc.TLabel", justify="center", wraplength=700
        ).pack()
        # ttk.Label(parent, text=name, style="Credits_Name.TLabel").pack(pady=(10, 2))
        # ttk.Label(parent, text=role, style="Credits_Role.TLabel", justify="center").pack(pady=(10, 4))
