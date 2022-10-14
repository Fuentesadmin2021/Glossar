# ------------------------------- nodo class ---------------------------------
class node:

    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None

# ----------------------------- dlinked class --------------------------------
class dlinked_list:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0

    def empty(self):
        return self.head == None

    def add_back(self, data):
        if self.empty():
            self.head = self.tail = node(data)

        else:
            aux = self.tail
            self.tail = aux.next = node(data)
            self.tail.prev = aux
        self.length += 1

    def add_front(self, data):
        if self.empty():
            self.head = self.tail = node(data)

        else:
            aux = node(data)
            aux.next = self.head
            self.head.prev = aux
            self.head = aux
        self.length += 1
        
    def tra_head(self):
        aux = self.head
        while aux:
            print(aux.data, end = " ")
            aux = aux.next
        
    def tra_tail(self):
        aux = self.tail 
        while aux:
            print(aux.data)
            aux = aux.prev

    def del_head(self):
        if self.empty():
            print("empty list")

        elif self.head.next == None:
            self.head = self.tail = None
            self.length = 0
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            
    def del_tail(self):
        if self.empty():
            print("empty list")

        elif self.tail.prev == None:
            self.head = self.tail = None
            self.length = 0
            
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        
    def length_list(self):
        return self.length


    def clear_list(self):
        self.head = self.tail = None
        self.length = 0

    def get_head_data(self):
        if self.empty():
            raise  Exception("Empty list")
        return self.head.data

    def get_tail_data(self):
        if self.empty():
            raise Exception("Empty list")
        return self.tail.data
    
    # find specific node from value (goal)
    def find_node_from_value(self, goal):
        aux = self.head
        while aux:
            if aux.data == goal:
                return aux

            aux = aux.next      
    # if not found return None

    def insert_after(self, data_prev, data_insert):
        node_prev = self.find_node_from_value(data_prev)

        # case: null position and empty list
        if node_prev is None:
            self.add_front(data_insert)
        
        # case: middle position and last position
        if node_prev is not None:
            try:
                node_insert = node(data_insert)
                node_next = node_prev.next
                node_insert.next = node_next
                node_next.prev = node_insert
                node_insert.prev = node_prev
                node_prev.next = node_insert
            except AttributeError:
                self.add_back(data_insert)


# ------------------------------- prueba de funcionamiento --------------------------------
mi_lista = dlinked_list()
mi_lista.add_back("hola")
mi_lista.add_back("como")
mi_lista.add_back("estas")
mi_lista.add_back("mi")
mi_lista.add_back("amor")
mi_lista.add_back("eterno")

mi_lista.insert_after(None , "Maria, ¿")
mi_lista.insert_after("mi", "querido")
mi_lista.insert_after("eterno", "?")

mi_lista.tra_head()









        
    
