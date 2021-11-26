status = ['Директор', 'Учитель', 'Ученик']

class User:
    def __init__(self, idUser, status, idLocal = None, name = None, dateOfBirth = None, mail = None, activity = None):
        self.idUser = idUser
        self.idLocal = idLocal
        self.status = status
        self.name = name
        self.dateOfBrith = dateOfBirth
        self.mail = mail
        self.activity = activity

class Teacher(User):
    def __init__(self, idUser, status, idLocal, name, dateOfBirth, experience, phoneNumber, mail, activity):
        super().__init__(idUser, status, idLocal, name, dateOfBirth, mail, activity)
        self.experience = experience
        self.phoneNumber = phoneNumber

class Student(User):
    def __init__(self, idUser, status, idLocal, name, dateOfBirth, parentPhoneNumber, mail, numClass, activity):
        super().__init__(idUser, status, idLocal,  name, dateOfBirth, mail, activity)
        self.numClass = numClass
        self.parentPhoneNumber = parentPhoneNumber
