from structures.HashMap import HashMap
from Patients import Patients
from Doctors import Doctor
from Diaseases import Diaseases

class Hospital:
    def __init__(self, txt_patients, txt_doctors):
        self.patients = HashMap()
        self.doctors = HashMap()
        self.txt_patients = txt_patients
        self.txt_doctors = txt_doctors

        self.__load_patients()
        self.__load_doctors()

    def __load_patients(self):
        try:
            with open(self.txt_patients, "r") as file:
                for line in file:
                    values = line.strip().split(";")

                    if len(values) < 9:
                        continue

                    patient = Patients(
                        name=values[0],
                        last_name=values[1],
                        id=values[2],
                        age=int(values[3]),
                        status=values[4],
                        photo=values[5],
                        appointments=[],
                        password=values[6],
                        allergies=values[7].split(","),
                        Doctor=values[8]
                    )

                    self.patients.put(patient.id, patient)

        except FileNotFoundError:
            print("Archivo de pacientes no encontrado, iniciando vacío.")

    def __load_doctors(self):
        try:
            with open(self.txt_doctors, "r") as file:
                for line in file:
                    values = line.strip().split(";")

                    if len(values) < 4:
                        continue

                    doc = Doctor(
                        name=values[0],
                        last_name=values[1],
                        id=values[2],
                        speciality=values[3]
                    )
                    self.doctors.put(doc.id, doc)

        except FileNotFoundError:
            print("Archivo de doctores no encontrado.")

    def add_patient(self, patient: Patients):
        if patient.id in self.patients:
            raise ValueError("Ya existe un paciente con ese ID.")
        self.patients.put(patient.id, patient)

    def remove_patient(self, patient_id):
        self.patients.remove(patient_id)

    def get_patient(self, patient_id):
        return self.patients.get(patient_id)

    def update_patient_status(self, patient_id, new_status):
        patient = self.patients.get(patient_id)
        patient.status = new_status
        self.patients.put(patient_id, patient)

    def add_patient_disease(self, patient_id, disease: Diaseases):
        patient = self.patients.get(patient_id)

        if not hasattr(patient, "diseases"):
            patient.diseases = []

        patient.diseases.append(disease)

    def add_appointment(self, patient_id, appointment):
        patient = self.patients.get(patient_id)
        patient.appointments.append(appointment)

    def add_allergy(self, patient_id, allergy):
        patient = self.patients.get(patient_id)
        patient.allergies.append(allergy)

    def list_patients(self):
        return self.patients.items()

    def list_doctors(self):
        return self.doctors.items()

    def save_patients(self):
        with open(self.txt_patients, "w") as file:
            for _, p in self.patients:
                allergies = ",".join(p.allergies)
                file.write(f"{p.name};{p.last_name};{p.id};{p.age};{p.status};{p.photo};{p.password};{allergies};{p.Doctor}\n")
    
    def can_modify_patient(self, doctor: Doctor, patient_id: str) -> bool:
        if doctor.rank == "Chief of Service":
            return True

        return patient_id in doctor.my_patients

