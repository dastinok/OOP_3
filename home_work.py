#Создайте класс студента. ○Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
#○Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
#○Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
#○Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv


class Names:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: str):
        if value.istitle() == False:
            raise ValueError(f'Значение {value} должно с заглавной буквы ')
        if value.isalpha() == False:
            raise ValueError(f'Значение {value} не должно содержать цыфры')

class Scores:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value
    def __set_name__(self, owner, name):
        self.param_name = "_" + name
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    def validate(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class Subjects:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: str):
        data = []
        with open('sub.csv', 'r', newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                data.append(''.join(line))

            if value not in data:
                raise ValueError(f'Значение {value} нет в списке ')
class Student:
    name = Names(str)
    family_name = Names (str)
    last_name = Names (str)
    score = Scores(2, 5)
    res_test = Scores(0, 100)

    subject = Subjects(str)

    def __init__(self, name, family_name, last_name, subject, score, res_test):
        self.name = name
        self.family_name_name = family_name
        self.last_name = last_name
        self.subject = subject
        self.res_test = res_test
        self.score = score

student = Student('Nade', 'Sevostyanova', 'Sergeevna', 'Math', 5, 96)