class User:
    def __init__(self,ID,name,last_name,birth_day,password,foto,appointments=None):
        self.id=ID
        self.name=name
        self.last_name=last_name
        self.birth_day=birth_day
        self.password=password
        self.appointments = appointments if appointments is not None else []
        
        