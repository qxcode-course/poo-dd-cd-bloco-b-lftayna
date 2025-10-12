class Chinela:
    def _init_(self, tamanho: int = 0):
        self.__tamanho = tamanho

    def set_tamanho(self, valor: int) -> bool:
        if valor % 2 != 0:
            print(f"valor invalido")
            return False 
        if valor < 20 or valor > 50:
            return False
        if self.__tamanho == valor:
            return True
        
    def get_tamanho(self) -> int: 
        return self.__tamanho

    def _str_(self) -> str:
        return f"{self.__tamanho}"

def main(): 
    chinela = Chinela()
    while chinela.get_tamanho() == 0:
        valor = int(input("digite o tamanho de sua chinela!"))
        if chinela.set_tamanho(valor) == True:
            break

        print("compra obtida com sucesso! tamanho da chinela: ", chinela.get_tamanho())

main()