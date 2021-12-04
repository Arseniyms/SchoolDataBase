from tkinter import *
from tkinter import ttk

import tkinter.messagebox as mb

import director_app
import mainApp
import student_app
from queries import Query

label_font = ('Times New Roman', 10)
day_of_weeks = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
time_subjects = ['08:00:00', '10:00:00', '12:00:00', '14:00:00']

dir_login = ''

def exit_clicked(window, user, dir = None):
    if user==None and dir:
        window.destroy()
        director_app.director_app(dir_login)
    elif dir:
        show_table_for_dir(window, user)
    else:
        q = Query()
        window.destroy()
        if user.status == 'Учитель':
            mainApp.mainApp(q.getUserLoginByID(user.idUser))
        elif user.status == 'Ученик':
            student_app.studentApp(q.getUserLoginByID(user.idUser))
        elif user.status == 'Директор':
            director_app.director_app(q.getUserLoginByID(user.idUser))


def confirm_timetable(window, user, class_box, subject_box, teacher_box, day_box, time_box):
    q = Query()
    idTeach = q.getidTeacherByName(teacher_box.get())
    idSubject = q.getSubjectByName(subject_box.get()).idSubject
    idTeacherSubject = q.getIdTeacherSubject(idTeach, idSubject)
    day = day_of_weeks.index(day_box.get())
    q.addTimetable(idTeacherSubject, class_box.get(), day, time_box.get())
    label = Label(window, text='Успешно', font=('Times New Roman', 10, 'bold'), fg="green", bg="white")
    label.grid(sticky="W", column=2, row=3)


def change_timetable(window, user):
    window.destroy()
    window = Tk()
    window.title("Расписание")
    window.geometry('500x250')
    window['background'] = 'white'
    q = Query()
    class_label = Label(window, text='Выберите класс', font=label_font, fg="black", bg="white", anchor='w' ,justify=LEFT)
    class_label.grid(column=0, row=0);
    class_box = ttk.Combobox(window, values=q.getClasses(), font=label_font, state='readonly')
    class_box.grid(column=1, row=0, sticky='w')
    class_label = Label(window, text='Выберите предмет', font=label_font, fg="black", bg="white", anchor='w', justify=LEFT)
    class_label.grid(column=0, row=1);
    subject_box = ttk.Combobox(window, values=q.getSubjects(), font=label_font, state='readonly')
    subject_box.grid(column=1, row=1, sticky='w')

    def sub_chosen(event):
        teacher_label = Label(window, text='Выберите учителя', font=label_font, fg="black", bg="white", anchor='w',
                            justify=LEFT)
        teacher_label.grid(column=0, row=2);
        teacher_box = ttk.Combobox(window, values=q.getSubjectTeachers(subject_box.get()), font=label_font, state='readonly')
        teacher_box.grid(column=1, row=2, sticky='w')
        day_label = Label(window, text='Выберите день недели', font=label_font, fg="black", bg="white", anchor='w',
                            justify=LEFT)
        day_label.grid(column=0, row=3);
        day_box = ttk.Combobox(window, values=day_of_weeks, font=label_font, state='readonly')
        day_box.grid(column=1, row=3, sticky='w')
        time_label = Label(window, text='Выберите время урока', font=label_font, fg="black", bg="white", anchor='w',
                          justify=LEFT)
        time_label.grid(column=0, row=4);
        time_box = ttk.Combobox(window, values=time_subjects, font=label_font, state='readonly')
        time_box.grid(column=1, row=4, sticky='w')

        confirm_buttton = Button(window, text='Подтвердить', fg="black", bg="white",
                            command=lambda: confirm_timetable(window, user, class_box, subject_box, teacher_box, day_box, time_box))
        confirm_buttton.grid(column=1, row=10, sticky='w')

    exit_label = Button(window, text='Назад', fg="black", bg="white",
                        command=lambda: exit_clicked(window, user))
    exit_label.grid(column=0, row=10, sticky='w')


    subject_box.bind('<<ComboboxSelected>>', sub_chosen)

    window.mainloop()


def show_table_for_dir(window, user):
    window.destroy()
    window = Tk()
    window.title("Расписание")
    window.geometry('500x250')
    window['background'] = 'white'
    q = Query()
    global dir_login
    if dir_login == '':
        dir_login = q.getUserLoginByID(user.idUser)
    name_label = Label(window, text='Выберите класс или учителя', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row = 0);
    class_box = ttk.Combobox(window, values=q.getClasses(), font=label_font, state='readonly')
    class_box.grid(column=0, row=1, sticky='w')
    name_box = ttk.Combobox(window, values=q.getTeachersNames(), font=label_font, state='readonly')
    name_box.grid(column=0, row=2, sticky='w')

    def class_chosen(event):
        try:
            stud = q.getStudentByClass(class_box.get())
            stud = q.getUserInfo(stud.idUser)
            show_table_for_student(window, stud, True)
        except Exception:
            mb.showerror("Ошибка", "В классе должен быть хотя бы один ученик, чтобы посмотреть расписание")

    def name_chosen(event):
        idUser = q.getidUserByName(name_box.get())
        teacher = q.getUserInfo(idUser)
        show_table_for_teacher(window, teacher, True)

    class_box.bind('<<ComboboxSelected>>', class_chosen)
    name_box.bind('<<ComboboxSelected>>', name_chosen)

    exit_label = Button(window, text='Назад', fg="black", bg="white",
                        command=lambda: exit_clicked(window, None, dir_login))
    exit_label.grid(column=0, row=10, sticky='w')

    window.mainloop()


