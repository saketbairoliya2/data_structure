def mimik_switch_case(argument):
    student_roll = {
        1: "saket",
        2: "Rohit",
        3: "Ramesh",
    }
    return student_roll.get(argument, "None found")
    
if __name__ == "__main__":
    print(mimik_switch_case(1))
    

'''
The code below is the equivalent code in Java Langauge, it will not work here, Definitely. :D
def mimik_switch_case(argument):
    switch(argument):
        case 1: return "saket"
        case 2: return "Rohit"
        case 3: return "Ramesh"
        default: return "None found"
'''