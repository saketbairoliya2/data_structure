####
#The code to show the Principle of Inheritance 
####

class Person(object):
    
    def __init__(self, name):
        self.name = name
        
class Student(Person):
    
    def __init__(self, name, age):
        super(Student, self).__init__(name)
        self.age = age
        
    def get_student_details(self):
        print("Student here is {} of age {}" .format(self.name, self.age))
        
        
if __name__ == "__main__":
    student = Student("saket", 25)
    student.get_student_details()