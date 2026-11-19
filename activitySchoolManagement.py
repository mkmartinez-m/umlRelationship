class Person: 
    def __init__(person, name, age):
        person.name = name
        person.age = age

person1 = Person("Lina", 30)
print(f"Name: {person1.name}, Age: {person1.age}")