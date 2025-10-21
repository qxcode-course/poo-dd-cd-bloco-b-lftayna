class Pessoa:
    def __init__(self, name: str = "", age: int = 0):
        self.__name: str = ""
        self.__age: int = 0
        
    def get_name(self) -> str:
        return self.__name
    def get_age(self) -> int:
        return self.__age

    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"

class Moto:

    def __init__(self, power: int = 1, time: int = 0, person: Pessoa = None):
        self.__power: int = 1
        self.__time: int = 0
        self.__person: Pessoa | None = "(empty)"

    def getPower(self, int):
        return self.__power

    def getTime(self, int):
        return self.__time

    def getPerson(self, person = Pessoa):
        return self.__person

    def inserir(self, person = Pessoa) -> bool:
        if self.__person != None:
            print("fail: busy motorcycle")
            return False
        else: 
            self.__person = person
            return True

    def remover(self, Pessoa = None):
        if self.__person != None:
            print("fail: empty motorcycle")
            return None
        aux: Pessoa = self.__person
        self.__person = None
        return aux

    def drive(self, time: int):
        if self.__time == 0:
            print("fail: buy time first")
        if self.__person == None:
            print("fail: empty motorcycle")
        if self.__age > 10:
            print("fail: too old to drive")
        if time <= 0:
            print (f"fail: time finished after {self.__time} minutes")
        self.__time = time

    def __str__(self) -> str:
        return f"power:{self.__power}, time:{self.__time}, person:{self.__person}"

    def buyTime(self, time: int):
        self.__time += time

    def inserir(self, person = Pessoa) -> bool:
        if self.__person == 1:
            print("fail: busy motorcycle")
            return False
        else: 
            self.__person += person
            return True

def main():
    moto = Moto()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(moto)
        if args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            person = Pessoa(nome, idade)
            moto.inserir(person)
main()




