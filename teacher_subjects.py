import tkinter
from tkinter import *
from tkinter import ttk

import dir_class
import dir_subjects
import login
import mainApp
import progress
import timetable
from queries import Query
import tkinter.messagebox as mb
label_font = ('Times New Roman', 10)


def conirm_anchor(window, teach_box, sub_box):

    q = Query()
    idTeach = q.getidTeacherByName(teach_box.get())
    idSub = q.getSubjectByName(sub_box.get()).idSubject
    q.anchorTeacher(idTeach, idSub)
    label = Label(window, text='Учитель добавлен', font = ('Times New Roman', 10, 'bold'),fg="green", bg="white")
    label.grid(sticky="W", column=2, row=3)


def anchor_teacher(window):
    window = Toplevel()
    window.title("Закрепление учителя")
    window.geometry('490x250')
    window['background'] = 'white'

    label = Label(window, text='Выберите учителя или предмет', fg="black", bg="white")
    label.grid(sticky="W", column=0, row=0)
    q = Query()
    teach_box = ttk.Combobox(window, values=q.getTeachersNames(), state='readonly')
    teach_box.grid(sticky="W", column=0, row=1)

    def teach_selected(event):
        sub_box = ttk.Combobox(window, values=q.getSubjects(), state='readonly')
        sub_box.grid(sticky="W", column=1, row=1)

        def sub_selected(event):
            confirm_button =  Button(window, text='Закрепить учителя', fg="black", bg="white",
                             command=lambda: conirm_anchor(window, teach_box, sub_box))
            confirm_button.grid(sticky="W", column=0, row=5)

            

        sub_box.bind('<<ComboboxSelected>>', sub_selected)
    teach_box.bind('<<ComboboxSelected>>', teach_selected)
    exit_button = Button(window, text='Назад', fg="black", bg="white",
                         command=lambda: window.destroy())
    exit_button.grid(column=0, row=10, sticky='w')
    window.mainloop()



def show_teacher_subjects(window):
    teach_sub_window=Toplevel(window)
    teach_sub_window.title("Закрепленные учителя")
    teach_sub_window.geometry('600x250')
    teach_sub_window['background'] = 'white'

    label = Label(teach_sub_window, text='Выберите учителя или предмет', fg="black", bg="white")
    label.grid(sticky="W", column=0, row=0)
    q = Query()
    teach_box = ttk.Combobox(teach_sub_window, values=q.getTeachersNames(), state='readonly')
    teach_box.grid(sticky="W", column=0, row=1)
    sub_box = ttk.Combobox(teach_sub_window, values=q.getSubjects(), state='readonly')
    sub_box.grid(sticky="W", column=1, row=1)
    label = Label(teach_sub_window, text='', font=label_font, fg="black", bg="white", anchor='w', justify=LEFT)

    def teach_selected(event):
        label.grid(sticky="W", column=1, row=2)
        subjects = q.getTeacherSubjects(q.getidTeacherByName(teach_box.get()))
        text = ''
        for s in subjects:
            text += str(s) + '\n'

        label.config(text=text)
        label.grid(sticky="W", column=1, row=10)


    def sub_selected(event):
        label.grid(sticky="W", column=1, row=2)
        subjects = q.getSubjectTeachers(sub_box.get())
        text = ''
        for s in subjects:
            text += str(s) + '\n'

        label.config(text=text)
        label.grid(sticky="W", column=1, row=10)

    teach_box.bind('<<ComboboxSelected>>', teach_selected)
    sub_box.bind('<<ComboboxSelected>>', sub_selected)


    exit_button = Button(teach_sub_window, text='Назад', fg="black", bg="white",
                         command=lambda: teach_sub_window.destroy())
    exit_button.grid(column=0, row=10, sticky='w')
    teach_sub_window.mainloop()