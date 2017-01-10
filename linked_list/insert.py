# Simple mprogram for Inserting the node in the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    #Iterates and print the list from start i.e. head
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    # For inserting node from front        
    def push(self, new_data):
        #Allocating Memory for new node
        new_node = Node(new_data)
        #Pointing new node's next to head
        new_node.next = self.head
        #Changing head to the new_node
        self.head = new_node
        
    def insert_after(self, prev_node, new_data):
        #Steps
        #1. Search for the prev_node presetnt or Not.
        if prev_node is None:
            print('No prev node available')
            
        # Else make the node and assign the pointer of prev node to the new_node
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def append(self, new_data):
        #1. Create new node.
        new_node = Node(new_data)
        #2. Traverse to find the last node. Two cases a) If the List is Empty, b) If the List is not Empty
        #a) If the List is empty, assign the tail to new node and return.
        if self.head is None:
            self.head = new_node
            return
        
        tail = self.head
        #Traverse till the last, and assign the tail
        while(tail.next):
            tail = tail.next
        
        tail.next = new_node
        
        
if __name__ == '__main__':
     #The Code Execution Starts here.
     l_list = LinkedList()
     
     l_list.push(1)
     l_list.push(2)
     l_list.append(3)
     l_list.append(4)
     l_list.insert_after(l_list.head.next, 6)
     
     l_list.print_list()