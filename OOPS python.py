class employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary=salary
    def getsalary(self):
        return self.salary
    
rohan=employee("rohan",999)
print(rohan.salary)
print(rohan.name)

atharva=employee("atharva",999999)
print(atharva.salary)
print(atharva.name)