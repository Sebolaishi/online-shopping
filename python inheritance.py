'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Person:

    def __init__(self, name, surname):
        self.firstname = name
        self.lastname = surname

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, name, surname, staffnumber):
        Person.__init__(self,name, surname)
        self.empno = staffnumber

    def GetEmployee(self):
        return self.Name() + ", " +  self.empno

x = Person("Lodwin", "Moloto")
y = Employee("Sebolaishi", "Moloto", "930301")

print(y.GetEmployee())
