from .HashMap import HashMap
from .Sets import Set
from .Patients import Patients
from .Doctors import Doctor
from .Diaseases import Diasesases
import os
import random

class Hospital:
    def __init__(self, txt_patients, txt_doctors):

        self.patients = HashMap()
        self.doctors = HashMap()

        self.txt_patients = txt_patients
        self.txt_doctors = txt_doctors

        self.data_path = os.path.join(os.path.dirname(__file__), "data")

        self.male_names = self.__load_names("M.txt")
        self.female_names = self.__load_names("F.txt")
        self.last_names = self.__load_names("LN.txt")

        self.__ensure_files_exist()
        self.__load_doctors()

        if len(self.doctors) == 0:
            self.__generate_initial_doctors()
        
    def login_doctors(self,id,password):
        if id not in self.doctors:
            return None
        
        doctor=self.doctors.get(id)

        if password ==doctor.password:
            print("work")
            return doctor
        
        return None
    
    def create_doctor(self,name,last,age,password,gender,photo,spece):
        pass


    def create_and_assign_patient(self, name, last, age, password, gender, photo, allergies, doctor_id):
        new_id = f"P{len(self.patients) + 1}"
        allergies_set = Set()
        for a in allergies:
            allergies_set.add(a)

        
        patient = Patients(
            name=name,
            last_name=last,
            id=new_id,
            age=age,
            status="Active",
            photo=photo,
            appointments="",
            password=password,
            allergies=allergies_set,
            Doctors=doctor_id,
            gender=gender
        )

       
        self.patients.put(new_id, patient)

      
        if doctor_id not in self.doctors:
            raise ValueError(f"❌ Doctor {doctor_id} no existe")

        doctor = self.doctors.get(doctor_id)

        
        doctor.assign_patient(new_id)

        self.save_doctors()
        self.save_patients()

        return new_id

    def filter_doctor_patients(self, doctor_id, gender=None, allergy=None):
        if doctor_id not in self.doctors:
            raise ValueError(f"Doctor {doctor_id} no encontrado")

        doctor = self.doctors.get(doctor_id)

        resultados = []
        for pid, _ in doctor.my_patients.items():  
            if pid not in self.patients:
                continue 

            patient = self.patients.get(pid)

            if gender and patient.gender != gender:
                continue

            if allergy and not patient.allergies.contains(allergy):
                continue

            resultados.append(patient)

        return resultados
    
    

    def __ensure_files_exist(self):
        doctor_path = os.path.join(os.path.dirname(__file__), self.txt_doctors)
        patient_path = os.path.join(os.path.dirname(__file__), self.txt_patients)

        if not os.path.exists(doctor_path):
            open(doctor_path, "w").close()

        if not os.path.exists(patient_path):
            open(patient_path, "w").close()


    def __load_names(self, file_name):
        path = os.path.join(self.data_path, file_name)

        if not os.path.exists(path):
            print(f"Advertencia: Archivo {file_name} no encontrado en {path}")
            return []

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        names = text.replace("\n", " ").split(" ")
        return [n.strip() for n in names if n.strip() != ""]


    def __generate_initial_doctors(self):
        for i in range(10):
            if not self.male_names and not self.female_names:
                raise ValueError("⚠ No hay nombres cargados en /data/M.txt o /data/F.txt")

            if random.random() < 0.5 and self.male_names:
                firstname = random.choice(self.male_names)
                gender="M"
            else:
                firstname = random.choice(self.female_names)
                gender="F"

            lastname = random.choice(self.last_names)

            speciality = random.choice(["Pediatría", "Cardiología", "Trauma", "Cirugía"])

            doc = Doctor(
                name=firstname,
                last_name=lastname,
                id=f"D{i+1}",
                age=random.randint(30, 65),
                status="Active",
                photo="none",
                appointments=[],
                password="1234",
                rank=random.choice(["Resident", "Attending", "Chief of Service"]),
                speciality=speciality,
                gender=gender,
                pacientes=[]
            )

            self.doctors.put(doc.id, doc)

        self.save_doctors()

    def save_doctors(self):
        path = os.path.join(os.path.dirname(__file__), self.txt_doctors)

        with open(path, "w", encoding="utf-8") as file:
            for _, doc in self.doctors.items():

                patients_str = ",".join(doc.my_patients.keys())


                file.write(
                    f"{doc.name};{doc.last_name};{doc.id};{doc.age};{doc.status};"
                    f"{doc.photo};{doc.password};{doc.rank};{doc.speciality};"
                    f"{doc.gender};{patients_str}\n"
                )



    def __load_patients(self):
        try:
            path = os.path.join(os.path.dirname(__file__), self.txt_patients)

            with open(path, "r") as file:
                for line in file:
                    values = line.strip().split(";")

                    allergies = Set()
                    if values[8]:
                        for a in values[8].split(","):
                            allergies.add(a)

                    patient = Patients(
                        name=values[0],
                        last_name=values[1],
                        id=values[2],
                        age=values[3],
                        status=values[4],
                        photo=values[5],
                        appointments=values[6],
                        password=values[7],
                        allergies=allergies,
                        Doctors="",
                        gender=values[9]
                    )

                    self.patients.put(patient.id, patient)

        except FileNotFoundError:
            print("Archivo de pacientes no encontrado.")



    def __load_doctors(self):
        try:
            path = os.path.join(os.path.dirname(__file__), self.txt_doctors)

            with open(path, "r") as file:
                for line in file:
                    values = line.strip().split(";")

                    if len(values) < 4:
                        continue

                    doc = Doctor(
                        name=values[0],
                        last_name=values[1],
                        id=values[2],
                        age=values[3],
                        status=values[4],
                        photo=values[5],
                        appointments="",
                        password=values[6],
                        rank=values [7],
                        speciality=values[8],
                        gender=values[9],
                        pacientes=values[10].split(",") if values[10] else []

                    )
                    self.doctors.put(doc.id, doc)

        except FileNotFoundError:
            print("Archivo de doctores no encontrado.")


    def save_patients(self):
        path = os.path.join(os.path.dirname(__file__), self.txt_patients)

        with open(path, "w", encoding="utf-8") as file:
            for _, p in self.patients.items():

                allergies_str = ",".join(p.allergies.to_list()) if hasattr(p.allergies, "to_list") else ""

                file.write(
                    f"{p.name};{p.last_name};{p.id};{p.age};{p.status};"
                    f"{p.photo};{p.password};{allergies_str};{p.Doctors};{p.gender}\n"
            )

