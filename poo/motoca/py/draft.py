class Pessoa:
    def __init__(self, name: str = "", age: int = 0):
        self.__name: str = name
        self.__age: int = age
        
    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"

class Moto:

    def __init__(self):
        self.__power: int = 1
        self.__time: int = 0
        self.__person: Pessoa | None = None

    def getPower(self) -> int:
        return self.__power

    def getTime(self) -> int:
        return self.__time

    def getPerson(self) -> Pessoa | None:
        return self.__person

    def inserir(self, person: Pessoa) -> bool:
        if self.__person != None:
            print("fail: busy motorcycle")
            return False
        else: 
            self.__person = person
            return True

    def remover(self, Pessoa = None):
        if self.__person is None:
            print("fail: empty motorcycle")
            return None
        aux: Pessoa = self.__person
        self.__person = None
        print(aux)

    def drive(self, time: int):
        if self.__time == 0:
            print("fail: buy time first")
            return
        if self.__person is None:
            print("fail: empty motorcycle")
            return
        if self.__person.get_age() > 10:
            print("fail: too old to drive")
            return
        if time > self.__time:
            print (f"fail: time finished after {self.__time} minutes")
            self.__time = 0
            return
        self.__time -= time

    def __str__(self) -> str:
        return f"power:{self.__power}, time:{self.__time}, person:({"empty" if self.__person == None else self.__person})"

    def init(self, power: int = 1):
        self.__person = None
        self.__time = 0
        self.__power = power
        return

    def honk(self) -> str:
        return "P" + "e" * self.__power + "m"

    def buyTime(self, time: int):
        self.__time += time

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
        elif args[0] == "enter":
            name = str(args[1])
            age = int(args[2])
            person = Pessoa(name, age)
            moto.inserir(person)
        elif args[0] == "leave":
            moto.remover()
        elif args[0] == "drive":
            time = int(args[1])
            moto.drive(time)
        elif args[0] == "buy":
            moto.buyTime(int(args[1]))
        elif args[0] ==  "honk":
            print(moto.honk())
        elif args[0] == "init":
            power = int(args[1])
            moto.init(power)
    
    
        
main()




