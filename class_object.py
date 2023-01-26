class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def return_name(self):
        print(self.name)

    def set_school(self, school):
        self.school = school
    
    def get_school(self):
        return self.school

    def my_identity(self):
        print("My name is", self.name)
        print("My age is", self.age)

demo_person = Person("test", 17)
demo_person.set_school("ENS CACHAN")
#demo_person2 = Person("Thomas", 16)

print(demo_person.get_school())