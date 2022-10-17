# ------------------------------- nodo class ---------------------------------



class Node:

    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None

# ----------------------------- dlinked class --------------------------------



class Dlinked_list:

    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0

    def empty(self):
        return self.head == None

    def add_back(self, data):
        if self.empty():
            self.head = self.tail = Node(data)

        else:
            aux = self.tail
            self.tail = aux.next = Node(data)
            self.tail.prev = aux
        self.length += 1

    def add_front(self, data):
        if self.empty():
            self.head = self.tail = Node(data)

        else:
            aux = Node(data)
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

    """
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
    """
        
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
                node_insert = Node(data_insert)
                node_next = node_prev.next
                node_insert.next = node_next
                node_next.prev = node_insert
                node_insert.prev = node_prev
                node_prev.next = node_insert
            except AttributeError:
                self.add_back(data_insert)

    def delete(self, value_to_del):
        if self.empty():
            raise Exception("Cannot delete from empty linked list")
            return False


        node_to_del = self.find_node_from_value(value_to_del)

        # first node case
        if node_to_del.prev is None:
            self.head = node_to_del.next

        # last node case
        elif node_to_del.next is None:
            self.tail = node_to_del.prev

        # middle node case
        # if (node_to_del.next is not None) and (node_to_del.prev is not None)
        else:
            node_to_del.prev.next = node_to_del.next
            node_to_del.next.prev = node_to_del.prev      
        return True

# ----------------------------- glossar class --------------------------------



class Glossar(Dlinked_list):

    # constructor to
    def __init__(self):
        Dlinked_list.__init__(self)
        self.head = None
        self.tail = None 
        self.length = 0

    # transform string "abc" to numeric representation "[1,2,3]"
    def transform_to_numeric_representation(self, palabra):
        alfabeto = {
        "A":1,"Á":1,"Ä":1,"a":1,"á":1,"ä":1,
        "B":2,"b":2,
        "C":3,"c":3,
        "D":4,"d":4,
        "E":5,"É":5,"Ë":5,"e":5,"é":5,"ë":5,
        "F":6,"f":6,
        "G":7,"g":7,
        "H":8,"h":8,
        "I":9,"Í":9,"Ï":9,"i":9,"í":9,"ï":9,
        "J":10,"j":10,
        "K":11,"k":11,
        "L":12,"l":12,
        "M":13,"m":13,
        "N":14,"n":14,
        "Ñ":15,"ñ":15,
        "O":16,"Ó":16,"Ö":16,"o":16,"ó":16,"ö":16,
        "P":17,"p":17,
        "Q":18,"q":18,
        "R":19,"r":19,
        "S":20,"s":20,
        "T":21,"t":21,
        "U":22,"Ú":22,"Ü":22,"u":22,"ú":22,"ü":22,
        "V":23,"v":23,
        "W":24,"w":24,
        "X":25,"x":25,
        "Y":26,"y":26,
        "Z":27,"z":27,
        " ":28
        }
        numeric_representation = []
        for letra in palabra:
            numeric_representation.append(alfabeto[letra])
        return numeric_representation


    def insert_in_alhpabet_order(self, word_to_add):

        if isinstance(word_to_add, str):
            coded_word = self.transform_to_numeric_representation(word_to_add)
            pointer = self.head
        else:
            raise Exception("Error, The input is not a string")

        if self.empty():
            self.add_back(word_to_add)

        else:
            while pointer:
                try:
                    coded_pointer = self.transform_to_numeric_representation(pointer.data) 
                    coded_next_pointer = self.transform_to_numeric_representation(pointer.next.data)

                    recorrido = []
                    recorrido.append(len(coded_word))
                    recorrido.append(len(coded_pointer))
                    recorrido.append(len(coded_next_pointer))

                    recorrido = min(recorrido)

                    for i in range (0, recorrido):

                        #Look other words
                        if coded_pointer[i] < coded_word[i] and coded_next_pointer[i] < coded_word[i]:
                            break
                        #Continue checking words
                        if coded_pointer[i] == coded_word[i] and coded_next_pointer[i] == coded_word[i]: 
                            continue 
                        #Continue checking words
                        if coded_pointer[i] <= coded_word[i] and coded_next_pointer[i] == coded_word[i]: 
                            continue 
                        #Founded place
                        if coded_pointer[i] <= coded_word[i] and coded_next_pointer[i] > coded_word[i]:
                        
                            newNode = Node(word_to_add)
                            newNode.next = pointer.next
                            pointer.next.prev = newNode
                            pointer.next = newNode
                            newNode.prev = pointer
                            if pointer is list.tail:
                                list.tail = newNode

                    pointer = pointer.next
            
                except TypeError: 
                    newNode = Node(word_to_add)
                    if list.head is None and list.tail is None:
                        list.tail = list.tail = newNode
                    else:
                        newNode.prev = list.tail
                        list.tail = newNode
                        newNode.prev.next = newNode
# ------------------------ prueba de funcionamiento -------------------------

glosario = Glossar()

glosario.add_back("hola")
glosario.add_back("como")
glosario.add_back("estas")
glosario.add_back("mi")
glosario.add_back("amor")
glosario.add_back("eterno")

glosario.insert_after(None , "Maria, ¿")
glosario.insert_after("mi", "querido")
glosario.insert_after("eterno", "?")

glosario.delete("hola")


glosario.tra_head()