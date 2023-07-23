#Создайте класс-функцию, который считает факториал числа при
#вызове экземпляра.
#Экземпляр должен запоминать последние k значений.
#Параметр k передаётся при создании экземпляра.
#Добавьте метод для просмотра ранее вызываемых значений и
#их факториалов.
from collections import defaultdict


class Factorial:



    def __init__(self):
        self.results = defaultdict(list)
        self.kresults = []
        self.termresults = []

    def __call__(self, number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        self.results[number].append(result)
        self.termresults.append(result)
        if number < len(self.termresults):
            for i in range(len(self.termresults) - number - 1, len(self.termresults)):
                self.kresults.append(self.termresults[i])
        else:
            for i in range(len(self.termresults)):
                self.kresults.append(self.termresults[i])

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.results.items())) + '\n' + '\n'.join((f'{v}' for v in self.kresults))
        return txt

fact = Factorial()

fact(3)
fact(1)
fact(4)

print(fact)






