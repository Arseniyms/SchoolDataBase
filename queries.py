import pyodbc
from cryptography.fernet import Fernet

key = b'OlboXezUYLMgXl7NcM6SO2fkW3r0hJ00aMYhSubM3rQ='

def getTeachersNames():
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute('Select Name from Teachers')

    teachersName = cursor.fetchall()
    connection_to_db.close()

    return teachersName

def getStudentsNames():
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute('Select Name from Students')
    studentsName = cursor.fetchall()
    connection_to_db.close()

    return studentsName


def getUserInfo(idUser):
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT idTeacher from Teachers where idUser ='{idUser}'")
    ifTeacher = cursor.fetchone()
    if ifTeacher:
        connection_to_db.close()
        return ifTeacher.idTeacher
    else:
        cursor.execute(f"SELECT idStudent from Students where idUser ='{idUser}'")
        ifStudent = cursor.fetchone()
        connection_to_db.close()
        return ifStudent.idStudent

def getLogin(login):
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT login from Users where login ='{login}'")
    ifLogin = cursor.fetchone()
    connection_to_db.close()
    return ifLogin

def getPassword(login,password):
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    f = Fernet(key)
    cursor.execute(f"SELECT password from Users where login ='{login}'")
    ifPass = cursor.fetchone().password
    ifPass = f.decrypt(str.encode(ifPass)).decode()
    if ifPass == password:
        return ifPass
    return None
