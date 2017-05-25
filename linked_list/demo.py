# A basic Program for gettting insert working o9n linked List.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    #Pushing things from front 
    def push(self, data):
        #1. Create new Node
        new_node = Node(data)
        
        #2. new_node ->  next is head
        new_node.next = self.head
        
        #3. self.head is noe new_node
        self.head = new_node
        
    # Pushing things at end.
    def append(self, data):
        
        # Traverse till the end and get the last element and add element post that.
        # 2 cases possible, 1. If the head is empty -> assign head to this node.
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        tail = self.head
        while(tail.next):
            tail = tail.next
            
        tail.next = new_node
        
    def delete_node(self, data):
        
        temp = self.head
        
        #1. If temp itself is to be deleted.
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
            
        while(temp is not None):
            if temp.data == value:
                break
            
            prev = temp
            temp = temp.next
            
        if temp == None:
            return
        
        prev.next = temp.next
        
        temp = None
        
    # Pusheing things after a g8uiven position
    def insert_after(self, prev_data, data);
        
if __name__ == '__main__':
    l_list = LinkedList()
    
    l_list.push(1)
    
    