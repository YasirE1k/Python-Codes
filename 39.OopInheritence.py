
class worker():
    def __init__(self,name,wage,department):
        self.name=name
        self.wage=wage
        self.department=department
    def showtheknowledges(self):
        print("""name={}\nwage={}\ndepartment={}""".format(self.name,self.wage,self.department))
    def changethedepartment(self,new_department):
        self.department=new_department

class manager(worker):
    pass

manager1=manager("John Wood",3000,"IT")

manager1.showtheknowledges()

manager1.changethedepartment("marketing")

manager1.showtheknowledges()

class manager(worker):
    def raise_wage(self,increase):
        self.wage+=increase

manager2=manager("John Wood",3000,"IT")

manager2.showtheknowledges()

manager2.raise_wage(500)

manager2.showtheknowledges()

class manager(worker):
    def __init__(self,name,wage,department,personal_number):
        self.name=name
        self.wage=wage
        self.department=department
        self.personal_number=personal_number

    def raise_wage(self,increase):
        self.wage+=increase

a=manager("John Wood",3000,"IT",12)


class manager(worker):
    def __init__(self,name,wage,department,personal_number):
        self.name=name
        self.wage=wage
        self.department=department
        self.personal_number=personal_number

    def raise_wage(self,increase):
        self.wage+=increase
    
    def showtheknowledges(self):
        print("""name={}\nwage={}\ndepartment={}\npersonal_number={}""".format(self.name,self.wage,self.department,self.personal_number))

b=manager("John Wood",3000,"IT",12)

b.showtheknowledges()

class worker():
    def __init__(self,name,wage,department):
        self.name=name
        self.wage=wage
        self.department=department
    def showtheknowledges(self):
        print("""name={}\nwage={}\ndepartment={}""".format(self.name,self.wage,self.department))
    def changethedepartment(self,new_department):
        self.department=new_department

class manager(worker):
    def __init__(self,name,wage,department,personal_number):
        super().__init__(name,wage,department)
        self.personal_number=personal_number

    def raise_wage(self,increase):
        self.wage+=increase
    
    def showtheknowledges(self):
        print("""name={}\nwage={}\ndepartment={}\npersonal_number={}""".format(self.name,self.wage,self.department,self.personal_number))
    
c=manager("John Wood",3000,"IT",12)

c.showtheknowledges()



#super can use the other methods too probably.

