class Doctor:
    def __init__(self, name):
        self.name = name
        self.__list_of_pacients = list()

    def add_pacient(self, pacient):
        self.__list_of_pacients.append(pacient)


    def get_paciens(self):
        p = []
        for i in self.__list_of_pacients:
            p.append(i.name)
        return p


    def get_unique_pacient(self):
        return list(set(self.get_paciens()))


class Pacient:
    def __init__(self, name):
        self.name = name


class CommonPacients:
    def __init__(self, *args):
        self.doctors = [doctor for doctor in args]


    def get_doctors(self):
        return [doctor.name for doctor in self.doctors]


    def get_common_pacient(self):
        sets_of_pacient =[set(doctor.get_unique_pacient()) for doctor in self.doctors]
        if not sets_of_pacient:
            return []
        common_pacient = set.intersection(*sets_of_pacient)
        return list(common_pacient)

class Queue:
    def __init__(self):
        self.__patients_queue = []


    def add_to_queue(self, pacient):
        self.__patients_queue.append(pacient)


    def appointment_doctor(self):
        pass


    def list_of_patients_in_queue(self):
        p = []
        for i in self.__patients_queue:
            p.append(i.name)
        return p


    def number_pacients_in_queue(self):
        return len(self.__patients_queue)





doctor_Ivan = Doctor("Иван")
doctor_Vera = Doctor("Вера")

pacient_Arkadii = Pacient("Аркадий")
pacient_Nikolai = Pacient("Николай")
pacient_Oksana = Pacient("Оксана")
pacient_Nina = Pacient("Нина")
pacient_Grigorii = Pacient("Григорий")

doctor_Vera.add_pacient(pacient_Grigorii)
doctor_Vera.add_pacient(pacient_Nina)
doctor_Vera.add_pacient(pacient_Grigorii)
doctor_Vera.add_pacient(pacient_Nikolai)
# print(f"Все посетители доктора Веры: {doctor_Vera.get_paciens()}")
# print(f"Уникальные посетители доктора Веры: {doctor_Vera.get_unique_pacient()}")

doctor_Ivan.add_pacient(pacient_Grigorii)
doctor_Ivan.add_pacient(pacient_Nikolai)
doctor_Ivan.add_pacient(pacient_Arkadii)
doctor_Ivan.add_pacient(pacient_Arkadii)
doctor_Ivan.add_pacient(pacient_Oksana)
doctor_Ivan.add_pacient(pacient_Nina)
print(f"Все посетители доктора Ивана: {doctor_Ivan.get_paciens()}")
print(f"Уникальные посетители доктора Ивана: {doctor_Ivan.get_unique_pacient()}")

CD = CommonPacients(doctor_Vera, doctor_Ivan)
print(f"Список всех докторов: {CD.get_doctors()}")
print(f"Общие пациенты: {CD.get_common_pacient()}")
