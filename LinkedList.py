from My_Node import Node

class LinkedList:
    def __init__(self, *args):
        self._n = Node()
        self._len = 0
        
        for i in args:
            self.append(i)
            
        
    def append(self, a):
        temp = self._n
        
        if self._len == 0:
            self._n._a = a
            self._len += 1
            return
        
        while temp._next != None:
            temp = temp._next
        
        self._len += 1    
        temp._next = Node(a, self)
        
    def prepend(self, a):
        self._n._prev = Node(a, None, self._n)
        self._n = self._n._prev
        self._len += 1  
        
    def insert_after(self, target_data, a):
        temp = self._n
        
        try:
            while temp._a != target_data:
                temp = temp._next
        except(AttributeError):
            return
        
        temp_node = temp._next
        temp._next = Node(a, temp, temp_node)
        self._len += 1
    
    def insert_before(self, target_data, data):
        temp = self._n
        
        try:
            while temp._a != target_data:
                temp = temp._next
        except(AttributeError):
            return
        
        temp._prev._next = Node(data, temp._prev, temp)
        self._len += 1
        
    def delete(self, data):
        temp = self._n
        
        if self._n._a == data:
            self._n = self._n._next
            self._n._prev = None
            self._len -= 1
            return
        
        try:
            while temp._a != data:
                temp = temp._next
        except(AttributeError):
            return
       
        temp._prev._next = temp._next
        self._len -= 1
        
        
    def display(self):
        temp = self._n
        
        while temp != None:
            print(temp._a)
            temp = temp._next
            
    def is_empty(self):
        return not bool(self._len)
    
    def length(self):
        return self._len
    
    
a = LinkedList()

a.append(1)
a.prepend(1)
a.insert_after(1, 4)
a.delete(4)
a.append(1)

a.display()