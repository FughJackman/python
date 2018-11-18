# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Student:
    def __init__(self, name, mother, father):
        self.name = name
        self.mother = mother
        self.father = father

    def get_parents_names(self):
        return("Мать: {}, Отец: {}".format(self.mother, self.father))

class Class:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def get_students(self):
        return[a.name for a in self.students]

class Teacher:
    def __init__(self, name, subject, classes):
        self.name = name
        self.subject = subject
        self.classes = classes

class School:
    def __init__(self, number, teachers, classes):
        self.number = number
        self.teachers = teachers
        self.classes = classes

    def get_teachers(self):
        return[a.name for a in self.teachers]

    def get_classes(self):
        return[a.name for a in self.classes]

    def find_student_subjects(self, student):
        zz = [x.name for x in self.classes if student in [y.name for y in x.students]]
        return [x.subject for x in self.teachers if zz[0] in [y.name for y in x.classes]]
            

st1 = Student("П. А. Иванов", "Мария Александровна Иванова", "Даниил Сергеевич Иванов")
st2 = Student("С. А. Иванов", "Ирина Александровна Иванова", "Виталий Сергеевич Иванов")
st3 = Student("С. А. Петров", "Ирина Олеговна Петрова", "Виталий Игоревич Петров")
st4 = Student("И. А. Иванов", "Екатерина Владимировна Иванова", "Леонид Витальевич Иванов")
st5 = Student("И. О. Николаев", "Татьяна Владимировна Петрова", "Михаил Павлович Николаев")
st6 = Student("И. Ф. Крутой", "Софья Владимировна Крутая", "Эдуард Михаилович Крутой")
cl2b = Class("2Б", [st1, st2])
cl5a = Class("5А", [st3, st4])
cl7g = Class("7Г", [st5, st6])
teacher1 = Teacher("Илья Дмитриевич Савин", "География", [cl2b, cl5a])
teacher2 = Teacher("Алексей Сергеевич Долматов", "Литература", [cl7g])
sch46 = School("46", [teacher1, teacher2], [cl2b, cl5a, cl7g])

print(sch46.get_classes())
print(cl5a.get_students())
print(st4.get_parents_names())
print(sch46.get_teachers())
print(sch46.find_student_subjects('П. А. Иванов'))
