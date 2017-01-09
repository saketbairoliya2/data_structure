# A program to Introdce Linked List

#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Linked List Clas containing Node inside.
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Function Prints List content starting from head   
    def print_list(self):
        #print('Print list Called!!')
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code Execution will start here.
if __name__ == '__main__':
    l_list = LinkedList() #Start with Empty List
    
    l_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    l_list.head.next = second
    second.next = third
    
    l_list.print_list()