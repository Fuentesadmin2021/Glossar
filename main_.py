
    def insertAfter(self, positionValue, data):
        prevNode = self.find(positionValue)
        if prevNode is None:
            print("The position doesn't exist")
            return False
        newNode = node(data)
        newNode.next = prevNode.next
        prevNode.next.prev = newNode
        prevNode.next = newNode
        newNode.prev = prevNode
        if prevNode is self.tail:
            self.tail = newNode
        return True


    def delete(self, delValue):
        if self.isEmpty():
            raise Exception("Cannot delete from empty linked list")
            return False
        delNode = self.find(delValue)
        aux = delNode.prev
        delNode.prev.next = aux.next
        delNode.next.prev = aux
        return True

#--------------------------------------

class Glossar:

    def toRepNumer(self, palabra):
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
        repNumer = []
        for letra in palabra:
            repNumer.append(alfabeto[letra])
        return repNumer



    def insertAlphabetOrd(self,wordToAdd,list):

        if isinstance(wordToAdd, str):
            codedWord = self.toRepNumer(wordToAdd)
            ptr = list.head

        if list.length<=0 :
            list.insertHead(node(wordToAdd))

        elif list.length >= 1:
            while ptr != None:
                try:
                    arrPtr = self.toRepNumer(ptr.data) 
                    arrNext = self.toRepNumer(ptr.next.data)

                    for i in range (0,codedWord.length):

                        #Look other words
                        if arrPtr[i] < codedWord[i] and arrNext[i] < codedWord[i]:
                            break
                        #Continue checking words
                        if arrPtr[i] == codedWord[i] and arrNext[i] == codedWord[i]: 
                            continue 
                        #Continue checking words
                        if arrPtr[i] <= codedWord[i] and arrNext[i] == codedWord[i]: 
                            continue 
                        #Founded place
                        if arrPtr[i] <= codedWord[i] and arrNext[i] > codedWord[i]:
                        
                            newNode = node(wordToAdd)
                            newNode.next = ptr.next
                            ptr.next.prev = newNode
                            ptr.next = newNode
                            newNode.prev = ptr
                            if ptr is list.tail:
                                list.tail = newNode

                    ptr = ptr.next
            
                except TypeError: 
                    newNode = node(wordToAdd)
                    if list.head is None and list.tail is None:
                        list.tail = list.tail = newNode
                    else:
                        newNode.prev = list.tail
                        list.tail = newNode
                        newNode.prev.next = newNode
    
        else:
            raise Exception("ERROR: dato ingresado no es un String")


#--------------------------------------
#MAIN CODE

menu_prin = """
-  -  -  -  -  -  -  -  -  -  -  -  -  -  
(1) -> Ingresar datos al Glossar
(2) -> Eliminar datos al Glossar
(3) -> Print
(4) -> Descargar archivo .txt del Glossar

¿Qué le gustaría hacer?:"""

sub_in = """
Inserte un dato: """

sub_inNew = """
¿Quiere ingresar otro dato (SÍ/1) (NO/0)?: """

sub_elim = """
Dato a eliminar: """

sub_elimNew = """
¿Quiere eliminar otro dato (SÍ/1) (NO/0)?: """

retorno = """
¿Quiere hacer continuar el programa (SÍ/1) (NO/0)?: """

def run():
    dll = DLL()
    glossar = Glossar()
    x = 1
    print("Bienvenido al prototipo de glosario:")
    while  x == 1:
        z = int(input(menu_prin))
    
        if z == 1: #INSERT
            var_1 = 1
            while var_1 == 1:
                wordInsert = input(sub_in)
                glossar.insertAlphabetOrd(wordInsert, dll)
        
                var_1aux = input(sub_inNew)
        
                try:
                    var_1aux = int(var_1aux)
                except ValueError:
                    continue

                if isinstance(var_1aux, int):
                    var_1 = var_1aux
                else:
                    raise Exception("ERROR: Input debe ser un entero")
                    var_1 = 1


        elif z == 2: #DELETE
            var_1 = 1
            while var_1 == 1:
                print(sub_elim)
                wordInsert = input(sub_elim)
                glossar.insertAlphabetOrd(wordInsert, dll)
                var_1 = int(input(sub_elimNew))
                if isinstance(var_1, int):
                    continue
                else:
                    var_1 = 1


        elif z == 3: #PRINT
            print(ptr)
            while ptr:
                print(ptr.data, end = "")
                ptr = ptr.next


        x = int(input(retorno))      

if __name__ == '__main__':
    run()


 aux = self.head
        while aux:
            if aux.data != goal:
                aux = aux.next
            else:
                return aux.data

aux = self.head
        while self.head:
            if self.get_head_data() != goal:
                self.head = self.head.next
            else:
                return self.head.data
        self.head = aux