import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb

import mainApp
from queries import Query

label_font = ('Times New Roman', 10)


def exit_clicked(window, user):
    q = Query()
    window.destroy()
    mainApp.mainApp(q.getUserLoginByID(user.idUser))


def confrim_grade(window, nameStudent, numClass, nameSubject, grade, dateOfGrade):
    conf = mb.askokcancel('Выставление оценки', 'Вы уверены, что хотите поставить оценку?')
    if conf:
        q = Query()
        q.put_grade(nameStudent, numClass, nameSubject, grade, dateOfGrade)
        label = Label(window, text='Оценка поставлена    ', font=('Times New Roman', 10, 'bold'), fg="green", bg="white")
        label.grid(column = 1, row = 9, sticky='w')
    else:
        label = Label(window, text='Оценка не поставлена    ', font=('Times New Roman', 10, 'bold'), fg="red", bg="white")
        label.grid(column=1, row=9, sticky='w')


def class_book(window, user):
    window.destroy()
    window = Tk()
    window.title("Расписание")
    window.geometry('500x250')
    window['background'] = 'white'

    exit_button = Button(window, text='Назад', fg="black", bg="white", command=lambda: exit_clicked(window, user))
    exit_button.grid(column=0, row=10, sticky='w')

    q = Query()
    class_box = ttk.Combobox(window, values=q.getClasses(), state='readonly')
    class_box.set('Выберите класс')
    class_box.grid(column=0, row=0, sticky='w')

    def class_chosen(event):
        numClass = class_box.get()
        id_and_name_students = q.getStudentsNamesByClass(numClass)
        student_names = []
        for i in range(len(id_and_name_students)):
            student_names.append(id_and_name_students[i][1])
        students_box = ttk.Combobox(window, values=student_names, state='readonly', width=35)
        students_box.set('Выберите ученика')
        students_box.grid(column=1, row=0, sticky='w')

        def student_chosen(event):
            subjects_box = ttk.Combobox(window, values=q.getTeacherSubjects(user.idLocal), state='readonly')
            subjects_box.set('Выберите предмет')
            subjects_box.grid(column=0, row=1, sticky='w')
            grade_box = ttk.Combobox(window, values=[1, 2, 3, 4, 5], state='readonly', width=17)
            grade_box.set('Выберите оценку')
            grade_box.grid(column=1, row=1, sticky='w')
            date_box = Entry(window, font=label_font, fg="black", bg="white", width=17)
            date_box.insert(1, datetime.datetime.now().strftime("%Y-%m-%d"))
            date_box.grid(column=1, row=1, sticky='e')

            confirm_button = Button(window, text='Выставить оценку', fg="black", bg="white",
                                    command=lambda: confrim_grade(window, students_box.get(), numClass,
                                                                  subjects_box.get(), grade_box.get(), date_box.get()))
            confirm_button.grid(column = 0, row = 9, sticky='w')
        students_box.bind('<<ComboboxSelected>>', student_chosen)

    class_box.bind('<<ComboboxSelected>>', class_chosen)

    window.mainloop()
