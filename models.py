from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column, sessionmaker, declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.engine import create_engine


Base = declarative_base()
class Groups(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)

class Teachers(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    full_name: Mapped[str] = mapped_column(nullable=False)

class Students(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(nullable=False)
    date_of_birth = mapped_column(DateTime, nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey(Groups.id, ondelete='CASCADE'))
    group = relationship('Groups')

class Subjects(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    subject_name: Mapped[str] = mapped_column(nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey(Teachers.id, ondelete='CASCADE'))
    teacher = relationship('Teachers')

class Grades(Base):
    __tablename__ = 'grades'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey(Students.id, ondelete='CASCADE'))
    subject_id: Mapped[int] = mapped_column(ForeignKey(Subjects.id, ondelete='CASCADE'))
    grade: Mapped[int] = mapped_column(CheckConstraint('grade>=0 and grade<=100'))
    date_received = mapped_column(DateTime, nullable=False)
    student = relationship('Students')
    subject = relationship('Subjects')


#Base.metadata.create_all(engine)



