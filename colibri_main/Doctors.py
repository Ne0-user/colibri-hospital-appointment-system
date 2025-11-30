from .Sets import Set
from .HashMap import HashMap
from .Users import User


class Doctor(User):
    def __init__(self, name, last_name, id, age, status, photo, appointments, password, rank, speciality,gender,pacientes):
        super().__init__(name, last_name, id, age, status, photo, appointments, password,gender)

        self.rank = rank
        self.speciality = speciality

        self.my_patients = HashMap()

        if pacientes:
            for i in pacientes:
                if i.strip() != "": 
                    self.my_patients.put(i, True)

    def assign_patient(self, patient_id):
        self.my_patients.put(patient_id,True)

    def pacients(self):
        print(self.my_patients)
    
    def get_my_complete_patients(self, hospital):
        set1=Set()
        for patient_id in self.my_patients.keys():
            patient = hospital.patients.get(patient_id)
            set1.add(patient)
        return set1


