import tkinter
from tkinter import *
from tkinter import ttk

import login
import mainApp
import progress
import timetable
from queries import Query
import tkinter.messagebox as mb

label_font = ('Times New Roman', 10)


def confirm_add_sub(window, name_text, desc_text):
    q =Query()
    try:
        q.addSubject(name_text.get(), desc_text.get())
        window.destroy()
    except Exception:
        wrong_sub_label = Label(window, text='Предмет не добавлен', font=('Times New Roman', 10, 'bold'),
                                 fg="red", bg="white")
        wrong_sub_label.grid(column = 1, row = 10)




def add_subject():
    subs_window = Toplevel()
    subs_window.title('Добавление предмета')
    subs_window.geometry('350x200')
    subs_window['background'] = 'white'
    subs_window.grab_set()

    name_label = Label(subs_window, text='Введите название предмета     ', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row=0, sticky='w')
    name_text = Entry(subs_window, font=label_font, fg="black", bg="white")
    name_text.grid(column=1, row=0, sticky='e')

    desc_label = Label(subs_window, text='Введите описание предмета     ', font=label_font, fg="black", bg="white")
    desc_label.grid(column=0, row=1, sticky='w')
    desc_text = Entry(subs_window, font=label_font, fg="black", bg="white")
    desc_text.grid(column=1, row=1, sticky='e')

    confirm_button = Button(subs_window, text='Подтвердить',fg="black", bg="white", command = lambda: confirm_add_sub(subs_window, name_text, desc_text))
    confirm_button.grid(column=0, row=10, sticky='e')


    exit_button = Button(subs_window, text='Назад', fg="black", bg="white",
                         command=lambda: subs_window.destroy())
    exit_button.grid(column=0, row=10, sticky='w')


def confirm_change_sub(window, name_box, name_text, desc_text, activity_text):
    q = Query()
    try:
        q.changeSubject(name_box.get(), name_text.get(), desc_text.get(), activity_text.get())
        window.destroy()
    except Exception:
        wrong_sub_label = Label(window, text='Предмет не изменен', font=('Times New Roman', 10, 'bold'),
                                fg="red", bg="white")
        wrong_sub_label.grid(column=1, row=10)


def change_subject():
    subs_window = Toplevel()
    subs_window.title('Изменение предметов')
    subs_window.geometry('350x200')
    subs_window['background'] = 'white'
    subs_window.grab_set()
    q= Query()
    name_box = ttk.Combobox(subs_window, values = q.getSubjects(), font=label_font, state='readonly')
    name_box.grid(column=0, row=0, sticky='w')

    def class_chosen(event):
        sub = q.getSubjectByName(name_box.get())
        name_label = Label(subs_window, text='Название предмета     ', font=label_font, fg="black", bg="white")
        name_label.grid(column=0, row=1, sticky='w')
        name_text = Entry(subs_window, font=label_font, fg="black", bg="white")
        name_text.insert(1, sub.NameOfSubject)
        name_text.grid(column=1, row=1, sticky='e')

        desc_label = Label(subs_window, text='Описание предмета     ', font=label_font, fg="black", bg="white")
        desc_label.grid(column=0, row=2, sticky='w')
        desc_text = Entry(subs_window, font=label_font, fg="black", bg="white")
        desc_text.insert(1, sub.Description)
        desc_text.grid(column=1, row=2, sticky='e')

        activity_label = Label(subs_window, text='Активность', font=label_font, fg="black", bg="white")
        activity_label.grid(column=0, row=3, sticky='w')
        activity_text = ttk.Combobox(subs_window, values=[0, 1], state='readonly', width = 10)
        activity_text.set(sub.Activity)
        activity_text.grid(column=1, row=3, sticky='w')

        confirm_button = Button(subs_window, text='Подтвердить', fg="black", bg="white",
                                command=lambda: confirm_change_sub(subs_window, name_box, name_text, desc_text, activity_text))
        confirm_button.grid(column=0, row=10, sticky='e')


    exit_button = Button(subs_window, text='Назад', fg="black", bg="white",
                         command=lambda: subs_window.destroy())
    exit_button.grid(column=0, row=10, sticky='w')

    name_box.bind('<<ComboboxSelected>>', class_chosen)
