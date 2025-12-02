from .Users import User
from .Sets import Set
from .Linkedlist import LinkedList
from .Deque import Deque
from .Note import Note
import os

class Patients(User):
    def __init__(self, name, last_name, id, age, status, photo, appointments, password, allergies, Doctors, gender):
        super().__init__(name, last_name, id, age, status, photo, appointments, password, gender)
        self.allergies = allergies
        self.Doctors = Doctors
        self.gender = gender

        self.notes = Deque()
    
    def get_all_notes(self):
        self.load_patient_history()
        result = []

        for note in self.notes:
            result.append({
                "reason": note.reason,
                "lab_results": note.lab_results,
                "treatments": note.treatments,
                "follow_up": note.follow_up
            })

        return result


    def add_note(self, reason, lab_results, treatments, follow_up):
        note = Note(reason, lab_results, treatments, follow_up)
        self.notes.appendleft(note)
        self.save_patient_history()


    def save_patient_history(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(base_dir, "data", "load_patients_data")
        os.makedirs(folder, exist_ok=True)

        path = os.path.join(folder, f"{self.id}.txt")

        with open(path, "w", encoding="utf-8") as file:
            for note in self.notes:
                file.write(str(note))


    def load_patient_history(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(base_dir, "data", "load_patients_data")
        path = os.path.join(folder, f"{self.id}.txt")

        if not os.path.exists(path):
            return

        self.notes.clear()

        with open(path, "r", encoding="utf-8") as file:
            blocks = file.read().split("----\n")

            for block in blocks:
                if not block.strip():
                    continue

                lines = block.strip().split("\n")

                reason = lines[0].replace("Reason: ", "")
                lab = lines[1].replace("Lab results: ", "")
                treatments = lines[2].replace("Treatments: ", "")
                follow = lines[3].replace("Follow up: ", "")

                note = Note(reason, lab, treatments, follow)
                self.notes.append(note)
