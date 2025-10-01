class AcademicSubject:
    def __init__(self, name):
        self.name = name

class Group:
    def __init__(self, name):
        self.name = name

class Faculty:
    def __init__(self, name):
        self.name = name

class Speciality:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name

class Student:
    id_student = 1

    def __init__(self,
                 first_name,
                 last_name,
                 phone,
                 ticket_number,
                 type_of_training,
                 faculty,
                 speciality,
                 group,
                 patronymic=None):
        self.first_name = first_name
        self.last_name =last_name
        self.patronymic = patronymic
        self.phone = phone
        self.ticket_number = ticket_number
        self.type_of_training = type_of_training
        self.faculty = faculty
        self.speciality = speciality
        self.group = group
        self.set_of_lessons = {}
        self.id = self.next_id_student()

    @staticmethod
    def next_id_student(num):
        student_id = num.id_student
        num.id_student += 1
        return student_id

    def get_info(self):
        return


class Teacher:
    def __init__(self, fist_name, last_name,  phone, academic_degree, department,  patronymic = None):
        self.fist_name = fist_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone = phone
        self.academic_degree = academic_degree
        self.departament = department


academic_subject_1 = AcademicSubject("Информатика")
group_1 = Group("111")
faculty_1 = Faculty("Программирование")
speciality_1 = Speciality("Иноформационные технологии")
department_1 = Department("Кафедра прогроммирования")

teacher = Teacher("Игорь",
                  "Николаев",
                  "Сергеевич",
                  "8(800)5555555",
                  "Кандидат наук",
                  department_1)

student_1 = Student("Михаил",
                    "Михайлов",
                    "Миахйлович",
                    "8(800)1111111",
                    "101",
                    True, faculty_1, speciality_1, group_1)