# Python для начинающих 6
# Задание №2
# Реализовать поиск по полям, типа: рост больше 120, имя Наташа

from pprint import pprint                                                                   #подключение модуля

class Person:                                                                               #создание класса
    def __init__ (self, surname, adress, yearbirth, hight, weight, colorhair, coloreyes):
        self.surname, self.adress, self.yearbirth, self.hight, self.weight, self.colorhair, self.coloreyes = surname, adress, yearbirth, hight, weight, colorhair, coloreyes
        self.key = (surname, adress)
    def __repr__ (self):
        return "Person('%s','%s','%s','%s','%s','%s','%s')" % (self.surname, self.adress, self.yearbirth, self.hight, self.weight, self.colorhair, self.coloreyes)

medovschikov = Person("Медовщиков", "Сибирская, 1, 13", 1991, 178, 82, "русые", "карие")    #создание объектов класса
ivanov = Person("Иванов", "Лесная, 2, 22", 1994, 188, 80, "белые", "голубые")
petrov = Person("Петров", "Южная, 3, 31", 1999, 170, 82, "черные", "зеленые")
                                                                                            #создание словаря объектов
people = {
    medovschikov.key: medovschikov,
    ivanov.key: ivanov,
    petrov.key: petrov
}

print("Поля для поиска:\n0.ФИО\n1.Адрес\n2.Год рождения\n3.Рост\n4.Вес\n5.Цвет волос\n6.Цвет глаз") #информациюнное сообщение для начала процесса поиска

num_search = int(input("Введите цифру соответствующую полю по которому будет выполнен поиск: "))    #ввод числа с клавиатуры для определения поля по которому будет выполнен поиск, преобразование введеных данных str -> int 

if num_search == 0:                                                                                 #определение поля для поиска путем проверки какое число было введено пользователем с клавиатуры
   search = input("Введите Фамилию: ")                                                              #ввода данных с клавиатуры для поиска
   import fun_search_str                                                                            #подключение функции для выполнения поиска по словарю
   print (fun_search_str.fun_search_str (people, num_search, search))                               #вывод результата работы подключенной функции на экран
if num_search == 1:                                                     
   search = input("Введите адрес (Улица, дом, квартира): ")
   import fun_search_str
   print (fun_search_str.fun_search_str (people, num_search, search))
if num_search == 2:
   search = int(input("Введите год рождения (YYYY): "))
   import fun_search_str
   print (fun_search_str.fun_search_str (people, num_search, search))
if num_search == 3:
   search_from = int(input("Введите рост (в см), От: "))
   search_to = int(input("Введите рост (в см), До: "))
   import fun_search_int
   print (fun_search_int.fun_search_int (people, num_search, search_from, search_to))
if num_search == 4:
   search_from = int(input("Введите вес (в кг), От "))
   search_to = int(input("Введите вес (в кг), До "))
   import fun_search_int
   print (fun_search_int.fun_search_int (people, num_search, search_from, search_to))
if num_search == 5:
   search = input("Введите цвет волос: ")
   import fun_search_str
   print (fun_search_str.fun_search_str (people, num_search, search))
if num_search == 6:
   search = input("Введите цвет глаз: ")
   import fun_search_str
   print (fun_search_str.fun_search_str (people, num_search, search))