def show_table_for_student(window, student, dir=None):
    window.destroy()
    window = Tk()
    window.title("Расписание")
    window.geometry('500x250')
    window['background'] = 'white'

    day_label = Label(window, text='День недели/Время', font=label_font, fg="black", bg="white")
    day_label.grid(column=0, row=1, sticky='w')
    time_subjects = ['08:00:00', '10:00:00', '12:00:00', '14:00:00']
    day_of_weeks = ['Понедельник', 'Вторник', 'Среда', 'Четверг' , 'Пятница', 'Суббота']


    for i in range(len(time_subjects)):
        time_label = Label(window, text=time_subjects[i], font=label_font, fg="black", bg="white")
        time_label.grid(column=i + 1, row=1, sticky='w')

    q = Query()
    timetable = q.getTimeTableForClass(student.numClass)
    n = len(day_of_weeks)
    m = len(time_subjects)
    timetable_matrix = [[0] * m for i in range(n)]

    for t in range(len(timetable)):
        for i in range(n):
            for j in range(m):
                if timetable_matrix[i][j] == 0:
                    timetable_matrix[i][j] = timetable[t].NameOfSubject + "\n" + str.split(timetable[t].Teacher)[0] if timetable[t].dayOfWeek == i + 1 and timetable[t].time == time_subjects[j] else 0

    for i in range(len(day_of_weeks)):
        time_label = Label(window, text=day_of_weeks[i], font=label_font, fg="black", bg="white")
        time_label.grid(column=0, row=i + 2, sticky='w')
    for i in range(n):
        for j in range(m):
            sub_label = Label(window, text=timetable_matrix[i][j] if timetable_matrix[i][j] != 0 else '---',
                              font=('Times New Roman', 8), fg="black", bg="white")
            sub_label.grid(column=j + 1, row=i + 2, sticky='w')


    exit_label = Button(window, text='Назад', fg="black", bg="white", command=lambda: exit_clicked(window, student, dir))
    exit_label.grid(column=0, row=10, sticky='w')


    window.mainloop()

def show_table_for_teacher(window, teacher, dir=None):
    window.destroy()
    window = Tk()
    window.title("Расписание")
    window.geometry('500x250')
    window['background'] = 'white'

    day_label = Label(window, text='День недели/Время', font=label_font, fg="black", bg="white")
    day_label.grid(column=0, row=1, sticky='w')
    time_subjects = ['08:00:00', '10:00:00', '12:00:00', '14:00:00']
    day_of_weeks = ['Понедельник', 'Вторник', 'Среда', 'Четверг' , 'Пятница', 'Суббота']


    for i in range(len(time_subjects)):
        time_label = Label(window, text=time_subjects[i], font=label_font, fg="black", bg="white")
        time_label.grid(column=i + 1, row=1, sticky='w')

    q = Query()
    timetable = q.getTimeTableForTeacher(teacher.idLocal)
    n = len(day_of_weeks)
    m = len(time_subjects)
    timetable_matrix = [[0] * m for i in range(n)]

    for t in range(len(timetable)):
        for i in range(n):
            for j in range(m):
                if timetable_matrix[i][j] == 0:
                    timetable_matrix[i][j] = timetable[t].Class + " " + timetable[t].NameOfSubject if timetable[t].dayOfWeek == i + 1 and timetable[t].time == time_subjects[j] else 0

    for i in range(len(day_of_weeks)):
        time_label = Label(window, text=day_of_weeks[i], font=label_font, fg="black", bg="white")
        time_label.grid(column=0, row=i+2, sticky='w')
    for i in range(n):
        for j in range(m):
            sub_label = Label(window, text= timetable_matrix[i][j] if timetable_matrix[i][j] != 0 else '---' , font=('Times New Roman', 8), fg="black", bg="white")
            sub_label.grid(column=j + 1, row=i+2, sticky='w')

    exit_label = Button(window, text='Назад', fg="black", bg="white", command=lambda: exit_clicked(window, teacher, dir))
    exit_label.grid(column=0, row=10, sticky='w')


    window.mainloop()