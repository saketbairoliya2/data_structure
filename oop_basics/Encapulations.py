class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_name(self):
        print(self.name)
        
    def say_age(self):
        print(self.age)
        

if __name__ == "__main__":
    
    a_person = Person("Saket", 24)
    #Accessing the name value through the object name.
    print(a_person.name) # It'll access the name variable of the object defined here.
    
    #print(name) -> This is a wrong way to access name, since the name is incapsulated inside the class.
    