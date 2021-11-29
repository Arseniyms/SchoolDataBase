from cryptography.fernet import Fernet

from director_app import director_app
from login import logInForm
from mainApp import mainApp
from student_app import studentApp
from queries import *
#
key = b'$2b$12$COnvlB9Kses3CthyxNl9pu'
#
print(bcrypt.hashpw(str.encode("pass"), key))


# logInForm()
# mainApp('T1')
# studentApp('ST1')

q = Query()
# q.register_student('123', '123', 'test', '12.01.2021', '5 А', '12345', 'asd')

# print(q.getLogin('log'))
director_app('DIR')

