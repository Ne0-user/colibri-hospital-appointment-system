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
    
    def verify_password(self,password,name):
        if self.name or self.id==name:
            if self.__password==password:
                return True