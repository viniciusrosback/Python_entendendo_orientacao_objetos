class Cliente:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        print("chamando @property nome()")
        return self.nome.tittle()

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome

