from Users import User
from structures.Sets import Set

class Doctor(User):
    def __init__(self, name, last_name, id, age, status, photo, appointments, password, rank):
        super().__init__(name, last_name, id, age, status, photo, appointments, password)

        self.rank = rank
        self.my_patients = Set()            

    def assign_patient(self, patient_id):
        self.my_patients.add(patient_id)
