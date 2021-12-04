import datetime

import pyodbc
import bcrypt

from tools import *

key = b'$2b$12$COnvlB9Kses3CthyxNl9pu'


class Query:
    def __init__(self):
        self.connection_to_db = pyodbc.connect(
            r'Driver={SQL Server};Server=LAPTOP-GT7SSRCR;Database=Matus;Trusted_Connection=yes;')
        self.cursor = self.connection_to_db.cursor()

    def __del__(self):
        self.connection_to_db.close()

    def getTeachersNames(self):
        self.cursor.execute('Select Name from Teachers')
        teachersName = []
        while True:
            t = self.cursor.fetchone()
            if t == None:
                break
            teachersName.append(t.Name)
        return teachersName

    def getStudentsNames(self):
        self.cursor.execute('Select idStudent, Name from Students ORDER BY Name')
        return self.cursor.fetchall()

    def getStudentsNamesByClass(self, numClass):
        self.cursor.execute(f"Select idStudent, Name from Students Where NumClass = '{numClass}' ORDER BY Name")

        return self.cursor.fetchall()


    def changeInfoOfUser(self, idLocal, newName, dateOfBirth, phoneNumber, mail, activity=1):
        self.cursor.execute(
            f"Update Teachers Set Name = '{newName}', DateOfBirth = '{dateOfBirth}', PhoneNumber ='{phoneNumber}',Mail = '{mail}', Activity = '{activity}' Where idTeacher = '{idLocal}'")
        self.connection_to_db.commit()

    def changeInfoOfStudent(self, idLocal, newName, dateOfBirth, phoneNumber, mail, numClass, activity=1):
        self.cursor.execute(
            f"Update Students Set Name = '{newName}', DateOfBirth = '{dateOfBirth}', parentPhoneNumber ='{phoneNumber}',Mail = '{mail}', numClass = '{numClass}', Activity = '{activity}' Where idStudent = '{idLocal}'")
        self.connection_to_db.commit()


    def getUserLoginByID(self, idUser):
        self.cursor.execute(f"SELECT login from Users where idUser ='{idUser}'")
        return self.cursor.fetchone().login

    def getUserIdByLogin(self, login):
        self.cursor.execute(f"SELECT idUser from Users where login ='{login}'")
        return self.cursor.fetchone().idUser

    def getidUserByName(self, name):
        self.cursor.execute(f"SELECT idUser from Teachers where name ='{name}'")
        return self.cursor.fetchone().idUser

    def getidTeacherByName(self, name):
        self.cursor.execute(f"SELECT idTeacher from Teachers where name ='{name}'")
        return self.cursor.fetchone().idTeacher

    def getUserInfo(self, idUser):
        self.cursor.execute(f"SELECT idTeacher from Teachers where idUser ='{idUser}'")
        ifTeacher = self.cursor.fetchone()
        if ifTeacher:
            self.cursor.execute(
                f"Select idTeacher, Name, DateOfBirth, Experience, PhoneNumber, mail, Activity from Teachers where idTeacher = '{ifTeacher.idTeacher}'")
            teacherInfo = self.cursor.fetchone()
            return Teacher(idUser, status[1], teacherInfo.idTeacher, teacherInfo.Name, teacherInfo.DateOfBirth,
                           teacherInfo.Experience, teacherInfo.PhoneNumber, teacherInfo.mail, teacherInfo.Activity)
        else:
            self.cursor.execute(
                f"Select  idStudent, Name, DateOfBirth, ParentPhoneNumber, mail, NumClass, Activity from Students JOIN Users on Users.idUser = Students.idUser where Users.idUser = '{idUser}'")
            studentInfo = self.cursor.fetchone()
            if studentInfo:
                return Student(idUser, status[2], studentInfo.idStudent, studentInfo.Name, studentInfo.DateOfBirth,
                               studentInfo.ParentPhoneNumber, studentInfo.mail, studentInfo.NumClass,
                               studentInfo.Activity)
            else:
                return User(idUser, status[0])

    def getLogin(self, login):
        self.cursor.execute(f"SELECT login from Users where login ='{login}'")
        return self.cursor.fetchone().login



    def getPassword(self, login, password):
        self.cursor.execute(f"SELECT password from Users where login ='{login}'")
        ifPass = str.encode(self.cursor.fetchone().password)
        password = bcrypt.hashpw(str.encode(password), key)
        if password == ifPass:
            return True
        return None

    def changePassword(self, idUser, password):
        password = bcrypt.hashpw(str.encode(password), key)
        self.cursor.execute(f"UPDATE Users Set password = '{password.decode()}' where idUser ='{idUser}'")
        self.connection_to_db.commit()


    # Вывод предметов, закрепленных за учителем
    def getTeacherSubjects(self, idTeacher):
        self.cursor.execute(f"Select nameOfSubject from Subjects " 
                            f"JOIN TeacherSubjects ON TeacherSubjects.idSubject=Subjects.idSubject "
                            f"JOIN Teachers ON TeacherSubjects.idTeacher=Teachers.idTeacher "
                            f"WHERE Teachers.idTeacher ='{idTeacher}'")
        subjects = []
        while True:
            sub = self.cursor.fetchone()
            if sub == None:
                break
            subjects.append(sub.nameOfSubject)

        return subjects

    def getSubjectTeachers(self, nameSubject):
        self.cursor.execute(f"""Select Distinct Name from Teachers
	                            JOIN TeacherSubjects ON TeacherSubjects.idTeacher=Teachers.idTeacher
	                            JOIN Subjects ON TeacherSubjects.idSubject=Subjects.idSubject
		                        WHERE Subjects.NameOfSubject = '{nameSubject}'""")
        teachers = []
        while True:
            sub = self.cursor.fetchone()
            if sub == None:
                break
            teachers.append(sub.Name)

        return teachers

    def getIdTeacherSubject(self, idTeacher, idSubject):
        self.cursor.execute(f"""Select idTeacherSubject from TeacherSubjects Where idTeacher = '{idTeacher}' and idSubject = '{idSubject}'""")
        return self.cursor.fetchone().idTeacherSubject

    def addTimetable(self, idTeacherSubject, numClass, dayOfWeek, time):
        self.cursor.execute(f"""INSERT INTO Timetable(idTeacherSubject, numClass, dayOfWeek, time) 
                                VALUES ('{idTeacherSubject}', '{numClass}', '{dayOfWeek}', '{time}')""")
        self.connection_to_db.commit()

    def anchorTeacher(self, idTeacher, idSubject):
        self.cursor.execute(f"exec ANCHOR_TEACHER '{idTeacher}', '{idSubject}'")
        self.cursor.commit()

    def getTimeTableForTeacher(self, idTeacher):
        self.cursor.execute(f"EXEC sp_set_session_context 'idTeacher', {idTeacher}")
        self.cursor.execute(f'Select * FROM TEACHER_TIMETABLE ORDER BY dayOfWeek ASC, time ASC')
        return self.cursor.fetchall()


    def getClasses(self):
        self.cursor.execute(f"Select numClass FROM Classes")
        classes = []
        while True:
            cl = self.cursor.fetchone()
            if cl == None:
                break
            if cl.numClass !='':
                classes.append(cl.numClass)
        return classes

    def getProgressForClass(self, numClass):
        self.cursor.execute(f"""Select Subjects.NameOfSubject, Students.Name, Grade from Grades 
	                                JOIN Students ON Students.idStudent = Grades.idStudent
	                                JOIN TeacherSubjects ON TeacherSubjects.idTeacherSubject = Grades.idTeacherSubject
	                                JOIN Subjects ON TeacherSubjects.idSubject = Subjects.idSubject
                                        WHERE Students.NumClass = '{numClass}'
                                            ORDER BY NameOfSubject, Name""")
        grades = []
        while True:
            gr = self.cursor.fetchone()
            if gr == None:
                break
            grades.append(gr)
        return grades


    def getProgressOfStudent(self, idStudent):
        self.cursor.execute(f"""Select Subjects.NameOfSubject, Grade from Grades
                                    JOIN Students ON Students.idStudent = Grades.idStudent
                                    JOIN TeacherSubjects ON TeacherSubjects.idTeacherSubject = Grades.idTeacherSubject
                                    JOIN Subjects ON TeacherSubjects.idSubject = Subjects.idSubject
                                        WHERE Students.idStudent = {idStudent}
                                            ORDER BY NameOfSubject""")
        grades = []
        while True:
            gr = self.cursor.fetchone()
            if gr == None:
                break
            grades.append(gr)
        return grades


    def put_grade(self, nameStudent, numClass, nameSubject, grade, dateOfGrade):
        self.cursor.execute(f"""INSERT INTO Grades(idStudent, idTeacherSubject, Grade, DateOfGrade)
                                VALUES((Select idStudent from Students where Name='{nameStudent}'),
                                        (Select DISTINCT TeacherSubjects.idTeacherSubject from TeacherSubjects 
                                            JOIN Subjects ON Subjects.idSubject = TeacherSubjects.idSubject
                                            JOIN Timetable ON Timetable.idTeacherSubject = TeacherSubjects.idTeacherSubject
                                            WHERE Subjects.NameOfSubject='{nameSubject}' and Timetable.numClass = (Select numClass from Students where name ='{nameStudent}' and numClass ='{numClass}')),
                                            {grade}, '{dateOfGrade}')""")
        self.connection_to_db.commit()

    def getTimeTableForClass(self, numClass):
        self.cursor.execute(f"EXEC sp_set_session_context 'NumClass', '{numClass}'")
        self.cursor.execute(f'Select * FROM CLASS_TIMETABLE order by dayOfWeek ASC, time ASC')
        return self.cursor.fetchall()


    def register_student(self, login, password, name, dateOfBirth, numClass, parentPhoneNumber, mail):
        password = bcrypt.hashpw(str.encode(password), key)
        self.cursor.execute(f"EXEC REGISTER_STUDENTS '{login}', '{password.decode()}','{name}', '{dateOfBirth}',  '{numClass}', '{parentPhoneNumber}', '{mail}'")
        self.connection_to_db.commit()

    def register_teacher(self, login, password, name, dateOfBirth, experience, phoneNumber, mail):
        password = bcrypt.hashpw(str.encode(password), key)
        self.cursor.execute(
            f"EXEC REGISTER_TEACHERS '{login}', '{password.decode()}','{name}', '{dateOfBirth}',  {experience}, '{phoneNumber}', '{mail}'")
        self.connection_to_db.commit()

    def getUserIdByStudentId(self, studentId):
        self.cursor.execute(f"Select idUser from Students where idStudent={studentId}")
        return self.cursor.fetchone().idUser



    def addSubject(self, name, description):
        self.cursor.execute(f"INSERT INTO Subjects (NameOfSubject, Description)VALUES ('{name}', '{description}')")
        self.connection_to_db.commit()

    def getSubjects(self):
        self.cursor.execute(f"Select NameOfSubject from Subjects")
        subjects = []
        while True:
            sub = self.cursor.fetchone()
            if sub == None:
                break
            if sub.NameOfSubject != '':
                subjects.append(sub.NameOfSubject)
        return subjects

    def changeSubject(self, currentName,name, description, activity):
        self.cursor.execute(f"Update Subjects Set NameOfSubject='{name}', Description = '{description}', Activity = '{activity}' where NameOfSubject = '{currentName}'")
        self.connection_to_db.commit()

    def getSubjectByName(self, name):
        self.cursor.execute(f"Select * from Subjects where NameOfSubject = '{name}'")
        return self.cursor.fetchone()

    def getClassByNum(self, num):
        self.cursor.execute(f"Select * from Classes where NumClass = '{num}'")
        return self.cursor.fetchone()

    def addClass(self, name,max):
        self.cursor.execute(f"INSERT INTO Classes (NumClass, MaxQuantity) VALUES ('{name}', '{max}')")
        self.connection_to_db.commit()

    def changeClass(self, num ,newNum, max):
        self.cursor.execute(f"Update Classes Set NumClass='{newNum}', MaxQuantity = '{max}' where NumClass = '{num}'")
        self.connection_to_db.commit()

    def getStudentByClass(self, numClass):
        self.cursor.execute(f"Select * from Students where NumClass='{numClass}'")
        return self.cursor.fetchone()