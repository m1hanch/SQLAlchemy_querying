import logging

from faker import Faker
from random import randint
from db import session
from models import Students, Subjects, Teachers, Groups, Grades

from models import Grades, Groups, Subjects, Students, Teachers
from psycopg2 import DatabaseError
import psycopg2



NUMBER_OF_GROUPS = 3
NUMBER_OF_STUDENTS = 40
NUMBER_OF_SUBJECTS = 8
NUMBER_OF_TEACHERS = 4
NUMBER_OF_GRADES = 20




def insert_data():
    data = Faker()
    for i in range(NUMBER_OF_TEACHERS):
        teacher = Teachers(full_name=data.name())
        session.add(teacher)
    session.commit()

    for i in range(NUMBER_OF_GROUPS):
        group = Groups(name=chr(65 + i))
        session.add(group)
    session.commit()

    for i in range(NUMBER_OF_STUDENTS):
        student = Students(fullname=data.name(), date_of_birth=data.date_of_birth())




if __name__ == '__main__':
    #insert_data(teachers, groups, students, subject, grades)