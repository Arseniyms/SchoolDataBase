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

def log_out(window):
    window.destroy()
    login.logInForm()


def exit_click(window, user):
    q = Query()
    window.destroy()
    director_app(q.getUserLoginByID(user.idUser))

def confirm_change_student(window, user, name_text, date_text, phone_text, mail_text, class_text, activity_text):
    q = Query()
    conf = mb.askokcancel("Изменение данных", 'Вы уверены, что хотите изменить данные?')
    if conf:
        q.changeInfoOfStudent(user.idLocal, name_text.get(), date_text.get(), phone_text.get(), mail_text.get(),
                              class_text.get(), activity_text.get())
        window.destroy()
        director_app(q.getUserLoginByID(user.idUser))

def confirm_change(window, user, name_text, date_text, phone_text, mail_text, activity_text):
    q = Query()
    q.changeInfoOfUser(user.idLocal, name_text.get(), date_text.get(), phone_text.get(), mail_text.get(), activity_text.get())
    conf = mb.askokcancel("Изменение данных", 'Вы уверены, что хотите изменить данные?')
    if conf:
        window.destroy()
        director_app(q.getUserLoginByID(user.idUser))

def confirm_pass_change(pass_wind, user, new_pass, confirm_pass):
    conf = mb.askokcancel("Изменение пароля", 'Вы уверены, что хотите изменить пароль?')
    if conf:
        q = Query()
        wrong_pass_label = Label(pass_wind, font=('Times New Roman', 10, 'bold'),
                                 fg="red", bg="white")
        if confirm_pass.get() != '' and new_pass.get() == confirm_pass.get():
            q.changePassword(user.idUser, new_pass.get())
            mb.showinfo('Изменение пароля', 'Пароль успешно изменен!')
            pass_wind.destroy()
        else:
            wrong_pass_label.config(text='Пароли не совпадают')
            wrong_pass_label.grid(column=0, row=10, sticky='w')



def password_change(window, user):
    pass_wind = Toplevel()
    pass_wind.title('Изменение информации')
    pass_wind.geometry('350x200')
    pass_wind['background'] = 'white'
    pass_wind.grab_set()

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
                            command=lambda: confirm_pass_change(pass_wind, user, new_pass, confirm_pass))
    confirm_button.grid(column=1, row=10, sticky='e')



def change_info_student(window, user):
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
    phone_text.insert(1, user.parentPhoneNumber)
    phone_text.grid(column=0, row=3, sticky='e')

    class_label = Label(window, text='Класс', font=label_font, fg="black", bg="white")
    class_label.grid(column=0, row=4, sticky='w')
    class_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    class_text.insert(1, user.numClass)
    class_text.grid(column=0, row=4, sticky='e')

    mail_label = Label(window, text='Эл.почта', font=label_font, fg="black", bg="white")
    mail_label.grid(column=0, row=5, sticky='w')
    mail_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    mail_text.insert(1, user.mail)
    mail_text.grid(column=0, row=5, sticky='e')

    activity_label = Label(window, text='Активность', font=label_font, fg="black", bg="white")
    activity_label.grid(column=0, row=6, sticky='w')
    activity_text = ttk.Combobox(window, values=[0,1], state='readonly')
    activity_text.set(user.activity)
    activity_text.grid(column=0, row=6, sticky='e')

    confirm_button = Button(window, text='Подтвердить изменения', fg="black", bg="white",
                            command=lambda: confirm_change_student(window, user, name_text, date_text, phone_text, mail_text, class_text, activity_text))
    confirm_button.grid(column=0, row=10, sticky='e')

    password_button = Button(window, text='Изменить пароль', fg="black", bg="white",
                             command=lambda: password_change(window, user))
    password_button.grid(column=0, row=10, sticky='w')

    exit_button = Button(window, text='Отмена', fg="black", bg="white",
                         command=lambda: exit_click(window, user))
    exit_button.grid(column=0, row=11, sticky='w')
    window.mainloop()


