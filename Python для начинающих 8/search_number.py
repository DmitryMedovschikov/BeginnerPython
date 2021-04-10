# Функция определяет и возвращает диалог, который будет выведен на экран
# в зависимости от номера поля по которому необходимо выполнить поиск.
def func_search_number(num_search):
    if num_search == 0:
        num_text = "Введите Фамилию: "
    if num_search == 1:
        num_text = "Введите адрес (Улица, дом, квартира): "
    if num_search == 2:
        num_text = "Введите год рождения (YYYY): "
    if num_search == 3:
        num_text = "Введите рост (см): "
    if num_search == 4:
        num_text = "Введите вес (кг): "
    if num_search == 5:
        num_text = "Введите цвет волос: "
    if num_search == 6:
        num_text = "Введите цвет глаз: "       
    return num_text
