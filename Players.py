class Players:
    __instance = None
    Name = "Bobo"
    HP = 100
    Power = 15

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, hp, power):
        self.Name = name
        self.HP = hp
        self.Power = power


class Player1(Players):

    def __init__(self, name, x, y, hp, power):
        super().__init__(name, hp, power)
        self.X = x
        self.Y = y


class Player2(Players):

    def __init__(self, name, x, y, hp, power):
        super().__init__(name, hp, power)
        self.X = x
        self.Y = y