def confirm_student(window, login, password, name, dateOfBirth, numClass, parentPhoneNumber, mail):
    q=Query()
    conf = mb.askokcancel('Добавление ученика', 'Вы уверены, что хотите добавить ученика?')
    if conf:
        try:
            q.register_student(login, password,name,dateOfBirth,numClass,parentPhoneNumber,mail)
            label = Label(window, font=('Times New Roman', 10, 'bold'), fg="green", bg="white")
            label.config(text='Пользователь добавлен    ')
            label.grid(column=1, row=100)
        except:
            label = Label(window, font=('Times New Roman', 10, 'bold'), fg="red", bg="white")
            label.config(text='Пользователь не добавлен')
            label.grid(column =1, row = 100)


def reg_stud(window, user):
    window.destroy()
    window = Tk()
    window.title("Регистрация ученика")
    window.geometry('490x250')
    window['background'] = 'white'

    name_label = Label(window, text='Введите информацию    ', font=label_font, fg="black",
                       bg="white")
    name_label.grid(column=0, row=0)
    name_label = Label(window, text='Имя', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row=1, sticky='w')
    name_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    name_text.grid(column=1, row=1, sticky='w')

    date_label = Label(window, text='Дата рождения', font=label_font, fg="black", bg="white")
    date_label.grid(column=0, row=2, sticky='w')
    date_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    date_text.grid(column=1, row=2, sticky='w')

    phone_label = Label(window, text='Номер телефона родителя', font=label_font, fg="black", bg="white")
    phone_label.grid(column=0, row=3, sticky='w')
    phone_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    phone_text.grid(column=1, row=3, sticky='w')

    q = Query()
    class_label = Label(window, text='Класс', font=label_font, fg="black", bg="white")
    class_label.grid(column=0, row=4, sticky='w')
    class_text = ttk.Combobox(window, values=q.getClasses(), state='readonly')
    class_text.grid(column=1, row=4, sticky='w')

    mail_label = Label(window, text='Эл.почта', font=label_font, fg="black", bg="white")
    mail_label.grid(column=0, row=5, sticky='w')
    mail_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    mail_text.grid(column=1, row=5, sticky='w')

    login_label = Label(window, text='Логин', font=label_font, fg="black", bg="white")
    login_label.grid(column=0, row=6, sticky='w')
    login_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    login_text.grid(column=1, row=6, sticky='w')

    pass_label = Label(window, text='Пароль', font=label_font, fg="black", bg="white")
    pass_label.grid(column=0, row=7, sticky='w')
    pass_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    pass_text.grid(column=1, row=7, sticky='w')

    confirm_button = Button(window, text='Подтвердить', fg="black", bg="white",
                            command=lambda: confirm_student(window, login_text.get(), pass_text.get(), name_text.get(), date_text.get(),
                                                            class_text.get(), phone_text.get(), mail_text.get(),))
    confirm_button.grid(column=0, row=10, sticky='e')

    exit_button = Button(window, text='Отмена', fg="black", bg="white",
                         command=lambda: exit_click(window, user))
    exit_button.grid(column=0, row=10, sticky='w')
    window.mainloop()


def confirm_teacher(window, login, password, name, dateOfBirth, experience, parentPhoneNumber, mail):
    q=Query()
    conf = mb.askokcancel('Добавление учителя', 'Вы уверены, что хотите добавить учителя?')
    if conf:
        try:
            q.register_teacher(login, password,name,dateOfBirth,experience,parentPhoneNumber,mail)
            label = Label(window, font=('Times New Roman', 10, 'bold'), fg="green", bg="white")
            label.config(text='Пользователь добавлен    ')
            label.grid(column=1, row=100)
        except:
            label = Label(window, font=('Times New Roman', 10, 'bold'), fg="red", bg="white")
            label.config(text='Пользователь не добавлен')
            label.grid(column =1, row = 100)


