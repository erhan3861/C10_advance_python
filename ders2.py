# miras almak
import json

class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def show_info(self):
        print(self.name, self.surname, self.age)

    def save(self):
        print(self.name,"isimli kişi kayıt edildi.")
        
    def to_json(self):
        return {
            "name" : self.name,
            "surname" : self.surname,
            "age" : self.age
        }

class Student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(name,surname, age)  # super kelimesi miras aldığım sınıfı abana anlatır
        self.number = number


class Teacher(Person):
    def __init__(self, name, surname, age, lesson):
        super().__init__(name, surname, age)  # super kelimesi miras aldığım sınıfı abana anlatır
        self.lesson = lesson

    def change_lesson(self, lesson):
        self.lesson = lesson
        

p = Person("Ali", "Yıldız", 15)
p.show_info()

s = Student("İhsan", "Yılmaz", 14, 1001)
s.show_info()

t = Teacher("Mustafa", "Kaya", 15, "Coding")
t.show_info()
t.save()
t.change_lesson("Graphic")
print(t.lesson)

ogrenciler = [s, p, t]

s.name = "Çağlar"
print(s.name)

# Kişi bilgilerini JSON formatına dönüştürüp kaydediyoruz
with open("person.json", "w") as f:
    json.dump(p.to_json(), f, indent=4)

