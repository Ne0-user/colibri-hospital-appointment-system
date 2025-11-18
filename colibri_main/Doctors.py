from Users import User
class Doctors(User):
    def __init__(self, ID, name, last_name, birth_day, password,appointments,patients,speciality,rank,foto):
        super().__init__(ID, name, last_name, birth_day, password,foto,appointments)
        