# Создание класса, используя конструктор.
class Person:
    def __init__(self, surname, adress, yearbirth, hight, weight, colorhair,
                 coloreyes):
        self.surname = surname
        self.adress = adress
        self.yearbirth = yearbirth
        self.hight = hight
        self.weight = weight
        self.colorhair = colorhair
        self.coloreyes = coloreyes
        self.key = (surname, adress)
        
    def __repr__(self):        
        return "Person('%s','%s','%s','%s','%s','%s','%s')" % (self.surname,
                                                               self.adress,
                                                               self.yearbirth,
                                                               self.hight,
                                                               self.weight,
                                                               self.colorhair,
                                                               self.coloreyes)

# Создание объектов класса.
medovschikov = Person("Медовщиков", "Сибирская, 1, 13", "1991", "178", "82",
                      "русые", "карие")
ivanov = Person("Иванов", "Лесная, 2, 22", "1994", "188", "80", "белые",
                "голубые")
petrov = Person("Петров", "Южная, 3, 31", "1999", "170", "82", "черные",
                "зеленые")

# Создание словаря объектов класса.
PEOPLE = {
    medovschikov.key: medovschikov,
    ivanov.key: ivanov,
    petrov.key: petrov
}
