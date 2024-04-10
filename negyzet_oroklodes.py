class Téglalap:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def terület(self):
        return self.a * self.b
    def kerület(self):
        return 2 * (self.a + self.b)


class Négyzet(Téglalap):
    def __init__(self, a):
        super().__init__(a, a)

négyzet1 = Négyzet(3)
négyzet2 = Négyzet(4)

print(négyzet1.terület()) # 9
print(négyzet1.kerület()) # 12
print(négyzet2.terület()) # 16
print(négyzet2.kerület()) # 16

