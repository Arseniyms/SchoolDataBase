import pyodbc
from cryptography.fernet import Fernet

from tools import *

key = b'OlboXezUYLMgXl7NcM6SO2fkW3r0hJ00aMYhSubM3rQ='


def getTeachersNames():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute('Select Name from Teachers')

    teachersName = cursor.fetchall()
    connection_to_db.close()

    return teachersName


def getStudentsNames():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute('Select Name from Students')
    studentsName = cursor.fetchall()
    connection_to_db.close()

    return studentsName

def getUserIdByLogin(login):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT idUser from Users where login ='{login}'")
    return cursor.fetchone().idUser

def getUserInfo(idUser):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT idTeacher from Teachers where idUser ='{idUser}'")
    ifTeacher = cursor.fetchone()
    if ifTeacher:
        cursor.execute(
            f"Select idTeacher, Name, DateOfBirth, Experience, PhoneNumber, mail, Activity from Teachers where idTeacher = '{ifTeacher.idTeacher}'")
        teacherInfo = cursor.fetchone()
        connection_to_db.close()
        return Teacher(idUser, status[1], teacherInfo.idTeacher, teacherInfo.Name, teacherInfo.DateOfBirth,
                       teacherInfo.Experience, teacherInfo.PhoneNumber, teacherInfo.mail, teacherInfo.Activity)
    else:
        # cursor.execute(f"SELECT idStudent from Students where idUser ='{idUser}'")
        cursor.execute(
            f"Select  idStudent, Name, DateOfBirth, ParentPhoneNumber, mail, NumClass, Activity from Students JOIN Users on Users.idUser = Students.idUser where Users.idUser = '{idUser}'")
        studentInfo = cursor.fetchone()
        connection_to_db.close()
        if studentInfo:
            return Student(idUser, status[2], studentInfo.idStudent, studentInfo.Name, studentInfo.DateOfBirth,
                           studentInfo.ParentPhoneNumber, studentInfo.mail, studentInfo.NumClass, studentInfo.Activity)
        else:
            return User(idUser, status[0])


def getLogin(login):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT login from Users where login ='{login}'")
    ifLogin = cursor.fetchone()
    connection_to_db.close()
    return ifLogin


def getPassword(login, password):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    f = Fernet(key)
    cursor.execute(f"SELECT password from Users where login ='{login}'")
    ifPass = cursor.fetchone().password
    ifPass = f.decrypt(str.encode(ifPass)).decode()
    if ifPass == password:
        return ifPass
    return None