def reg_teacher(window, user):
    window.destroy()
    window = Tk()
    window.title("Регистрация учителя")
    window.geometry('490x250')
    window['background'] = 'white'

    name_label = Label(window, text='Введите информацию    ', font=label_font, fg="black",
                       bg="white")
    name_label.grid(column=0, row=0)
    name_label = Label(window, text='Имя', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row=1, sticky='w')
    name_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    name_text.grid(column=1, row=1, sticky='w')

    date_label = Label(window, text='Дата рождения', font=label_font, fg="black", bg="white")
    date_label.grid(column=0, row=2, sticky='w')
    date_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    date_text.grid(column=1, row=2, sticky='w')

    phone_label = Label(window, text='Номер телефона', font=label_font, fg="black", bg="white")
    phone_label.grid(column=0, row=3, sticky='w')
    phone_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    phone_text.grid(column=1, row=3, sticky='w')

    class_label = Label(window, text='Опыт работы', font=label_font, fg="black", bg="white")
    class_label.grid(column=0, row=4, sticky='w')
    class_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    class_text.grid(column=1, row=4, sticky='w')

    mail_label = Label(window, text='Эл.почта', font=label_font, fg="black", bg="white")
    mail_label.grid(column=0, row=5, sticky='w')
    mail_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    mail_text.grid(column=1, row=5, sticky='w')

    login_label = Label(window, text='Логин', font=label_font, fg="black", bg="white")
    login_label.grid(column=0, row=6, sticky='w')
    login_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    login_text.grid(column=1, row=6, sticky='w')

    pass_label = Label(window, text='Пароль', font=label_font, fg="black", bg="white")
    pass_label.grid(column=0, row=7, sticky='w')
    pass_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    pass_text.grid(column=1, row=7, sticky='w')

    confirm_button = Button(window, text='Подтвердить', fg="black", bg="white",
                            command=lambda: confirm_teacher(window, login_text.get(), pass_text.get(), name_text.get(),
                                                            date_text.get(),
                                                            class_text.get(), phone_text.get(), mail_text.get(), ))
    confirm_button.grid(column=0, row=10, sticky='e')

    exit_button = Button(window, text='Отмена', fg="black", bg="white",
                         command=lambda: exit_click(window, user))
    exit_button.grid(column=0, row=10, sticky='w')
    window.mainloop()

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

    activity_label = Label(window, text='Активность', font=label_font, fg="black", bg="white")
    activity_label.grid(column=0, row=5, sticky='w')
    activity_text = ttk.Combobox(window, values=[0,1], state='readonly')
    activity_text.set(user.activity)
    activity_text.grid(column=0, row=5, sticky='e')

    confirm_button = Button(window, text='Подтвердить изменения', fg="black", bg="white",
                            command=lambda: confirm_change(window, user, name_text, date_text, phone_text, mail_text, activity_text))
    confirm_button.grid(column=0, row=10, sticky='e')

    password_button = Button(window, text='Изменить пароль', fg="black", bg="white",
                             command=lambda: password_change(window, user))
    password_button.grid(column=0, row=10, sticky='w')

    exit_button = Button(window, text='Отмена', fg="black", bg="white",
                         command=lambda: exit_click(window, user))
    exit_button.grid(column=0, row=11, sticky='w')
    window.mainloop()

