#создание класса, используя конструктор
class Person:
    def __init__ (self, surname, adress, yearbirth, hight, weight, colorhair, coloreyes):

        self.surname, self.adress, self.yearbirth, self.hight, self.weight, self.colorhair, self.coloreyes = surname, adress, yearbirth, hight, weight, colorhair, coloreyes
        self.key = (surname, adress)
        
    def __repr__ (self):
        
        return "Person('%s','%s','%s','%s','%s','%s','%s')" % (self.surname, self.adress, self.yearbirth, self.hight, self.weight, self.colorhair, self.coloreyes)
#создание объектов класса
medovschikov = Person("Медовщиков", "Сибирская, 1, 13", "1991", "178", "82", "русые", "карие")
ivanov = Person("Иванов", "Лесная, 2, 22", "1994", "188", "80", "белые", "голубые")
petrov = Person("Петров", "Южная, 3, 31", "1999", "170", "82", "черные", "зеленые")
#создание словаря объектов класса
people = {
    medovschikov.key: medovschikov,
    ivanov.key: ivanov,
    petrov.key: petrov
}
