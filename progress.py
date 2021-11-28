from tkinter import *
from tkinter import ttk

import mainApp
from queries import Query

label_font = ('Times New Roman', 10)

def exit_clicked(window, user):
    q = Query()
    window.destroy()
    mainApp.mainApp(q.getUserLoginByID(user.idUser))



def showProgress(window, user):
    window.destroy()
    window = Tk()
    window.title("Успеваемость")
    window.geometry('500x250')
    window['background'] = 'white'

    q = Query()
    class_box = ttk.Combobox(window, values=q.getClasses(), state='readonly')
    class_box.set('Выберите класс')
    class_box.grid(column=0, row=0, sticky='w')

    exit_button = Button(window, text='Назад', fg="black", bg="white", command=lambda: exit_clicked(window, user))
    exit_button.grid(column = 0, row = 10, sticky='w')

    grades_label = Label(window, text='', justify=LEFT, font=label_font, fg="black", bg="white")

    def class_chosen(event):
        numClass = class_box.get()
        grades = q.getProgressForClass(numClass)
        grades_label.grid_forget()
        grades_label.grid(column=0, row=1, sticky='w')
        grades_label.configure(text='')
        grades_label.grid(column=0, row=1, sticky='w')

        id_and_name_students = q.getStudentsNamesByClass(numClass)
        student_names = []
        for i in range(len(id_and_name_students)):
            student_names.append(id_and_name_students[i][1])
        students_box = ttk.Combobox(window, values=student_names, state='readonly', width=35)
        students_box.set('Выберите ученика')
        students_box.grid(column=1, row=0, sticky='w')


        if len(grades) != 0:
            text = grades[0][0] + '\n\t'
            text += grades[0][1] + ': '+ str(grades[0][2]) + ' '
            for i in range(len(grades) - 1):
                if grades[i][0] != grades[i+1][0]:
                    text += '\n' + (grades[i + 1][0]) # предмет
                if grades[i][1] != grades[i+1][1]:
                    text += "\n\t" + (grades[i + 1][1]) + ': ' # ученик
                text += str(grades[i+1][2]) + ' ' # оценка
            grades_label.configure(text=text)
            grades_label.grid(column = 0, row=1, sticky='w')
            def student_chosen(event):
                text = ''
                if len(grades) != 0:
                    text += grades[0][0] + ': '
                    if grades[0][1] == students_box.get():
                        text += str(grades[0][2]) + ' '
                    for i in range(len(grades) - 1):
                        if grades[i][0] != grades[i+1][0]:
                            text += '\n' + grades[i+1][0] + ': ' # предмет
                        if grades[i + 1][1] == students_box.get(): # ученик
                            text += str(grades[i + 1][2]) + ' '
                    grades_label.configure(text=text)
                    grades_label.grid(column=0, row=1, sticky='w')

            students_box.bind('<<ComboboxSelected>>', student_chosen)

    class_box.bind('<<ComboboxSelected>>', class_chosen)

    window.mainloop()
