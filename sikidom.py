class Téglalap:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def terület(self):
        return self.a * self.b
    def kerület(self):
        return 2 * (self.a + self.b)

téglalap1 = Téglalap(3, 4)
téglalap2 = Téglalap(5, 2)

print(téglalap1.terület()) # 12
print(téglalap1.kerület()) # 14

print(téglalap2.terület()) # 10
print(téglalap2.kerület()) # 14
