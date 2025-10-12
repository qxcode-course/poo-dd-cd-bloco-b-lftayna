class Roupa:
        def __init__(self):
            self.__size: str = ""
            self.size: list[str] = ["PP", "P", "M", "G", "GG", "XG"]

        def set_size(self, valor: str):
            if valor in self.size:
             self.__size = valor

            else: 
                print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

        def get_size(self) -> str:
            return self.__size

        def __str__(self):
            return f"{self.__size}"

def main():
    roupa = Roupa ()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(f"size: ({roupa.get_size()})")
        if args[0] == "size":
            roupa.set_size(args[1])

main()




        