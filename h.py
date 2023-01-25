class Person:
    def __init__(self, fullname, age, is_married):
        self.fln = fullname
        self.age = age
        self.ism = is_married

    def introduce_myself(self):
        print(f'Full name - {self.fln}\nAge - {self.age}\nMarriage - {self.ism}')


alan = Person('Alan Toktomambetov', 16, 'no')
# print(f'{alan.fullname},{alan.age},{alan.is_married}')
alan.introduce_myself()


class Student(Person):

    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.mks = marks

    def avarage(self):
        c = 0
        s = 0
        for item in self.mks.values():
            c += 1
            s += item
        print(round(s / c, 1))


class Teacher(Person):
    salary = 2000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.exp = experience

    def cash(self):
        if self.exp > 3:
            salary_new = self.salary + (self.salary / 100 * 5)
            print(salary_new)
        else:
            print(self.salary)


tatiana = Teacher('Tatiana Vsevolodovna', 42, 'yes', 20)
tatiana.introduce_myself()
tatiana.cash()
student = []


def create_students():
    student1 = Student('Bogdan Shepsheliy', 17, 'no', marks={
        'algebra': 5,
        'english': 4,
        'python': 5
    })
    student.append(student1)
    student2 = Student('Alex Ernandes', 18, 'no', marks={
        'python': 4,
        'algebra': 4,
        'english': 4
    })
    student.append(student2)
    student3 = Student('Dima Son', 17, 'no', marks={
        'english': 4,
        'python': 4,
        'algebra': 5
    })
    student.append(student3)
    student4 = Student('Baizak Jyrgalbekov', 17, 'no', marks={
        'algebra': 5,
        'python': 3,
        'english': 4
    })


create_students()
for i in student:
    i.introduce_myself()
    i.avarage()
