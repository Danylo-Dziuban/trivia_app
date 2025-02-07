import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tk.Label(self.window, text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white', font=('Arial', 10))
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(self.window, height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, width= 299, text='Some question text', font=('Arial', 20, 'italic'), fill='black')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file='images/true.png')
        false_image = tk.PhotoImage(file='images/false.png')

        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()

            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg='white')

        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.canvas.config(bg='white')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        if self.quiz.still_has_questions():
            self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        if self.quiz.still_has_questions():
            self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score_label.config(text=f'Score {self.quiz.score}')

        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

