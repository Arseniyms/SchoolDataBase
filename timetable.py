from tkinter import *
import mainApp
import studentApp
from queries import Query

label_font = ('Times New Roman', 10)


def exit_clicked(window, user):
    q = Query()
    window.destroy()
    if user.status == 'Учитель':
        mainApp.mainApp(q.getUserLoginByID(user.idUser))
    elif user.status == 'Ученик':
        studentApp.studentApp(q.getUserLoginByID(user.idUser))

def show_table_for_student(window, student):
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


    exit_label = Button(window, text='Назад', fg="black", bg="white", command=lambda: exit_clicked(window, student))
    exit_label.grid(column=0, row=10, sticky='w')


    window.mainloop()

def show_table_for_teacher(window, teacher):
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

    exit_label = Button(window, text='Назад', fg="black", bg="white", command=lambda: exit_clicked(window, teacher))
    exit_label.grid(column=0, row=10, sticky='w')


    window.mainloop()