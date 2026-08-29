import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo
from utils.assets import asset
import random


class TicTacToeGame(ttk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent, style="App.TFrame")
        self.show_frame = show_frame

# ---------- BACK CONFIRM ----------
        def confirm():
            answer = askyesno(
                title="Exit",
                message="Are you sure you want to go back to the main menu?"
            )
            if answer:
                self.reset_game()
                show_frame("home")

# ---------- TOP BAR ----------
        game_top_frame = ttk.Frame(self, padding=15, style="App.TFrame")
        game_top_frame.pack(fill="x")

        ttk.Label(
            game_top_frame,
            text="Tic Tac Toe",
            style="Title.TLabel"
        ).pack()

        self.game_back_img = tk.PhotoImage(file=asset("back.png"))
        ttk.Button(
            game_top_frame,
            text="Back",
            image=self.game_back_img,
            compound=tk.LEFT,
            style="Secondary.TButton",
            command=confirm
        ).place(relx=0.02, rely=0.2, anchor="nw")

        ttk.Button(
            game_top_frame,
            text="Restart",
            style="Secondary.TButton",
            command=self.reset_game
        ).place(relx=0.98, rely=0.2, anchor="ne")

        ttk.Separator(self).pack(fill="x", pady=10)

# ---------- GAME AREA ----------
        self.game_area = ttk.Frame(self, style="App.TFrame")
        self.game_area.pack(expand=True, fill="both")

        self.build_game(self.game_area)

# ---------- FRAME SHOW ----------
    def on_show(self):
        self.reset_game()

# ---------- GAME UI ----------
    def build_game(self, parent):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        self.vs_computer = True

        self.canvases = []

        # Card wrapper (padding FIXED here)
        container = tk.Frame(
            parent,
            bg="#FFFFFF",
            highlightbackground="#E5E7EB",
            highlightthickness=1
        )
        container.pack(expand=True, padx=150, pady=5)

        inner = tk.Frame(container, bg="#1a2332")
        inner.pack(padx=40, pady=40)

        self.status_label = tk.Label(
            inner,
            text="Player X's Turn",
            font=("Segoe UI", 18, "bold"),
            fg="#31c3bd",
            bg="#1a2332"
        )
        self.status_label.pack(pady=(0, 20))

        board_frame = tk.Frame(inner, bg="#1a2332")
        board_frame.pack()

        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                canvas = tk.Canvas(
                    board_frame,
                    width=120,
                    height=120,
                    bg="#1f3641",
                    highlightthickness=0
                )
                canvas.grid(row=i, column=j, padx=8, pady=8)
                canvas.bind("<Button-1>", lambda e, idx=index: self.make_move(idx))
                self.canvases.append(canvas)

# ---------- DRAW ----------
    def draw_x(self, canvas):
        canvas.delete("all")
        canvas.create_line(30, 30, 90, 90, fill="#31c3bd", width=12, capstyle=tk.ROUND)
        canvas.create_line(90, 30, 30, 90, fill="#31c3bd", width=12, capstyle=tk.ROUND)

    def draw_o(self, canvas):
        canvas.delete("all")
        canvas.create_oval(25, 25, 95, 95, outline="#f2b137", width=12)

# ---------- GAME LOGIC ----------
    def make_move(self, index):
        if self.game_over or self.board[index]:
            return

        self.board[index] = self.current_player

        if self.current_player == "X":
            self.draw_x(self.canvases[index])
        else:
            self.draw_o(self.canvases[index])

        if self.check_winner():
            self.game_over = True
            self.status_label.config(
                text=f"Player {self.current_player} Wins! 🎉",
                fg="#31c3bd" if self.current_player == "X" else "#f2b137"
            )
            showinfo("Game Over", f"Player {self.current_player} wins!")
            return

        if "" not in self.board:
            self.game_over = True
            self.status_label.config(text="It's a Tie 🤝", fg="#A8BFC9")
            showinfo("Game Over", "It's a Tie!")
            return

        self.current_player = "O" if self.current_player == "X" else "X"

        if self.vs_computer and self.current_player == "O":
            self.after(500, self.computer_move)
        else:
            self.status_label.config(text="Player X's Turn", fg="#31c3bd")

# ---------- COMPUTER ----------
    def computer_move(self):
        if self.game_over:
            return

    # 1️⃣ Try to WIN
        move = self.find_best_move("O")
        if move is not None:
            self.make_move(move)
            return

    # 2️⃣ Block PLAYER X
        move = self.find_best_move("X")
        if move is not None:
            self.make_move(move)
            return

    # 3️⃣ Take center if available
        if self.board[4] == "":
            self.make_move(4)
            return

    # 4️⃣ Take a corner
        corners = [0, 2, 6, 8]
        available_corners = [i for i in corners if self.board[i] == ""]
        if available_corners:
            self.make_move(random.choice(available_corners))
            return

    # 5️⃣ Random fallback
        empty = [i for i, v in enumerate(self.board) if v == ""]
        if empty:
            self.make_move(random.choice(empty))

    def find_best_move(self, player):
        winning_combinations = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for combo in winning_combinations:
            values = [self.board[i] for i in combo]

            if values.count(player) == 2 and values.count("") == 1:
                return combo[values.index("")]
        return None



# ---------- WIN ----------
    def check_winner(self):
        combos = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for c in combos:
            if self.board[c[0]] == self.board[c[1]] == self.board[c[2]] != "":
                return True
        return False

# ---------- RESET ----------
    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False

        for canvas in self.canvases:
            canvas.delete("all")
            canvas.config(bg="#1f3641")

        self.status_label.config(
            text="Player X's Turn",
            fg="#31c3bd"
        )
