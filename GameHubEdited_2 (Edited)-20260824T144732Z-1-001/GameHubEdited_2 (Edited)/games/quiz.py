import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, askquestion
import random


class QuizGame(ttk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent, style="App.TFrame")
        self.show_frame = show_frame

        self.selected_answer = tk.IntVar(value=-1)
        self.current_question = 0
        self.score = 0

        self.build_layout()
        self.load_questions()
        self.display_question()

    # ---------------- LAYOUT ---------------- #

    def build_layout(self):
        header = ttk.Frame(self, padding=10, style="App.TFrame", height=70)
        header.pack(fill="x", pady=(10, 10))
        header.pack_propagate(False)

        quizButton = ttk.Button(
            header,
            text="← Back",
            style="Secondary.TButton",
            command=self.confirm_exit
        )
        quizButton.place(relx=0.02, rely=0.2, anchor="nw")

        self.title_label = ttk.Label(
            header,
            text="Question 1 of 10",
            style="QuizTitle.TLabel"
        )
        self.title_label.pack()

        ttk.Button(
            header,
            text="Restart",
            style="Secondary.TButton",
            command=self.restart_quiz
        ).place(relx=0.98, rely=0.2, anchor="ne")

        ttk.Separator(self).pack(fill="x", pady=10)

        score_frame = ttk.Frame(self, style="App.TFrame")
        score_frame.pack(fill="x")

        self.score_label = ttk.Label(
            score_frame,
            text="Score: 0/10",
            style="Score.TLabel"
        )
        self.score_label.pack(anchor="e", padx=30)

        card = ttk.Frame(self, style="Card.TFrame", padding=25)
        card.pack(fill="both", expand=True, padx=40, pady=40)

        self.question_label = ttk.Label(
            card,
            style="CardTitle.TLabel",
            wraplength=700,
            justify="center"
        )
        self.question_label.pack(pady=(10, 25))

        self.options_frame = ttk.Frame(card, style="QuizFrame.TFrame")
        self.options_frame.pack()

    # ---------------- QUESTIONS ---------------- #

    def load_questions(self):
        self.questions = random.sample([
            {
                "question": "Which data structure uses LIFO (Last In First Out)?",
                "options": ["Queue", "Stack", "Array", "Tree"],
                "answer": 1
            },
            {
                "question": "What does CPU stand for?",
                "options": [
                    "Central Processing Unit",
                    "Computer Power Unit",
                    "Central Program Unit",
                    "Control Processing Unit"
                ],
                "answer": 0
            },
            {
                "question": "Which language runs in a web browser?",
                "options": ["Python", "Java", "C++", "JavaScript"],
                "answer": 3
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["func", "define", "def", "function"],
                "answer": 2
            },
            {
                "question": "Which file extension is used for Python files?",
                "options": [".pt", ".py", ".pyt", ".python"],
                "answer": 1
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["//", "/* */", "#", "<!-- -->"],
                "answer": 2
            },
            {
                "question": "Which HTML tag is used to create a hyperlink?",
                "options": ["<link>", "<a>", "<href>", "<url>"],
                "answer": 1
            },
            {
                "question": "Which CSS property controls text color?",
                "options": ["text-color", "font-color", "color", "foreground"],
                "answer": 2
            },
            {
                "question": "Which loop is best when the number of iterations is known?",
                "options": ["while", "do-while", "for", "repeat"],
                "answer": 2
            },
            {
                "question": "Which JavaScript keyword is used to declare a constant?",
                "options": ["var", "let", "const", "static"],
                "answer": 2
            }
        ], 10)

    # ---------------- DISPLAY ---------------- #

    def display_question(self):
        self.selected_answer.set(-1)

        q = self.questions[self.current_question]
        self.title_label.config(
            text=f"Question {self.current_question + 1} of {len(self.questions)}"
        )
        self.question_label.config(text=q["question"])

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for i, option in enumerate(q["options"]):
            self.create_option(i, option)

    def create_option(self, index, text):
        card = ttk.Frame(self.options_frame, style="OptionCard.TFrame")
        card.pack(fill="x", pady=6, padx=150)

        label = ttk.Label(
            card,
            text=text,
            style="OptionText.TLabel",
            wraplength=850,
            justify="center"
        )
        label.pack(pady=15, padx=200)

        card.bind("<Button-1>", lambda e: self.select_option(index, card, label))
        label.bind("<Button-1>", lambda e: self.select_option(index, card, label))
        card.bind("<Enter>", lambda e: card.configure(cursor="hand2"))

    def select_option(self, index, card, label):
        self.selected_answer.set(index)

        for child in self.options_frame.winfo_children():
            child.configure(style="OptionCard.TFrame")
            for lbl in child.winfo_children():
                lbl.configure(style="OptionText.TLabel")

        card.configure(style="OptionSelected.TFrame")
        label.configure(style="OptionSelected.TLabel")

        self.after(300, self.next_question)

    # ---------------- LOGIC ---------------- #

    def next_question(self):
        correct = self.questions[self.current_question]["answer"]
        if self.selected_answer.get() == correct:
            self.score += 1
            self.score_label.config(
                text=f"Score: {self.score}/{len(self.questions)}"
            )

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        percent = int((self.score / len(self.questions)) * 100)
        result = askquestion(
            "Quiz Complete",
            f"Score: {self.score}/{len(self.questions)}\nPercentage: {percent}%\n\nPlay again?"
        )
        if result == "yes":
            self.restart_quiz()
        else:
            self.show_frame("home")

    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        self.score_label.config(text="Score: 0/10")
        self.load_questions()
        self.display_question()

    def confirm_exit(self):
        if askyesno("Exit", "Are you sure you want to go back to the main menu?"):
            self.show_frame("home")
