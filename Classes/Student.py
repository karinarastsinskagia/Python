class Student:

    def __init__(self, id, name, age, *student_class):
        self.id = id
        self.name = name
        self.age = age
        self.student_class = student_class

    def set_student_class(self,st_name, class_level):
        self.student_class = class_level
        return f'Student Name: {st_name}\nClass: {class_level}'

    def student_data(self, **args):
        print(f'Student id is : {self.id}')
        print(args)
        if 'student_name' in args:
            print(f'Student name is : {self.name}')

        if 'student_class' in args:
            print(f'Student class is : {self.student_class}')

        return None

    def display_student_data(self):

        for attr,value in self.__dict__.items():
            print(f'{attr} -> {value}')

class Marks:
    pass

student = Student(1,'Wilson Medina',12)
print(student.__dict__)
print((isinstance(student,Student)))
print((isinstance(student,Marks)))


print(student.set_student_class('Wilson Medina','A'))
print(student.student_data())
print(student.student_data(student_name='Wilson Medina',stundet_class='A'))

#Update student's attribute in different ways
print("The Student's name is : ",student.name)

student.name = "Wilson A"
print("The Student's name is : ",student.name)

student.__setattr__("name","Wilson B")
print("The Student's name is : ",student.name)

setattr(student,"name","Wilson C")
print("The Student's name is : ",getattr(student,'name'))

print("Display all student's data:")
student.display_student_data()

del student.student_class

print("Display all student's data:")
student.display_student_data()




