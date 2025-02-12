from classes import person, Emobilis_Employee, Developer,Teacher
from classes import Employee
from classes import Vehicle
from classes import Rectangle


person1 = person()
print(person1.first_name)
print(person1.last_name)
print(person1.gender)
print(person1.age)

person2 = person()
print(person2.first_name)
print(person2.last_name)
print(person2.gender)
print(person2.age)

Employee1 = Employee("John", "Male",100000,23,"developer")
Employee2 = Employee("Ann", "Female",20000,19,"nurse")
Employee3 = Employee("Peter", "Male",30000,34,"security")

print(Employee1.basic_salary)
print(Employee2.gender)
print(Employee3.position)

print(Employee1.display_employees())
print(Employee2.display_employees())
print(Employee3.display_employees())

print(Employee1.full_salary())
print(Employee2.full_salary())
print(Employee3.full_salary())

vehicle1 = Vehicle("aura","hybrid","2018")
vehicle2 = Vehicle("noah","electric","2017")
vehicle3 = Vehicle("bmw","M5","2017")
vehicle4 = Vehicle("Mercedes","GLS400","2020")
vehicle5 = Vehicle("Dodge","demon","2020")
print(vehicle4.make)
print(vehicle5.year)
print(vehicle1.model)
print(vehicle2.make)
print(vehicle3.model)



# Create an instance of Rectangle
rect = Rectangle(5, 3)

# Display the length and width
rect.display()

# Calculate the perimeter
print("Perimeter:", rect.perimeter())

# Calculate the area
print("Area:", rect.area())

# Create an instance of Rectangle
rect = Rectangle(8, 20)

# Display the length and width
rect.display()

# Calculate the perimeter
print("Perimeter:", rect.perimeter())

# Calculate the area
print("Area:", rect.area())


# Create an instance of Rectangle
rect = Rectangle(70, 30)

# Display the length and width
rect.display()

# Calculate the perimeter
print("Perimeter:", rect.perimeter())

# Calculate the area
print("Area:", rect.area())


Emobilis_Employee1 = Emobilis_Employee("Evans", "Male",230000,34,"Degree")
Emobilis_Employee2 = Emobilis_Employee("Purity", "Female",125000,21,"Diploma")
Emobilis_Employee3 = Emobilis_Employee ("Ann", "Female",200000,19,"Master")
print(Emobilis_Employee1.qualification)
print(Emobilis_Employee2.salary)
print(Emobilis_Employee1.promotion())
print(Emobilis_Employee2.promotion())
print(Emobilis_Employee3.promotion())
Developer1 = Developer("Ruth", "female",230000,24,"Degree","Fronted Developer","Python")
Developer2 = Developer("Alex","Male",230000,26,"Diploma","Backend Developer","HTMl")
print(Developer1.specialization)
print(Developer2.prog_language)

teacher1 = Teacher("John",34000,"Male",45,"Python","decade","masters")
teacher2 = Teacher("Sandra",56000,"female",33,"html","6 years","degree")
print(teacher1.age)
print(teacher2.gender)
print(teacher1.salary())
print(teacher2.salary())



