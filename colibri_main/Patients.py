from Users import User

class Diaseases:
    def __init__(self,name,description,state):
        self.name=name
        self.description=description
        self.state=state


class Patients(User):
    def __init__(self, name, last_name, id, age, status, photo, appointments, password,allergies,Doctors,gender):
        super().__init__(name, last_name, id, age, status, photo, appointments, password,gender)