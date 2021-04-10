# Функция выполняет поиск по словарю персонажей неявным способом в
# зависимости от введенных пользователем данных и возвращает результат в
# виде списка персонажей, сответствующих кретериям поиска.
def funс_search_unmanifest(PEOPLE, num_search, search):
    result = []  # список для записи результата поиска
    counter = 0  # счетчик для определения количества найденных объектов
    # Инициализация списка двуграм путем среза производимого над
    # введенной пользователем строкой.
    ngrams = [
        search[i:i+2] for i in range(len(search))
        ]
    # 1) Определеяется поле по которому будет выполнен поиск;
    # 2) Выполянется перебор получившегося ранее списка двуграмм;
    # 3) Для каждой двуграммы выполняется перебор списка объектов;
    # 4) Если найдена соответствующая двуграмма, объект добавляется в
    # список result и счетчик увеличивается на 1;
    # 5) Если перебрав список двуграмм не найдено ни одного подходящего
    # критериям поиска объекта, выполняется выход из цикла и функции с
    # соответствующим сообщением.
    if num_search == 0:                             
        for i in ngrams:                            
            for key in PEOPLE:                      
                if i in PEOPLE[key].surname:        
                    result.append(PEOPLE[key])      
                    counter +=1                     
            if counter != 0:                        
                break                               
    if num_search == 1:
        for i in ngrams:
            for key in PEOPLE:
                if i in PEOPLE[key].adress:
                    result.append(PEOPLE[key])
                    counter +=1
            if counter != 0:
                break
    if num_search == 2:
        for i in ngrams:
            for key in PEOPLE:
                if i in PEOPLE[key].yearbirth:
                    result.append(PEOPLE[key])
                    counter +=1
            if counter != 0:
                break
    if num_search == 3:
        for i in ngrams:
            for key in PEOPLE:
                if i in PEOPLE[key].hight:
                    result.append(PEOPLE[key])
                    counter +=1
            if counter != 0:
                break
    if num_search == 4:
        for i in ngrams:
            for key in PEOPLE:
                if i in PEOPLE[key].weight:
                    result.append(PEOPLE[key])
                    counter +=1
            if counter != 0:
                break
    if num_search == 5:
        for i in ngrams:
            for key in PEOPLE:
                if i in PEOPLE[key].colorhair:
                    result.append(PEOPLE[key])
                    counter +=1
            if counter != 0:
                break
    if num_search == 6:
        for i in ngrams:
            for key in PEOPLE:
                if i in PEOPLE[key].coloreyes:
                    result.append(PEOPLE[key])
                    counter +=1
            if counter != 0:
                break
    if counter == 0:
        result = "Персонаж не найден"      
    return result

