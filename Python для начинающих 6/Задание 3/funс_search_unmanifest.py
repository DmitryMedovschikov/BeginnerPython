#функция выполняет поиск по словарю персонажей неявным способом в зависимости от введенных пользователем данных
#и возвращает результат в виде списка персонажей, сответствующих кретериям поиска
def funс_search_unmanifest (people, num_search, search):
    result = []                                     #инициализация пустого списка в который будут занесены объекты, соотвествующие критериям поиска
    counter = 0                                     #инициализация счетчика для определения найден ли хоть один соотвествующий критериям поиска персонаж
    ngrams = [
        search[i:i+2] for i in range(len(search))
        ]                                           #инициализация списка двуграм путем среза производимого над строкой (введенными пользователем данными для поиска)
    if num_search == 0:                             #определение поля по которому будет выполнен поиск
        for i in ngrams:                            #перебор получившегося списка двуграмм
            for key in people:                      #для каждой двуграммы перебор списка объектов (персонажей)
                if i in people[key].surname:        #если найдена двуграмма в соответствующем поле 
                    result.append(people[key])      #информация об объекте добавляется в конец списка (результат поиска)
                    counter +=1                     #счетчик увеличивается на 1 при каждом совпадении
            if counter != 0:                        #если, перебрав все двуграммы, не найдено ни одного подходящего критериям поиска объекта
                break                               #выполянется выход из цикла и функции с соответствующим сообщением
    if num_search == 1:
        for i in ngrams:
            for key in people:
                if i in people[key].adress:
                    result.append(people[key])
                    counter +=1
            if counter != 0:
                break
    if num_search == 2:
        for i in ngrams:
            for key in people:
                if i in people[key].yearbirth:
                    result.append(people[key])
                    counter +=1
            if counter != 0:
                break
    if num_search == 3:
        for i in ngrams:
            for key in people:
                if i in people[key].hight:
                    result.append(people[key])
                    counter +=1
            if counter != 0:
                break
    if num_search == 4:
        for i in ngrams:
            for key in people:
                if i in people[key].weight:
                    result.append(people[key])
                    counter +=1
            if counter != 0:
                break
    if num_search == 5:
        for i in ngrams:
            for key in people:
                if i in people[key].colorhair:
                    result.append(people[key])
                    counter +=1
            if counter != 0:
                break
    if num_search == 6:
        for i in ngrams:
            for key in people:
                if i in people[key].coloreyes:
                    result.append(people[key])
                    counter +=1
            if counter != 0:
                break
    if counter == 0:
        result = "Персонаж не найден"
        
    return result

