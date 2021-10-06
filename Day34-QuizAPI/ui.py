from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score.grid(row=1, column=2)

        self.canvas = Canvas (width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="Question text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row = 2, column=1, columnspan=2, pady = 50)

        correct_i = PhotoImage(file = "E:/Python codes/Day34-QuizAPI/images/true.png")
        self.correct_b = Button(image = correct_i, borderwidth=0, command=self.true_pressed)
        self.correct_b.grid(row=3, column=1)
        false_i = PhotoImage(file = "E:/Python codes/Day34-QuizAPI/images/false.png")
        self.false_b = Button(image = false_i, borderwidth=0, command=self.false_pressed)
        self.false_b.grid(row=3, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="End of the quiz")
            self.correct_b.config(state="disabled")
            self.false_b.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        

