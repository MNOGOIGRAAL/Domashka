from Departament import Department

class Teacher:
    def __init__(self, fist_name, last_name,  phone, academic_degree, department,  patronymic = None):
        self.fist_name = fist_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone = phone
        self.academic_degree = academic_degree
        self.departament = department

teacher = Teacher(fist_name="Игорь", last_name="Николаев", phone="8(900)777-77-77", )