from .HashMap import HashMap
from .Sets import Set
from .Patients import Patients
from .Doctors import Doctor
from .Diaseases import Diasesases
from .NotificationSystem import NotificationsSystem
import os
import random

class Hospital:
    def __init__(self, txt_patients, txt_doctors):

        self.patients = HashMap()
        self.doctors = HashMap()

        self.patients_fg=Set()
        self.patients_mg=Set()
        self.patients_as=Set()
        self.patients_is=Set()

        self.txt_patients = txt_patients
        self.txt_doctors = txt_doctors
        self.txt_notifications="data/notifications.txt"

        self.data_path = os.path.join(os.path.dirname(__file__), "data")

        self.male_names = self.__load_names("M.txt")
        self.female_names = self.__load_names("F.txt")
        self.last_names = self.__load_names("LN.txt")

        self.notifications = NotificationsSystem(
            os.path.join(os.path.dirname(__file__), self.txt_notifications)
        )


        self.__ensure_files_exist()
        self.__load_doctors()
        self.__load_patients()

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
    
    def create_doctor(self,name,last,age,password,gender,photo,spece,rank):
        self.__load_doctors()
        self.__load_patients()
        new_id = f"D{len(self.doctors) + 1}"
        doc=Doctor(
            name=name,
            last_name=last,
            id=new_id,
            age=age,
            status="Active",
            photo=photo,
            appointments="",
            password=password,
            rank=rank,
            speciality=spece,
            gender=gender,
            pacientes=None
        )
        self.doctors.put(new_id,doc)

        self.save_doctors()

        self.notifications.add_notification(
            title="New Doctor",
            description=f"The doctor {name} {last} was succsesfully created."
        )

    def deleate_patient(self,patient):
        patient.change_status()

        if patient.status=="Inactive":
            self.notifications.add_notification(
            title="Pacient Inactived",
            description=f"The patient {patient.name} {patient.last_name} was Desactivated"
            )
        else:
            self.notifications.add_notification(
            title="Pacient Activated",
            description=f"The patient {patient.name} {patient.last_name} was Activated"
            )
        self.save_patients()
        self.__load_patients()
    
    def deleate_doctor(self,doc):
        doc.change_status()

        if doc.status=="Inactive":
            self.notifications.add_notification(
            title="Pacient Inactived",
            description=f"The patient {doc.name} {doc.last_name} was Desactivated"
            )
        else:
            self.notifications.add_notification(
            title="Pacient Activated",
            description=f"The patient {doc.name} {doc.last_name} was Activated"
            )
        
        self.save_doctors()
        self.__load_doctors()


    def create_and_assign_patient(self, name, last, age, password, gender, photo, allergies, doctor_id):
        self.__load_doctors()
        self.__load_patients()
        new_id = f"P{len(self.patients) + 1}"

        
        patient = Patients(
            name=name,
            last_name=last,
            id=new_id,
            age=age,
            status="Active",
            photo=photo,
            appointments="",
            password=password,
            allergies=allergies,
            Doctors=doctor_id,
            gender=gender
        )

       
        self.patients.put(new_id, patient)

        self.notifications.add_notification(
            title="New Patient",
            description=f"The Patient {name} {last} was succsesfully created."
        )
      
        if doctor_id not in self.doctors:
            raise ValueError(f"❌ Doctor {doctor_id} no existe")

        doctor = self.doctors.get(doctor_id)

        if gender == "M":
            self.patients_mg.add(new_id)
        else:
            self.patients_fg.add(new_id)

        self.patients_as.add(new_id)
        
        doctor.assign_patient(new_id)

        self.save_doctors()
        self.save_patients()
    
    def filter_doctors(self,fid=None,gender=None,rank=None,speciality=None):
        if fid:
            return [self.doctors.get(fid)]
        ids = Set()
        for pid in self.doctors.keys():
            ids.add(pid)
        
        if gender:
            if gender=="M":
                ids = ids.intersection(self.doctors_mg)
            else:
                ids = ids.intersection(self.doctors_fg)
        
        if rank:
            if rank=="Resident":
                ids = ids.intersection(self.docr_re)
            elif rank=="Fellow":
                ids = ids.intersection(self.docr_fe)
            elif rank=="Chief_of_service":
                ids = ids.intersection(self.docr_ch)
        
        if speciality:
            if speciality=="Allergy and Immunology":
                ids = ids.intersection(self.spe_al)
            elif speciality=="Cardiology":
                ids = ids.intersection(self.spe_ca)
            elif speciality=="Orthopedic Surgery":
                ids = ids.intersection(self.spe_or)
            elif speciality=="Dermatology":
                ids = ids.intersection(self.spe_de)
            elif speciality=="Pedriatrics":
                ids = ids.intersection(self.spe_pe)

        ids = ids.intersection(self.doctors_as)
            
        result = []
        for pid in ids:
            result.append(self.doctors.get(pid))
        
        self.__load_doctors()
        self.__load_patients()

        return result
    

    def add_note_patient(self,patient,reason,lab,treatment,follow):
        patient.add_note(reason,lab,treatment,follow)

        self.notifications.add_notification(
            title="New Note",
            description=f"The patient {patient.name} {patient.last_name} was succsesfully created."
        )

        patient.save_patient_history()
        patient.load_patient_history()


    
    def filter_patients(self, doctor=None, gender=None, allergies=None, only_doctor=True,fid=None):
            self.__load_doctors()
            self.__load_patients()
            if fid:
                return [self.patients.get(fid)]
            ids = Set()

            if only_doctor and doctor is not None:
                base = doctor.get_my_complete_patients(self)
                
                for p in base:
                    ids.add(p.id)
            else:
                for pid in self.patients.keys():
                    ids.add(pid)

            ids = ids.intersection(self.patients_as)

            if gender:
                if gender == "M":
                    ids = ids.intersection(self.patients_mg)
                else:
                    ids = ids.intersection(self.patients_fg)


            result = []
            for pid in ids:
                result.append(self.patients.get(pid))

            return result


    def __ensure_files_exist(self):
        doctor_path = os.path.join(os.path.dirname(__file__), self.txt_doctors)
        patient_path = os.path.join(os.path.dirname(__file__), self.txt_patients)
        notifications_path = os.path.join(os.path.dirname(__file__), self.txt_notifications)

        if not os.path.exists(doctor_path):
            open(doctor_path, "w").close()

        if not os.path.exists(patient_path):
            open(patient_path, "w").close()
        
        if not os.path.exists(notifications_path):
            open(notifications_path, "w").close()


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

            speciality = random.choice(["Allergy and Immunology", "Cardiology", "Dermatology", "Pediatrics","Orthopedic Surgery"])

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
        self.__load_doctors()



    def __load_patients(self):
        pas = Set()
        pis=Set()

        pm=Set()
        pf=Set()

        try:
            path = os.path.join(os.path.dirname(__file__), self.txt_patients)

            with open(path, "r") as file:
                for line in file:
                    values = line.strip().split(";")
                    
                    allergies = values[7].split(",") if values[7] else []

                    patient = Patients(
                        name=values[0],
                        last_name=values[1],
                        id=values[2],
                        age=values[3],
                        status=values[4],
                        photo=values[5],
                        password=values[6],
                        appointments="",
                        allergies=allergies,
                        Doctors=values[8],
                        gender=values[9]
                    )

                    self.patients.put(patient.id, patient)

                    
                    if patient.status == "Active":
                        pas.add(patient.id)
                    else:
                        pis.add(patient.id)

                    
                    if patient.gender == "M":
                        pm.add(patient.id)
                    else:
                        pf.add(patient.id)

            
            self.patients_as = pas
            self.patients_is = pis

            self.patients_fg=pf
            self.patients_mg=pm

        except Exception as e:
            print("Error cargando pacientes:", e)



    def __load_doctors(self):
        das = Set()
        dis=Set()

        dm=Set()
        df=Set()

        drre=Set()
        drfe=Set()
        drch=Set()

        dsa=Set()
        dsc=Set()
        dsd=Set()
        dsp=Set()
        dso=Set()
        
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

                    if doc.status == "Active":
                        das.add(doc.id)
                    else:
                        dis.add(doc.id)

                    if doc.gender == "M":
                        dm.add(doc.id)
                    else:
                        df.add(doc.id)

                    if doc.rank == "Resident":
                        drre.add(doc.id)
                    elif doc.rank== "Fellow":
                        drfe.add(doc.id)
                    elif doc.rank== "Chief_of_Service":
                        drch.add(doc.id)
                    
                    if doc.speciality=="Allergy and Immunology":
                        dsa.add(doc.id)
                    elif doc.speciality=="Cardiology":
                        dsc.add(doc.id)
                    elif doc.speciality=="Dermatology":
                        dsd.add(doc.id)
                    elif doc.speciality=="Pedriatrics":
                        dsp.add(doc.id)
                    elif doc.speciality=="Orthopedic Surgery":
                        dso.add(doc.id)
            
            self.doctors_as = das
            self.doctors_is = dis

            self.doctors_fg=df
            self.doctors_mg=dm

            self.docr_re=drre
            self.docr_fe=drfe
            self.docr_ch=drch

            self.spe_al=dsa
            self.spe_ca=dsc
            self.spe_pe=dsp
            self.spe_or=dso
            self.spe_de=dsd

        except FileNotFoundError:
            print("Archivo de doctores no encontrado.")


    def save_patients(self):
        path = os.path.join(os.path.dirname(__file__), self.txt_patients)

        with open(path, "w", encoding="utf-8") as file:
            for _, p in self.patients.items():
                allergies_str = ",".join(p.allergies)

                file.write(
                    f"{p.name};{p.last_name};{p.id};{p.age};{p.status};"
                    f"{p.photo};{p.password};{allergies_str};{p.Doctors};{p.gender}\n"
                )
        self.__load_patients()