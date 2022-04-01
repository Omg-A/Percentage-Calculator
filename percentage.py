from tkinter import *

root = Tk()
root.title("Percentage Calculator")
root.geometry("400x400")
root.configure(background="AliceBlue")

label_grade_1_percentage = Label(root, bg="AliceBlue")
label_grade_1_percentage.place(relx=0.5, rely=0.3, anchor=CENTER)

label_grade_2_percentage = Label(root, bg="AliceBlue")
label_grade_2_percentage.place(relx=0.5, rely=0.5, anchor=CENTER)

label_grade_3_percentage = Label(root, bg="AliceBlue")
label_grade_3_percentage.place(relx=0.5, rely=0.7, anchor=CENTER)

class grade_1:
    def __init__(self, language_arts, mathematics):
        self.Language = language_arts
        self.Math = mathematics
    def percentage(self):
        total_marks = self.Language + self.Math * 100
        grade_1_percentage = total_marks / 200
        label_grade_1_percentage["text"] =  "Grade 1 Percentage: " + str(grade_1_percentage)

class grade_2:
    def __init__(self, language_arts, mathematics, social):
        self.Language = language_arts
        self.Math = mathematics
        self.Social = social
    def percentage(self):
        total_marks = self.Language + self.Math + self.Social * 100
        grade_2_percentage = total_marks / 300
        label_grade_2_percentage["text"] =  "Grade 2 Percentage: " + str(grade_2_percentage)

class grade_3:
    def __init__(self, language_arts, mathematics, social, art):
        self.Language = language_arts
        self.Math = mathematics
        self.Social = social
        self.Art = art
    def percentage(self):
        total_marks = self.Language + self.Math + self.Social + self.Art * 100
        grade_3_percentage = total_marks / 400
        label_grade_3_percentage["text"] =  "Grade 3 Percentage: " + str(grade_3_percentage)

obj_grade_1 = grade_1(40, 50)
obj_grade_2 = grade_2(50, 40, 30)
obj_grade_3 = grade_3(20, 50, 30, 40)

button_grade_1 = Button(root, text="Grade 1 Percentage", bg="SteelBlue1", command=obj_grade_1.percentage)
button_grade_1.place(relx=0.5, rely=0.2, anchor=CENTER)

button_grade_2 = Button(root, text="Grade 2 Percentage", bg="SteelBlue1", command=obj_grade_2.percentage)
button_grade_2.place(relx=0.5, rely=0.4, anchor=CENTER)

button_grade_3 = Button(root, text="Grade 3 Percentage", bg="SteelBlue1", command=obj_grade_3.percentage)
button_grade_3.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()