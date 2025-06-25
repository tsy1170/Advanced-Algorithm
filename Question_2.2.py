class Person:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def get_person_detail(self):
        return (f"Name  : {self.name}\n"
                f"Age   : {self.age}\n"
                f"Gender: {self.gender}\n"
                f"E-mail: {self.email}")

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

alice = Person("Alice", "20", "Female", "alice20@gmail.com")
ben = Person("Ben", "21", "Male", "ben21@gmail.com")
chloe = Person("Chloe", "22", "Female", "chloe22@gmail.com")
alex = Person("Alex", "20", "Male", "alex20@gmail.com")
emma = Person("Emma", "19", "Female", "emma19@gmail.com")
