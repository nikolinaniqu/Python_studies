class Student:
    def __init__(self, name, address, phone, course, index_number):
        self.name = name
        self.address = address
        self.phone = phone
        self.course = course
        self.index_number = index_number

    def getInfo(self):
        print("Name:",self.name,"address:",self.address,"Phone:",self.phone,"Course:",self.course,"Index Number:",self.index_number)

p1=Student("John Benson","High Park 36","(507) 833-3567","Geography","123/007")
p2=Student("Nikolina Nisic-Quinones","Industrieweg 1","015734402128","GIS","07/10")
p3=Student("Mila Quinones","Industrieweg 1","015735555111","Arts","01/33")
p1.getInfo()
p2.getInfo()
p3.getInfo()
