# Example for function Overloading.

class Human():
    
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    
    def print_message(self):
        if self.name != None and self.age != None:
            print("A Human named {}, of age {} is here." .format(self.name, self.age))
        
        elif self.name != None:
            print("A Human named {} is here." .format(self.name))
            
        elif self.age != None:
            print("A Human of age {} is here." .format(self.age))
            
        else:
            print("A Human of is here.")
        
        
if __name__ == "__main__":
    human = Human()
    human.print_message()
    # Wil pass None Parameters to the class
    
    one_human = Human("saket")
    one_human.print_message()
    #Will Pass One Params to the class
    
    two_human = Human("Saket", 24)
    two_human.print_message()
    #Will pass Two Params to the class