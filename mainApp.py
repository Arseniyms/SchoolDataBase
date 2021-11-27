import tkinter
from tkinter import *

import login
from queries import *


def log_out(window):
    window.destroy()
    login.logInForm()


def confirm_change(window, user, name_text, date_text, phone_text, mail_text):
    q = Query()
    print(name_text.get())
    q.changeInfoOfUser(user.idLocal, name_text.get(), date_text.get(), phone_text.get(), mail_text.get(),)

    window.destroy()
    mainApp(q.getUserLoginByID(user.idUser))


def exit_click(window, user):
    q = Query()
    window.destroy()
    mainApp(q.getUserLoginByID(user.idUser))


def change_info(window, user):
    window.destroy()
    window = Tk()
    window.title('Изменение информации')
    window.geometry('400x250')
    window['background'] = 'white'
    label_font = ('Times New Roman', 10)
    name_label = Label(window, text='Введите информацию, которую хотите изменить    ', font=label_font, fg="black",
                       bg="white")
    name_label.grid(column=0, row=0)
    name_label = Label(window, text='Имя', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row=1, sticky='w')
    name_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    name_text.insert(1, user.name)
    name_text.grid(column=0, row=1, sticky='e')

    date_label = Label(window, text='Дата рождения', font=label_font, fg="black", bg="white")
    date_label.grid(column=0, row=2, sticky='w')
    date_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    date_text.insert(1, user.dateOfBrith)
    date_text.grid(column=0, row=2, sticky='e')

    phone_label = Label(window, text='Номер телефона', font=label_font, fg="black", bg="white")
    phone_label.grid(column=0, row=3, sticky='w')
    phone_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    phone_text.insert(1, user.phoneNumber)
    phone_text.grid(column=0, row=3, sticky='e')

    mail_label = Label(window, text='Эл.почта', font=label_font, fg="black", bg="white")
    mail_label.grid(column=0, row=4, sticky='w')
    mail_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    mail_text.insert(1, user.mail)
    mail_text.grid(column=0, row=4, sticky='e')

    confirm_button = Button(window, text='Подтвердить изменения', fg="black", bg="white",
                            command=lambda: confirm_change(window, user, name_text, date_text, phone_text, mail_text))
    confirm_button.grid(column=0, row=10, sticky='e')

    exit_button = Button(window, text='Выйти', fg="black", bg="white",
                            command=lambda: exit_click(window, user))
    exit_button.grid(column=0, row=10, sticky='w')
    window.mainloop()


def mainApp(login):
    window = Tk()
    window.title("Добро пожаловать в школу!")
    window.geometry('400x250')
    window['background'] = 'white'
    q = Query()
    idUser = q.getUserIdByLogin(login)
    user = q.getUserInfo(idUser)

    text = user.status + '\n' + user.name + '\n' + user.mail

    info = Text(window, fg="black", bg="white", height=3, width=30)
    info.insert(1.0, text)
    info.configure(state='disable')
    info.grid(sticky="E", column=0, row=0)

    log_out_button = Button(window, text='Выйти', fg="black", bg="white", command=lambda: log_out(window))
    log_out_button.grid(sticky="W", column=0, row=10)

    change_info_button = Button(window, text='Изменить данные', fg="black", bg="white",
                                command=lambda: change_info(window, user))
    change_info_button.grid(sticky="E", column=0, row=10)
    # def teacherChosen(event):
    #     lbl = Label(window, text=comboTeachers.get())
    #     lbl.grid(column=1, row=0)
    #
    #
    # def studentsChosen(event):
    #     lbl = Label(window, text=comboStudents.get())
    #     lbl.grid(column=1, row=1)

    #
    # comboTeachers = Combobox(window)
    # comboTeachers['state']= 'readonly'
    # comboTeachers.set("Выберите учителя")
    # comboTeachers['values'] = (getTeachersNames())
    # comboTeachers.grid(column=0, row=0)
    #
    # comboStudents = Combobox(window)
    # comboStudents['state']= 'readonly'
    # comboStudents.set("Выберите ученика")
    # comboStudents['values'] = (getStudentsNames())
    # comboStudents.grid(column=0, row=1)
    #
    # comboTeachers.bind('<<ComboboxSelected>>', teacherChosen)
    # comboStudents.bind('<<ComboboxSelected>>', studentsChosen)

    window.mainloop()
