from My_Node import Node

class LinkedList:
    def __init__(self, *args):
        self.__n = Node()
        self.__len = 0
        
        for i in args:
            self.append(i)
            
        
    def append(self, a):
        temp = self.__n
        
        if self.__len == 0:
            self.__n.set_a(a)
            self.__len += 1
            return
        
        while temp.get_next() != None:
            temp = temp.get_next()
        
        self.__len += 1    
        temp.set_next(Node(a, self))
        
    def prepend(self, a):
        self.__n.set_prev(Node(a, None, self.__n))
        self.__n = self.__n.get_prev()
        self.__len += 1  
        
    def insert_after(self, target_data, a):
        temp = self.__n
        
        try:
            while temp.get_a() != target_data:
                temp = temp.get_next()
        except(AttributeError):
            return
        
        temp_node = temp.get_next()
        temp.set_next(Node(a, temp, temp_node))
        self.__len += 1
    
    def insert_before(self, target_data, data):
        temp = self.__n
        
        if self.__n.get_a() == target_data:
            self.prepend(data)
            return
            
        
        try:
            while temp.get_next().get_a() != target_data:
                temp = temp.get_next()
        except(AttributeError):
            return
        
        temp.set_next(Node(data, temp, temp.get_next()))
                        
        self.__len += 1
        
    def delete(self, data):
        temp = self.__n
        
        if self.__n.get_a() == data:
            self.__n = self.__n.get_next()
            self.__n.set_prev(None)
            self.__len -= 1
            return
        
        try:
            while temp.get_a() != data:
                temp = temp.get_next()
        except(AttributeError):
            return
       
        temp.get_prev().set_next(temp.get_next())  
        self.__len -= 1
        
        
    def display(self, sep = '\n'):
        temp = self.__n
        
        while temp != None:
            print(temp.get_a(), sep = sep)
            temp = temp.get_next()
            
    def is_empty(self):
        return not bool(self.__len)
    
    def length(self):
        return self.__len