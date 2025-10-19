class Watch:
    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        self.set_minuto(minuto)
        self.set_segundo(segundo)
        self.set_hora(hora)

    def set_hora(self, hora: int = 0): # escrita
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
            return
        self.__hora = hora

    def set_minuto(self, minuto: int = 0):
        if minuto < 0 or minuto > 59:
            print("fail: minuto invalido")
            return
        self.__minuto = minuto

    def set_segundo(self, segundo: int = 0):
        if segundo < 0 or segundo > 59:
            print("fail: segundo invalido")
            return
        self.__segundo = segundo
            
    def mostrarHora(self):
            return f"{self.__hora:02}:{self.__minuto:02}:{self.__segundo:02}"

    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto += 1

        if self.__minuto > 59:
            self.__minuto = 0
            self.__hora += 1

        if self.__hora > 23:
            self.__hora = 0

    def get_hora(self) -> int: 
        return self.__hora

    def get_minuto(self) -> int: 
        return self.__minuto

    def get_segundo(self) -> int: 
        return self.__segundo

def main():
    relogio = Watch ()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(relogio.mostrarHora())
        if args[0] == "hora":
            relogio.set_hora(int(args[1]))
        if args[0] == "set":
            relogio.set_hora(int(args[1]))
            relogio.set_minuto(int(args[2]))
            relogio.set_segundo(int(args[3]))
        if args[0] == "init":
            relogio = Watch(int(args[1]), int(args[2]), int(args[3]))
        if args[0] == "next":
            relogio.nextSecond()
main()