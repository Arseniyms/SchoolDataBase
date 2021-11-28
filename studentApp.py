import tkinter
from tkinter import *
import login
import progress
import timetable
from queries import Query
import tkinter.messagebox as mb


def log_out(window):
    window.destroy()
    login.logInForm()


def info_clicked(user):
    info = (user.name + '\nДата рождения: ' + user.dateOfBrith +
            '\nЭл.почта: ' + user.mail + '\nНомер телефона родителя: ' + user.parentPhoneNumber + '\nКласс: ' + user.numClass)
    mb.showinfo("Информация", info)

def studentApp(login):
    window = tkinter.Tk()
    window.title("Добро пожаловать в школу!")
    window.geometry('400x250')
    window['background'] = 'white'
    q = Query()
    idUser = q.getUserIdByLogin(login)
    user = q.getUserInfo(idUser)

    text = user.status + ' ' + user.numClass + ' класса\n' + user.name + '\n' + user.mail

    info = tkinter.Text(window, fg="black", bg="white", height=3, width=30)
    info.insert(1.0, text)
    info.configure(state='disable')
    info.grid(sticky="E", column=0, row=0)

    info_button = Button(window, text='Посмотреть информацию', fg="black", bg="white",
                         command=lambda: info_clicked(user))
    info_button.grid(sticky="W", column=1, row=0)

    timetable_button = Button(window, text='Посмотреть расписание', fg="black", bg="white",
                              command=lambda: timetable.show_table_for_student(window, user))
    timetable_button.grid(sticky="W", column=0, row=1)

    grades_button = Button(window, text='Посмотреть успеваемость', fg="black", bg="white",
                           command=lambda: progress.showProgress(window, user))
    grades_button.grid(sticky="W", column=0, row=2)

    log_out_button = Button(window, text='Выйти', fg="black", bg="white", command=lambda: log_out(window))
    log_out_button.grid(sticky="W", column=0, row=10)


    window.mainloop()