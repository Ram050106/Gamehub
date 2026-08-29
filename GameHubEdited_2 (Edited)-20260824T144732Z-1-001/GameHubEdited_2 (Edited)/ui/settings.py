import tkinter as tk
from tkinter import ttk
import pygame
from utils.assets import asset

pygame.mixer.init()

class SettingsFrame(ttk.Frame):
    def __init__(self, parent, show_frame, theme, root):
        super().__init__(parent, style="App.TFrame")
        self.show_frame = show_frame
        self.theme = theme
        self.root = root

        

        # ---------- STYLE ----------
        # style = ttk.Style()
        # style.theme_use("clam")

        # style.configure("Title.TLabel", font=("Segoe UI", 34, "bold"))
        # style.configure("Item.TLabel", font=("Segoe UI", 18))
        # style.configure("Card.TFrame", background="#f4f4f4")

        # ---------- TOP BAR ----------
        top = ttk.Frame(self, style="App.TFrame", padding=10)
        top.pack(fill="x", pady=(10, 10))

        # Back Button
        self.Back_image = tk.PhotoImage(file = asset('back.png'))
        self.settings_btn = ttk.Button(
            top,
            text="Back",
            style = "Secondary.TButton",
            image=self.Back_image,
            compound=tk.LEFT,
            command=lambda: self.show_frame("home")
        )
        self.settings_btn.place(relx=0.02, rely=0.2, anchor="nw")

        # Title
        self.label = ttk.Label(
            top,
            text="Settings",
            style="Title.TLabel"
        )
        self.label.pack()

        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=(10,0))

        # ---------- BODY ----------
        body = ttk.Frame(self, style="App.TFrame")
        body.pack(fill="both", expand=True)

        # ---------- SETTINGS CARD ----------
        card = ttk.Frame(
            body,
            style = "Card.TFrame",
            width=900,
            height=500
        )
        card.pack(fill="both", expand=True, padx=50, pady=50)
        # card.place(relx=0.5, rely=0.5, anchor="center")
        # card.pack_propagate(False)

        # Grid layout inside card
        card.columnconfigure(0, weight=1)
        card.columnconfigure(1, weight=1)
        
        card.rowconfigure(0, weight=0, pad=20)
        card.rowconfigure(1, weight=0)
        card.rowconfigure(2, weight=0)
        card.rowconfigure(3, weight=1)

        # ---------- SETTINGS CONTENT ----------

# -------------Toggle Images------------
        self.on = tk.PhotoImage(file="assets/on.png")
        self.off = tk.PhotoImage(file="assets/off.png")

# -------------States------------
        global music_is_on
        music_is_on = True
        pygame.mixer.music.load("assets/music.mp3")
        pygame.mixer.music.play(loops = 0)

#-------------Music--------------
        # Music Name
        self.music = ttk.Label(
            card, 
            text = "Music", 
            style="Name.TLabel"
            )\
            .grid(row=0, column=0, padx=60, pady=20)
        
        # Definition
        def switchMusic():
            global music_is_on
            
            if music_is_on:
                self.music_btn.config(image=self.off)
                pygame.mixer.music.stop()
                music_is_on = False

            else:
                self.music_btn.config(image=self.on)
                pygame.mixer.music.load("assets/music.mp3")
                pygame.mixer.music.play(loops = 0)
                music_is_on = True

        # Mudic Button
        self.music_btn = ttk.Button(
            card,
            image = self.on,
            style = "Button.TButton",
            command = switchMusic
        )
        self.music_btn.grid(row=0, column=1, padx=60)

#-------------Visibility--------------

        self.mode_label = ttk.Label(
            card,
            text = "Dark Mode",
            style="Name.TLabel"
            )\
            .grid(row=1, column=0, padx=60, pady=20)
        
        def switchMode():
            self.theme.toggle_theme()
            if self.theme.is_dark():
                self.mode_btn.config(image=self.on)
                
            else:
                self.mode_btn.config(image=self.off)
                

        self.mode_btn = ttk.Button(
            card,
            image=self.off,
            style="Button.TButton",
            command=switchMode,
            takefocus=False
        )
        self.mode_btn.grid(row=1, column=1, padx=60)
        
        if self.theme.is_dark():
            self.mode_btn.config(image=self.on)
        
#-------------Fullscreen--------------
        self.fullscreen_is_on = False
        self.fullscreen_label = ttk.Label(
            card,
            text = "Fullscreen",
            style="Name.TLabel"
            )\
            .grid(row=2, column=0, padx=60, pady=20)
        
        def switchFullscreen():
            
            self.fullscreen_is_on = not self.fullscreen_is_on
            self.root.attributes("-fullscreen", self.fullscreen_is_on)

            if self.fullscreen_is_on:
                self.fullscreen_btn.config(image=self.on)

            else:
                self.fullscreen_btn.config(image=self.off)
                

        self.fullscreen_btn = ttk.Button(
            card,
            image = self.off,
            style = "Button.TButton",
            command = switchFullscreen
        )
        self.fullscreen_btn.grid(row=2, column=1, padx=60)
