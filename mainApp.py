from tkinter import *
from queries import *


def mainApp(login):
    window = Tk()
    window.title("Добро пожаловать в школу!")
    window.geometry('400x250')
    window['background'] = 'white'

    idUser = getUserIdByLogin(login)
    user = getUserInfo(idUser)

    label = Label(window, text=user.status, fg="black", bg="white")
    label.place(x=350 , y = 0)
    # def teacherChosen(event):
    #     lbl = Label(window, text=comboTeachers.get())
    #     lbl.grid(column=1, row=0)
    #
    #
    # def studentsChosen(event):
    #     lbl = Label(window, text=comboStudents.get())
    #     lbl.grid(column=1, row=1)
    #
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
