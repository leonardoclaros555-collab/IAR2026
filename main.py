class Statistics:
    def __init__(self, lista):
        self._lista = lista

    def suma(self):
        suma1 = sum(self._lista)
        return suma1

    def canti(self):
        canti1 = len(self._lista)
        return canti1

    def prome(self):
        prome1 = sum(self._lista) / len(self._lista)
        return prome1
    
    
list1 = [2, 4, 5]  # suma
list2 = [3, 2]  # tamaño
list3 = [1234, 789763, 245679]  # promedio

stat1 = Statistics(list1)
stat2 = Statistics(list2)
stat3 = Statistics(list3)

print(stat1.suma())

tam = stat2.canti()
print(tam)

prom1 = stat3.prome()
print(prom1)

print(stat3.prome())