def director_app(login):
    window = tkinter.Tk()
    window.title("Добро пожаловать в школу!")
    window.geometry('600x250')
    window['background'] = 'white'
    q = Query()
    idUser = q.getUserIdByLogin(login)
    user = q.getUserInfo(idUser)

    reg_stud_Label = Label(window, text='Директор', fg="black", bg="white")
    reg_stud_Label.grid(sticky="W", column=0, row=0)
    reg_stud_button = Button(window, text='Регистрация ученика', fg="black", bg="white",
                             command=lambda: reg_stud(window, user))
    reg_stud_button.grid(sticky="W", column=0, row=1)

    class_box = ttk.Combobox(window, values=q.getClasses(), state='readonly')
    class_box.set('Выберите класс')
    class_box.grid(column=1, row=1, sticky='w')


    def class_chosen(event):
        window.geometry('900x250')
        id_and_name_students = q.getStudentsNamesByClass(class_box.get())
        student_names = []
        for i in range(len(id_and_name_students)):
            student_names.append(id_and_name_students[i][1])
        students_box = ttk.Combobox(window, values=student_names, state='readonly', width=35)
        students_box.set('Выберите ученика')
        students_box.grid(column=2, row=1, sticky='w')
        def student_chosen(event):
            idUser = 0
            for i in range(len(id_and_name_students)):
                if id_and_name_students[i][1] == students_box.get():
                    idUser = id_and_name_students[i][0]
            student = q.getUserInfo(q.getUserIdByStudentId(idUser))
            change_stud_button = Button(window, text='Посмотреть/Измененить данные ученика', fg="black", bg="white", command= lambda: change_info_student(window, student))
            change_stud_button.grid(sticky="W", column=3, row=1)

        students_box.bind('<<ComboboxSelected>>', student_chosen)


    class_box.bind('<<ComboboxSelected>>', class_chosen)


    reg_teach_button = Button(window, text='Регистрация учителя', fg="black", bg="white",
                              command=lambda: reg_teacher(window, user))
    reg_teach_button.grid(sticky="W", column=0, row=2)

    teacher_box = ttk.Combobox(window, values=q.getTeachersNames(), state='readonly', width=30)
    teacher_box.set('Выберите учителя')
    teacher_box.grid(column=1, row=2, sticky='w')

    def teacher_chosen(event):
        window.geometry("900x250")
        idUser = q.getidUserByName(teacher_box.get())
        teacher = q.getUserInfo(idUser)
        change_teach_button = Button(window, text='Посмотреть/Измененить данные учителя', fg="black", bg="white",
                                     command=lambda: change_info(window, teacher))
        change_teach_button.grid(sticky="W", column=2, row=2)



    teacher_box.bind('<<ComboboxSelected>>', teacher_chosen)



    reg_subj_button = Button(window, text='Добавление предмета', fg="black", bg="white",
                             command=lambda: dir_subjects.add_subject())
    reg_subj_button.grid(sticky="W", column=0, row=3)
    change_subj_button = Button(window, text='Изменение предмета', fg="black", bg="white",
                                command=lambda: dir_subjects.change_subject())
    change_subj_button.grid(sticky="W", column=1, row=3)

    reg_class_button = Button(window, text='Добавление класса', fg="black", bg="white",
                              command=lambda: dir_class.add_class())
    reg_class_button.grid(sticky="W", column=0, row=4)
    change_class_button = Button(window, text='Изменение класса', fg="black", bg="white",
                                 command=lambda: dir_class.change_class())
    change_class_button.grid(sticky="W", column=1, row=4)

    timetable_button = Button(window, text='Просмотр расписания', fg="black", bg="white",
                              command=lambda: timetable.show_table_for_dir(window, user))
    timetable_button.grid(sticky="W", column=0, row=5)
    change_timetable_button = Button(window, text='Изменение расписания', fg="black", bg="white",
                                     command=None)
    change_timetable_button.grid(sticky="W", column=1, row=5)

    anchor_button = Button(window, text='Закрепить учителя \nза предметом', fg="black", bg="white",
                           command=None)
    anchor_button.grid(sticky="W", column=0, row=6)
    show_anchor_button = Button(window, text='Посмотреть закрепленных учителей\n за предметом', fg="black", bg="white",
                                command=None)
    show_anchor_button.grid(sticky="W", column=1, row=6)

    progress_button = Button(window, text='Посмотреть успеваемость', fg="black", bg="white",
                             command=lambda: progress.showProgress(window, user))
    progress_button.grid(sticky="W", column=0, row=7)

    log_out_button = Button(window, text='Выйти', fg="black", bg="white", command=lambda: log_out(window))
    log_out_button.grid(sticky="W", column=0, row=10)

    window.mainloop()
