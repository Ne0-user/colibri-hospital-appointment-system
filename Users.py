class User:
    def __init__(self,name,last_name,id,age,status,photo,appointments,password,gender):
        self.name=name
        self.last_name=last_name
        self.id=id
        self.age=age
        self.status=status
        self.appointments=appointments
        self.__password=password
        self.photo=photo
        self.gender=gender
    
    @property
    def password(self):
        return self.__password
