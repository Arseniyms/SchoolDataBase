from tkinter import *

import classBook
import login
import progress
from queries import *
import tkinter.messagebox as mb

import timetable

label_font = ('Times New Roman', 10)


def log_out(window):
    window.destroy()
    login.logInForm()


def confirm_change(window, user, name_text, date_text, phone_text, mail_text):
    q = Query()
    q.changeInfoOfUser(user.idLocal, name_text.get(), date_text.get(), phone_text.get(), mail_text.get(), )
    conf = mb.askokcancel("Изменение данных", 'Вы уверены, что хотите изменить данные?')
    if conf:
        window.destroy()
        mainApp(q.getUserLoginByID(user.idUser))


def exit_click(window, user):
    q = Query()
    window.destroy()
    mainApp(q.getUserLoginByID(user.idUser))


def confirm_pass_change(pass_wind, user, old_pass, new_pass, confirm_pass):
    conf = mb.askokcancel("Изменение пароля", 'Вы уверены, что хотите изменить пароль?')
    if conf:
        q = Query()
        login = q.getUserLoginByID(user.idUser)
        ifPass = q.getPassword(login, old_pass.get())
        wrong_pass_label = Label(pass_wind, font=('Times New Roman', 10, 'bold'),
                                 fg="red", bg="white")
        if ifPass:
            if confirm_pass.get() != '' and new_pass.get() == confirm_pass.get():
                q.changePassword(user.idUser, new_pass.get())
                mb.showinfo('Изменение пароля', 'Пароль успешно изменен!')
                pass_wind.destroy()
            else:
                wrong_pass_label.config(text='Пароли не совпадают')
                wrong_pass_label.grid(column=0, row=10, sticky='w')
        else:
            wrong_pass_label.config(text='Неверный пароль      ')
            wrong_pass_label.grid(column=0, row=10, sticky='w')



def password_change(window, user):
    pass_wind = Toplevel()
    pass_wind.title('Изменение информации')
    pass_wind.geometry('350x200')
    pass_wind['background'] = 'white'
    pass_wind.grab_set()

    old_pass_label = Label(pass_wind, text='Старый пароль    ', font=label_font, fg="black", bg="white")
    old_pass_label.grid(column=0, row=0, sticky='w')
    old_pass = Entry(pass_wind, font=label_font, show='*', fg="black", bg="white", width=30)
    old_pass.grid(column=1, row=0, sticky='e')

    new_pass_label = Label(pass_wind, text='Новый пароль    ', font=label_font, fg="black", bg="white")
    new_pass_label.grid(column=0, row=1, sticky='w')
    new_pass = Entry(pass_wind, font=label_font, show='*', fg="black", bg="white", width=30)
    new_pass.grid(column=1, row=1, sticky='e')

    confirm_pass_label = Label(pass_wind, text='Подтвердите пароль    ', font=label_font, fg="black", bg="white")
    confirm_pass_label.grid(column=0, row=2, sticky='w')
    confirm_pass = Entry(pass_wind, font=label_font, show='*', fg="black", bg="white", width=30)
    confirm_pass.grid(column=1, row=2, sticky='e')

    exit_button = Button(pass_wind, text='Назад', fg="black", bg="white",
                         command=lambda: pass_wind.destroy())
    exit_button.grid(column=1, row=10, sticky='w')

    confirm_button = Button(pass_wind, text='Изменить пароль', fg="black", bg="white",
                            command=lambda: confirm_pass_change(pass_wind, user, old_pass, new_pass, confirm_pass))
    confirm_button.grid(column=1, row=10, sticky='e')


def change_info(window, user):
    window.destroy()
    window = Tk()
    window.title('Изменение информации')
    window.geometry('400x250')
    window['background'] = 'white'

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

    password_button = Button(window, text='Изменить пароль', fg="black", bg="white",
                             command=lambda: password_change(window, user))
    password_button.grid(column=0, row=10, sticky='w')

    exit_button = Button(window, text='Отмена', fg="black", bg="white",
                         command=lambda: exit_click(window, user))
    exit_button.grid(column=0, row=11, sticky='w')
    window.mainloop()


def info_clicked(user):
    q = Query()
    info = (user.name + '\nДата рождения: ' + user.dateOfBrith + '\nОпыт работы: ' +
            str(user.experience) + '\nЭл.почта: ' + user.mail + '\nНомер телефона: +' + user.phoneNumber + '\nПредметы: ')
    subjects = q.getTeacherSubjects(user.idLocal)
    for s in subjects:
        if s != subjects[0]:
            info += ', '
        info += s
    mb.showinfo("Информация", info)


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

    info_button = Button(window, text='Посмотреть информацию', fg="black", bg="white",
                         command=lambda: info_clicked(user))
    info_button.grid(sticky="W", column=1, row=0)

    timetable_button = Button(window, text='Посмотреть расписание', fg="black", bg="white", command=lambda: timetable.show_table_for_teacher(window, user))
    timetable_button.grid(sticky="W", column=0, row=1)

    grades_button = Button(window, text='Посмотреть успеваемость', fg="black", bg="white", command=lambda: progress.showProgress(window, user))
    grades_button.grid(sticky="W", column=0, row=2)

    class_book_button = Button(window, text='Открыть журнал', fg="black", bg="white", command=lambda: classBook.class_book(window, user))
    class_book_button.grid(sticky="W", column=0, row=3)

    log_out_button = Button(window, text='Выйти', fg="black", bg="white", command=lambda: log_out(window))
    log_out_button.grid(sticky="W", column=0, row=10)

    change_info_button = Button(window, text='Изменить данные', fg="black", bg="white",
                                command=lambda: change_info(window, user))
    change_info_button.grid(sticky="E", column=1, row=10)

    window.mainloop()
