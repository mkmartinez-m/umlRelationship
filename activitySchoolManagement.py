class Person: 
    def __init__(person, name, age):
        person.name = name
        person.age = age

person1 = Person("Lina", 30)
print(f"Name: {person1.name}, Age: {person1.age}")

#(Excercise 2)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age  # Safely accesses the private __age attribute

# Reflection: Accessing __age through get_age() protects the data from accidental
# or unauthorized changes (encapsulation) while still allowing safe, controlled read access.

#(Excercise 3)
class Student(Person):
    def study(self):
        return f"{self.name} is studying"

student1 = Student("Lina", 20)
print(f"Name: {student1.name}")
print(f"Age: {student1.get_age()}")
print(student1.study())


#(Exercise 4)
class Teacher(Person):
    def teach(self):
        return f"{self.name} is teaching"

teacher1 = Teacher("Mona", 30)
print(f"Name: {teacher1.name}")
print(f"Age: {teacher1.get_age()}")
print(teacher1.teach())




