#Доработаем задачу 1.
#Создайте менеджер контекста, который при выходе
#сохраняет значения в JSON файл.
import json
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

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        new_file = open('man_file.json', 'w', encoding='utf-8')
        json.dump(self.results, new_file, indent=4, ensure_ascii=False)
        new_file.close()


fact = Factorial()

fact(3)
fact(1)
fact(4)

print(fact)
with fact as new_file:
    new_file(10)