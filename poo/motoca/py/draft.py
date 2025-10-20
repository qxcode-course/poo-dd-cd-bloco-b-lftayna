class Pessoa:
    def __init__(self, name: str = "", age: int = 0):
        self.__name: str = ""
        self.__age: int = 0
        
    def get_name(self) -> str:
        return self.__name
    def get_age(self) -> int:
        return self.__age

    def lerpessoa(self) -> str:
        return f"{self.__name}:{self.__age}"

class Moto:

    def __init__(self, power: int = 1, time: int = 0, person: Pessoa = None):
        self.__power: int = 1
        self.__time: int = 0
        self.__person: Pessoa | None = "empty"

    def inserir(self, pessoa = Pessoa) -> bool:
        if self.__person != None:
            print("fail: busy motorcycle")
            return False
        else: 
            self.__person = pessoa
            return True

    def remover(self, Pessoa = None):
        if self.__person != None:
            print("fail: empty motorcycle")
            return None
        aux: Pessoa = self.__cliente
        self.__cliente = None
        return aux

    def drive(self, tempo: int):
        if self.__tempo == 0:
            print("fail: buy time first")
        if self.__cliente == 0:
            print("fail: empty motorcycle")
        if self.__age > 10:
            print("fail: too old to drive")
            


def main():
    moto = Moto()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            return f"power:{moto.power}, time:{moto.time}, person:{moto.lerpessoa}"

main()




