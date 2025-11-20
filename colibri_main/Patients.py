from Users import User

class Diaseases:
    def __init__(self,name,description,state):
        self.name=name
        self.description=description
        self.state=state
    
    def change_condition(self):
        pass


class Patients(User):
    def __init__(self, ID, name, last_name, birth_day, password,allergies,sickness,history,foto):
        super().__init__(ID, name, last_name, birth_day, password,foto)
        self.history=history
        self.sickness=None
    
    def __str__(self):
        return (
            f"Paciente ID: {self.id}\n"
            f"Nombre: {self.name} {self.last_name}\n"
            f"Fecha de nacimiento: {self.birth_day}\n"
            f"Alergias: {self.allergies}\n"
            f"Enfermedades: {self.sickness}\n"
            f"Estado / Historial: {self.history}"
        )
        