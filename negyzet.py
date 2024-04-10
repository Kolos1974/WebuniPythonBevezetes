class Négyzet:
    def __init__(self, a):
        self.a = a
    def terület(self):
        return self.a * self.a
    def kerület(self):
        return 4 * self.a

négyzet1 = Négyzet(3)
négyzet2 = Négyzet(4)

print(négyzet1.terület()) # 9
print(négyzet1.kerület()) # 12
print(négyzet2.terület()) # 16
print(négyzet2.kerület()) # 16
