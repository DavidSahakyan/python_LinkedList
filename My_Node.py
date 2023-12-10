class Node:
    def __init__(self, a = None, prev = None, next = None):
        self.__prev = prev
        self.__next = next
        self.__a = a
        
    def get_a(self):
        return self.__a
    
    def get_prev(self):
        return self.__prev
    
    def get_next(self):
        return self.__next
    
    def set_a(self, a):
        self.__a = a
    
    def set_prev(self, prev):
        self.__prev = prev
    
    def set_next(self, next):
        self.__next = next
        