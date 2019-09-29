class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.next = self.tail 
        
        self.num_of_data = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next= new_node
        self.num_of_data += 1
    
    def pop(self):
        temp = self.head.next
        if temp == self.tail :
            return -1
        else:
            self.head.next = temp.next
            return temp.data
    
    def print_node(self):
        temp = self.head.next
        while temp != self.tail:
            print(str(temp.data) + " ")
            temp = temp.next
            
        

if __name__ == "__main__":
    linked_list = Stack()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    linked_list.pop()
    linked_list.print_node()
        
        
        
    