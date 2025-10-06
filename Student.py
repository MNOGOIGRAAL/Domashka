from AcademicSubject import AcademicSubject
from Faculty_0 import Faculty, faculty_programm
from Speciality import Speciality, speciality_1
from Group import Group, group_1


class Student:
    id_student = 1

    def __init__(self,
                 first_name,
                 last_name,
                 phone,
                 ticket_number,
                 faculty,
                 speciality,
                 group,
                 budget = True,
                 patronymic = None):
        self.first_name = first_name
        self.last_name =last_name
        self.patronymic = patronymic
        self.phone = phone
        self.ticket_number = ticket_number
        self.budget = budget
        self.faculty = faculty
        self.speciality = speciality
        self.group = group
        self.set_of_lessons = [{}]
        self.__id = Student.autoincrement()

    @classmethod
    def autoincrement(cls):
        cls.id_student += 1
        return cls.id_student

    def add_subject(self, subject, teacher, average_grade):
        self.subjecta[subject] = (teacher, average_grade)

    def get_info(self):
        return {
            "ID": self.id_student,
            "Имя": self.first_name,
            "Фамилия": self.last_name,
            "Отчество": self.patronymic,
            "Телефон": self.phone,
            "Студенческий номер билета": self.ticket_number,
            "Бюждет": self.budget,
            "Факультет": self.faculty,
            "Специальность": self.speciality,
            "Группа": self.group
        }


student_Ivanov = Student(first_name="Иван",
                         last_name="Иванов",
                         phone="8(800)555-55-55",
                         ticket_number="808",
                         budget=True,
                         faculty=faculty_programm.name,
                         speciality=speciality_1.name,
                         group=group_1.name)

print(student_Ivanov.id_student)
print(student_Ivanov.)
print(student_Ivanov.get_info())