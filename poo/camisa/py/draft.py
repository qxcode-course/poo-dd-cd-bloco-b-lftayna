class Camisa:
    def __init__(self, __tamanho: str = ""):
        self.__tamanhocamisa: str = ""
        self.Tamanhos: list[str] = ["PP", "P", "M", "G", "GG", "XG"]

    def getTamanho(self) -> str:
        return self.__tamanhocamisa

    def setTamanho(self, valor: str) -> bool:
        if valor in self.Tamanhos:
            self.__tamanhocamisa = valor 
            return True

        else: 
            print(f"Tamanho inválido! Os tamanhos permitidos são: PP, P, M, G, GG, XG")
            return False

def main():
    camisa = Camisa()
    while camisa.getTamanho() == "":
        print(f"Digite seu tamanho de roupa")
        tamanho = input()
        if camisa.setTamanho(tamanho) == True:
            print(f"Parabens, você comprou uma roupa tamanho", camisa.getTamanho())
            break
            
main()

