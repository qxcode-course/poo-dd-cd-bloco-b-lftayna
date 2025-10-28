class Pessoa:
    def __init__(self, name: str = "", dinheiro: int = 0):
        self.__name: str = name
        self.__dinheiro: int = dinheiro

    def get_name(self) -> str:
        return self.__name

    def set_dinheiro(self, valor: int):
        self.__dinheiro = valor

    def get_dinheiro(self) -> int:
        return self.__dinheiro

    def pagar(self, valor:int) -> bool:
        if self.__dinheiro >= valor:
            self.__dinheiro -= valor
            return True
        else:
            return False

    def receberdinheiro(self, valor: int):
        self.__dinheiro += valor

    def __str__(self) -> str:
        return f"{self.__name}:{self.__dinheiro}"
        
class Moto: 
    def __init__(self, passageiro: Pessoa | None = None, motorista: Pessoa | None = None):
        self.__custo: int = 0
        self.__passageiro: Pessoa | None = None
        self.__motorista: Pessoa | None = None

    def get_custo(self) -> int:
        return self.__custo

    def get_passageiro(self) -> Pessoa | None:
        return self.__passageiro 

    def get_motorista(self) -> Pessoa | None:
        return self.__motorista 

    def setDriver(self, motorista: Pessoa):
        if self.__motorista == None:
           self.__motorista = motorista
        
    def setPass(self, passageiro: Pessoa):
        if self.__motorista == None:
            return
        if self.__passageiro is not None:
            return
        self.__passageiro = passageiro
        self.__custo = 0

    def drive(self, km: int):
        if self.__motorista == None:
            return
        if self.__passageiro == None:
            return
        if km <= 0:
            return
        self.__custo += km

    def leavePass(self) -> bool:
        if self.__passageiro is None:
            return False 

        aux = self.__passageiro.get_dinheiro()
        if aux >= self.__custo:
            self.__passageiro.pagar(self.__custo)
            self.__motorista.receberdinheiro(self.__custo)
            print(f"{self.__passageiro} left")

        else: 
            self.__passageiro.pagar(aux)
            self.__motorista.receberdinheiro(self.__custo)
            print(f"fail: Passenger does not have enough money")
            print(f"{self.__passageiro} left")


        self.__passageiro = None
        self.__custo = 0
        return True

    def __str__(self) -> str:
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"
    
def main():
    moto = Moto()
    while True:
        line: str = input()
        print("$" + line)
        args : list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(moto)
        if args[0] == "setDriver":
            name = str(args[1])
            dinheiro = int(args[2])
            pessoa = Pessoa(name, dinheiro)
            moto.setDriver(pessoa)
        if args[0] == "setPass":
            name = str(args[1])
            dinheiro = int(args[2])
            pessoa = Pessoa(name, dinheiro)
            moto.setPass(pessoa)
        if args[0] == "drive":
            km = int(args[1])
            moto.drive(km)
        if args[0] == "leavePass":
            moto.leavePass()    
main()

    
