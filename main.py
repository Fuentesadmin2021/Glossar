from glossar import Glossar


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