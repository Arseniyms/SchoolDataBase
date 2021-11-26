from tkinter.ttk import Combobox
from tkinter import *

from queries import *

class User:
    def __init__(self, idUser, idLocal, status, name, dateOfBirth, mail, activity):
        self.idUser = idUser
        self.idLocal = idLocal
        self.status = status
        self.name = name
        self.dateOfBrith = dateOfBirth
        self.mail = mail
        self.activity = activity

class Teacher(User):
    def __init__(self, idUser, idLocal, status, name, dateOfBirth, experience, phoneNumber, mail, activity):
        super().__init__(idUser, idLocal, status, name, dateOfBirth, mail, activity)
        self.experience = experience
        self.phoneNumber = phoneNumber

class Student(User):
    def __init__(self, idUser, idLocal, status, name, dateOfBirth, parentPhoneNumber, mail, numClass, activity):
        super().__init__(idUser, idLocal, status, name, dateOfBirth, mail, activity)
        self.numClass = numClass
        self.parentPhoneNumber = parentPhoneNumber


def mainApp():
    window = Tk()
    window.title("Добро пожаловать в школу!")
    window.geometry('400x250')
    window['background'] = 'white'


    def teacherChosen(event):
        lbl = Label(window, text=comboTeachers.get())
        lbl.grid(column=1, row=0)


    def studentsChosen(event):
        lbl = Label(window, text=comboStudents.get())
        lbl.grid(column=1, row=1)


    comboTeachers = Combobox(window)
    comboTeachers['state']= 'readonly'
    comboTeachers.set("Выберите учителя")
    comboTeachers['values'] = (getTeachersNames())
    comboTeachers.grid(column=0, row=0)

    comboStudents = Combobox(window)
    comboStudents['state']= 'readonly'
    comboStudents.set("Выберите ученика")
    comboStudents['values'] = (getStudentsNames())
    comboStudents.grid(column=0, row=1)

    comboTeachers.bind('<<ComboboxSelected>>', teacherChosen)
    comboStudents.bind('<<ComboboxSelected>>', studentsChosen)



    window.mainloop()
