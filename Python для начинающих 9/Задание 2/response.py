from random import randint # модульдля генерации случайных чисел 

# Функция принимает на вход вопрос и список вопросов, добавляет вопрос
# в список, генерирует случайный ответ, используя остаток от деления и
# возвращает отредактированный спосок с ответом
def func_response (question, list_questions):

    list_questions.append(question)
    random_number = randint(0,9)
    random_number %= 2
    if random_number == 0:
        result = "Ответ: Нет"
    else:
        result = "Ответ: Да"
    
    return list_questions, result
