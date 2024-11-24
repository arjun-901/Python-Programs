class car:
    color="bkack"
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def Stop():
        print("car stoped")
class mahindra(car):
    def __init__(self,name):
        self.name=name
car1=mahindra("xuv 700")
car2=mahindra("xuv 300")

print(car1.color)

    
       





