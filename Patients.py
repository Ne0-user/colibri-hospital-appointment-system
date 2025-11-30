from .Users import User
from .Sets import Set
from .Diaseases import Diasesases


class Patients(User):
    def __init__(self, name, last_name, id, age, status, photo, appointments, password,allergies,Doctors,gender):
        super().__init__(name, last_name, id, age, status, photo, appointments, password,gender)
        self.allergies=allergies
        self.Doctors=Doctors
        self.gender=gender