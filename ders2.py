# miras almak
class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def show_info(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(name,surname, age)  # super kelimesi miras aldığım sınıfı abana anlatır
        self.number = number

class Teacher(Person):
    def __init__(self, name, surname, age, lesson):
        super().__init__(name, surname, age)  # super kelimesi miras aldığım sınıfı abana anlatır
        self.lesson = lesson

p = Person("Ali", "Yıldız", 15)
p.show_info()

s = Student("İhsan", "Yılmaz", 14, 1001)
s.show_info()

t = Teacher("Mustafa", "Kaya", 15, 1002)
t.show_info()