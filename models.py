from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime, Date

Base = declarative_base()

class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, autoincrement=True, primary_key=True)
    full_name = Column(String, nullable=False)

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    group_id = Column(Integer, ForeignKey(Groups.id, ondelete='CASCADE'))

class Subjects(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teachers.id, ondelete='CASCADE'))

class Grades(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey(Students.id, ondelete='CASCADE'))
    subject_id = Column(Integer, ForeignKey(Subjects.id, ondelete='CASCADE'))
    grade = Column(Integer, CheckConstraint('grade>=0 and grade<=100'))
    date_received = Column(Date, nullable=False)




