from tkinter import ttk

class ThemeManager:
    def __init__(self):
        self.themes = {
            "modern_blue": {
                "bg": "#F2F2F2",
                "card": "#FFFFFF",
                "primary": "#2563EB",
                "hover": "#1E40AF",
                "secondary": "#E5E7EB",
                "secondary_hover": "#D1D5DB",
                "text": "#111827",
                "muted": "#6B7280",
                "border": "#E5E7EB"
            },

            "dark": {
                "bg": "#0F172A",
                "card": "#1E293B",
                "primary": "#3B82F6",
                "hover": "#25ACEB",
                "secondary": "#334155",
                "secondary_hover": "#475569",
                "text": "#F8FAFC",
                "muted": "#94A3B8",
                "border": "#334155"
            }
        }

        self.current = "modern_blue"
        self.apply()

    def toggle_theme(self):
        self.current = "dark" if self.current == "modern_blue" else "modern_blue"
        self.apply()

    def is_dark(self):
        return self.current == "dark"

    # ---------- Public API ----------
    def get(self, key):
        """Return a color value by role"""
        return self.themes[self.current][key]

    def apply(self):
        """Apply ttk styles globally"""
        style = ttk.Style()
        style.theme_use("clam")

        t = self.themes[self.current]

        # App background
        style.configure("App.TFrame", background=t["bg"])

# ----------Global Styles----------
        # Cards / Containers
        style.configure(
            "Card.TFrame",
            background=t["card"],
            relief="solid",
            borderwidth=1,
            bordercolor=t["border"]
        )

        # Headings
        style.configure(
            "Title.TLabel",
            background=t["bg"],
            foreground=t["text"],
            font=("Segoe UI", 30, "bold"),
            # pady=10 home,
        )

        # Subtext / descriptions
        style.configure(
            "Sub.TLabel",
            background=t["bg"],
            foreground=t["muted"],
            font=("Segoe UI", 12)
        )

        # Card title
        style.configure(
            "CardTitle.TLabel",
            font=("Segoe UI", 20, "bold"),
            foreground=t["text"],
            background=t["card"]
        )

# -------HomePage--------
        # Primary button
        style.configure(
            "Primary.TButton",
            background=t["primary"],
            foreground="white",
            font=("Segoe UI", 14, "bold"),
            padding=10
        )

        # Secondary button
        style.configure(
            "Secondary.TButton",
            background=t["secondary"],
            foreground=t["text"],
            font=("Segoe UI", 13),
            padding=8
        )

        # Hover effect (ttk way)
        style.map(
            "Primary.TButton",
            background=[("active", t["hover"])]
        )

        style.map(
            "Secondary.TButton",
            background=[("active", t["secondary_hover"])]
        )
# -------GameDetails--------
        # Primary button
        style.configure(
            "Play.TButton",
            background=t["primary"],
            foreground="white",
            font=("Segoe UI", 18, "bold"),
            padding=(30, 15)
        )

        # Secondary button
        style.configure(
            "Back.TButton",
            background=t["secondary"],
            foreground=t["text"],
            font=("Segoe UI", 18),
            padding=(25, 12)
        )

        # Hover effect (ttk way)
        style.map(
            "Play.TButton",
            background=[("active", t["hover"])]
        )

        style.map(
            "Back.TButton",
            background=[("active", t["secondary_hover"])]
        )

        style.configure(
            "GameDesc.TLabel",
            background=t["card"],
            foreground=t["muted"],
            font=("Segoe UI", 15)
        )
# -------Credits--------
        # Credits name
        style.configure(
            "CreditsName.TLabel",
            background=t["bg"],
            foreground=t["text"],
            font=("Segoe UI", 20, "bold")
        )

        # Credits role 
        style.configure(
            "Desc.TLabel",
            background=t["bg"],
            foreground=t["muted"],
            font=("Segoe UI", 15)
        )

        style.configure(
            "Credits.TFrame",
            background=t["bg"]
        )
        style.configure(
            "Credits.TLabel",
            background=t["bg"]
        )

# -------Settings--------

        # content
        style.configure(
            "Name.TLabel",
            background=t["card"],
            foreground=t["text"],
            font=("Segoe UI", 18)
        )

        # button
        style.configure(
            "Button.TButton",
            background=t["card"],
            borderwidth=0,
            focuscolor="",
            focusthickness=0,
        )

        style.map(
            "Button.TButton",
            background=[
                ("active", t["card"]),
                ("pressed", t["card"])
            ]
        )

    # -------Quiz Game Style--------

        style.configure(
            "QuizFrame.TFrame",
            background=t["card"],
            borderwidth=0
        )

        style.configure(
            "OptionCard.TFrame",
            background=t["secondary"],
            relief="solid",
            padding=(50, 25),
            borderwidth=1,
        )
        style.map(
            "OptionCard.TFrame",
            background=[("active", t["secondary_hover"])]
        )

        style.configure(
            "OptionText.TLabel",
            background=t["secondary"],
            foreground=t["text"],
            font=("Segoe UI", 15)
        )


        style.configure(
            "OptionSelected.TFrame",
            background=t["primary"],
            borderwidth=0
        )

        style.configure(
            "OptionSelected.TLabel",
            background=t["primary"],
            foreground="white",
            font=("Segoe UI", 14, "bold")
        )


        style.configure(
            "QuizTitle.TLabel",
            background=t["bg"],
            foreground=t["text"],
            font=("Segoe UI", 20, "bold"),
            # pady=10 home,
        )

        style.configure(
            "Score.TLabel",
            background=t["bg"],
            foreground=t["text"],
            font=("Segoe UI", 18, "bold"),
            # pady=10 home,
        )


        