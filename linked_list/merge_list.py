# This is a simple code for merging two sorted list into one.

# A node for storing linked List.
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# A linked List
class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		#1. create a new node.
		new_node = Node(data)

		#2. new_node -> next = head.
		new_node.next = self.head

		#3. head = new_node
		self.head = new_node

	def print_list(self):
		temp = self.head
		while(temp):
			print (temp.data)
			temp = temp.next

	def merge_list(self, list_a, list_b):
		head_a = list_a.head
		head_b = list_b.head

		while(head_a and head_b):
			if (head_a is not None and head_b is not None):
				if(head_a.data < head_b.data):
					self.push(head_a.data)
					head_a = head_a.next
				else:
					self.push(head_b.data)
					head_b = head_b.next
		while(head_a):
			self.push(head_a.data)
			head_a = head_a.next

		while(head_b):
			self.push(head_b.data)
			head_b = head_b.next


if __name__ == '__main__':

	list_a = LinkedList()
	list_b = LinkedList()

	list_a.push(15)
	list_a.push(10)
	list_a.push(5)

	list_b.push(7)
	list_b.push(5)
	list_b.push(3)
	list_b.push(1)

	list_a.print_list()
	list_b.print_list()

	list_c = LinkedList()
	list_c.merge_list(list_a, list_b)

	print("List after Merging is :")
	list_c.print_list()