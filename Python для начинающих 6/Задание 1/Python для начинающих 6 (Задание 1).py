# Python для начинающих 6
# Задание №1
# Описать классом(ами) ранее используемые списки с персонажами

#подключаем модуль для удобочитабельного вида списка объектов при выводе
from pprint import pprint
#создаем класс
class Person:
    def __init__ (self, surname, adress, yearbirth, hight, weight, colorhair, coloreyes):
        self.surname, self.adress, self.yearbirth, self.hight, self.weight, self.colorhair, self.coloreyes = surname, adress, yearbirth, hight, weight, colorhair, coloreyes
        self.key = (surname, adress)
    def __repr__ (self):
        return "Person('%s','%s','%s','%s','%s','%s','%s')" % (self.surname, self.adress, self.yearbirth, self.hight, self.weight, self.colorhair, self.coloreyes)
#создаем объекты
medovschikov = Person("Медовщиков", "Сибирская, 1, 13", 1991, 178, 82, "русые", "карие")
ivanov = Person("Иванов", "Лесная, 2, 22", 1994, 188, 80, "белые", "голубые")
petrov = Person("Петров", "Южная, 3, 31", 1999, 170, 72, "черные", "зеленые")
#создаем словарь объектов
people = {
    medovschikov.key: medovschikov,
    ivanov.key: ivanov,
    petrov.key: petrov
}
#выводим словарь созданных объектов
pprint(people)
