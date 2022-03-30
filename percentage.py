from tkinter import *

root = Tk()
root.title("Percentage Calculator")
root.geometry("400x400")
root.configure(background="AliceBlue")

grade_1_percentage = Label(root)
grade_1_percentage.place(relx=0.5, rely=0.2, anchor=CENTER)

grade_2_percentage = Label(root)
grade_2_percentage.place(relx=0.5, rely=0.4, anchor=CENTER)

grade_3_percentage = Label(root)
grade_3_percentage.place(relx=0.5, rely=0.6, anchor=CENTER)

class grade_1:
    def __init__(self, language_arts, mathematics):
        self.language_arts = Language
        self.mathematics = Math
    def percentage(self.Language, self.Math):
        total_marks = self.Language + self.Math * 100
        grade_1_percentage = total_marks / 200

root.mainloop()