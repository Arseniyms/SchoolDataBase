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

def confirm_add_class(window, name_text, desc_text):
    q =Query()
    try:
        q.addClass(name_text.get(), desc_text.get())
        window.destroy()
    except Exception:
        wrong_sub_label = Label(window, text='Класс не добавлен', font=('Times New Roman', 10, 'bold'),
                                 fg="red", bg="white")
        wrong_sub_label.grid(column = 0, row = 11)




def add_class():
    class_window = Toplevel()
    class_window.title('Добавление класса')
    class_window.geometry('350x200')
    class_window['background'] = 'white'
    class_window.grab_set()

    name_label = Label(class_window, text='Введите название класса', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row=0, sticky='w')
    name_text = Entry(class_window, font=label_font, fg="black", bg="white", width=10)
    name_text.grid(column=1, row=0, sticky='e')

    desc_label = Label(class_window, text='Введите максимальное\nколичество учеников', font=label_font, fg="black", bg="white")
    desc_label.grid(column=0, row=1, sticky='w')
    desc_text = Entry(class_window, font=label_font, fg="black", bg="white", width=10)
    desc_text.grid(column=1, row=1, sticky='e')

    confirm_button = Button(class_window, text='Подтвердить',fg="black", bg="white", command = lambda: confirm_add_class(class_window, name_text, desc_text))
    confirm_button.grid(column=0, row=10, sticky='e')


    exit_button = Button(class_window, text='Назад', fg="black", bg="white",
                         command=lambda: class_window.destroy())
    exit_button.grid(column=0, row=10, sticky='w')


def confirm_change_class(window, name_box, name_text, desc_text):
    q = Query()
    try:
        q.changeClass(name_box.get(), name_text.get(), desc_text.get())
        window.destroy()
    except Exception:
        wrong_sub_label = Label(window, text='Класс не изменен', font=('Times New Roman', 10, 'bold'),
                                fg="red", bg="white")
        wrong_sub_label.grid(column=1, row=10)


def change_class():
    subs_window = Toplevel()
    subs_window.title('Изменение классов')
    subs_window.geometry('350x200')
    subs_window['background'] = 'white'
    subs_window.grab_set()
    q= Query()
    name_box = ttk.Combobox(subs_window, values = q.getClasses(), font=label_font, state='readonly')
    name_box.grid(column=0, row=0, sticky='w')

    def class_chosen(event):
        сl = q.getClassByNum(name_box.get())
        name_label = Label(subs_window, text='Название класса', font=label_font, fg="black", bg="white")
        name_label.grid(column=0, row=1, sticky='w')
        name_text = Entry(subs_window, font=label_font, fg="black", bg="white")
        name_text.insert(1, сl.NumClass)
        name_text.grid(column=1, row=1, sticky='e')

        desc_label = Label(subs_window, text='Максимальное количество\nучеников в класса', font=label_font, fg="black", bg="white")
        desc_label.grid(column=0, row=2, sticky='w')
        desc_text = Entry(subs_window, font=label_font, fg="black", bg="white")
        desc_text.insert(1, сl.MaxQuantity)
        desc_text.grid(column=1, row=2, sticky='e')

        confirm_button = Button(subs_window, text='Подтвердить', fg="black", bg="white",
                                command=lambda: confirm_change_class(subs_window, name_box, name_text, desc_text))
        confirm_button.grid(column=0, row=10, sticky='e')


    exit_button = Button(subs_window, text='Назад', fg="black", bg="white",
                         command=lambda: subs_window.destroy())
    exit_button.grid(column=0, row=10, sticky='w')

    name_box.bind('<<ComboboxSelected>>', class_chosen)