from .Users import User
from .Sets import Set
from .Linkedlist import LinkedList
from .Note import Note
import os

class Patients(User):
    def __init__(self, name, last_name, id, age, status, photo, appointments, password, allergies, Doctors, gender):
        super().__init__(name, last_name, id, age, status, photo, appointments, password, gender)
        self.allergies = allergies
        self.Doctors = Doctors
        self.gender = gender

        self.notes = LinkedList()

    def get_all_notes(self):
        result = []
        current = self.notes._LinkedList__head

        while current:
            note = current.get_data()
            result.append({
                "reason": note.reason,
                "lab_results": note.lab_results,
                "treatments": note.treatments,
                "follow_up": note.follow_up
            })
            current = current.get_next()

        return result

    
    def add_note(self,reason,lab_results,treatments,follow_up):
        n=Note(reason,lab_results,treatments,follow_up)
        self.notes.add(n)

    def save_patient_history(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(base_dir,"data", "load_patients_data")

        folder = os.path.abspath(folder)
        os.makedirs(folder, exist_ok=True)

        path = os.path.join(folder, f"{self.id}.txt")

        with open(path, "w", encoding="utf-8") as file:
            current = self.notes._LinkedList__head
            while current:
                file.write(str(current.get_data()))
                current = current.get_next()

    def return_data(self):
        aux=self.notes

    def load_patient_history(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(base_dir, "data", "load_patients_data")
        folder = os.path.abspath(folder)

        path = os.path.join(folder, f"{self.id}.txt")

        if not os.path.exists(path):
            return

        with open(path, "r", encoding="utf-8") as file:
            bloques = file.read().split("----\n")

            for bloque in bloques:
                if bloque.strip() == "":
                    continue

                lineas = bloque.strip().split("\n")

                reason = lineas[0].replace("Reason: ", "")
                lab = lineas[1].replace("Lab results: ", "")
                treatments = lineas[2].replace("Treatments: ", "")
                follow = lineas[3].replace("Follow up: ", "")

                nota = Note(reason, lab, treatments, follow)
                self.notes.add(nota)