from dict_people import people                                                                      #импорт словаря персонажей из файла dict_people

print("Поля для поиска:\n0.ФИО\n1.Адрес\n2.Год рождения\n3.Рост\n4.Вес\n5.Цвет волос\n6.Цвет глаз")

num_search = int(input("\nВведите цифру соответствующую полю по которому будет выполнен поиск: "))  #выбор поля по которому будет производится поиск
  
import func_search_number                                                                           #импорт функции, которая выводит соответствующий выбранному номеру поля диалог
search = input(func_search_number.func_search_number (num_search))                                  #вывод на экарн диалога и ввод пользователем данных для поиска
import funс_search_unmanifest                                                                       #импорт функции, которая выполняет поиск введенных пользователем данных в словаре персонажей
print (funс_search_unmanifest.funс_search_unmanifest (people, num_search, search))                  #вывод результата поиска на экран в виде списка персонажей
