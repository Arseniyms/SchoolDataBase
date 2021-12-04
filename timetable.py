from tkinter import *
from tkinter import ttk

import director_app
import mainApp
import student_app
from queries import Query

label_font = ('Times New Roman', 10)

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


def show_table_for_dir(window, user):
    window.destroy()
    window = Tk()
    window.title("Расписание")
    window.geometry('500x250')
    window['background'] = 'white'
    q = Query()
    if user != None:
        global dir_login
        dir_login = q.getUserLoginByID(user.idUser)
    name_label = Label(window, text='Выберите класс или учителя', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row = 0);
    class_box = ttk.Combobox(window, values=q.getClasses(), font=label_font, state='readonly')
    class_box.grid(column=0, row=1, sticky='w')
    name_box = ttk.Combobox(window, values=q.getTeachersNames(), font=label_font, state='readonly')
    name_box.grid(column=0, row=2, sticky='w')

    def class_chosen(event):
        stud = q.getStudentByClass(class_box.get())
        stud = q.getUserInfo(stud.idUser)
        show_table_for_student(window, stud, True)

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