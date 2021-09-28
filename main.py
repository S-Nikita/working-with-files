import os
# ---
# Была ошибка с кодировкой при чтении файла, нашел решение в интеренете
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
# ---


# Задание №1 Создание словаря с рецптами
def read_data():
    # В условиях попросили не создавать глобальных переменных, поэтому внутри функции так много переменных
    file_name = 'recipes.txt'
    path = f'{os.getcwd()}/cookbook/{file_name}'
    mode = 'r'
    encoding = 'utf-8'
    cook_book = {}
    with open(path, mode=mode, encoding=encoding) as file:
        for line in file:
            items_list = []
            recipe_name = line.strip()
            count = int(file.readline())
            for i in range(count):
                ingridient_data = file.readline().strip().split('|')
                items_list.append(
                    {'ingredient_name': ingridient_data[0], 'quantity': int(ingridient_data[1]), 'measure': ingridient_data[2]})
            cook_book[recipe_name] = items_list

            file.readline()

    return cook_book


# Задание №2 Рассчет ингридиентов на количество персон
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_data()
    shop_list = {}
    for meal in dishes:
        if meal in cook_book.keys():
            for i in range(len(cook_book[meal])):
                ingridient_data = cook_book[meal][i]
                ingridient = ingridient_data['ingredient_name']
                quantity = int(
                    ingridient_data['quantity']) * person_count * dishes.count(meal)
                measure = ingridient_data['measure']

                shop_list[ingridient] = {
                    'measure': measure,
                    'quantity': quantity
                }

    print(shop_list)


get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет', 'Запеченный картофель'], 2)


# Задание №3 Составление файла
# Функция сортировки листа с файлами в зависимости от количества строк в каждом файле
def sort_files_info_list(unsorted_list):
    sorted_list = []
    while unsorted_list:
        min_rows = unsorted_list[0]['rows']
        smallest_text = unsorted_list[0]
        for file_info in unsorted_list:
            if file_info['rows'] < min_rows:
                min_rows = file_info['rows']
                smallest_text = file_info
        sorted_list.append(smallest_text)
        unsorted_list.remove(smallest_text)
    return sorted_list


# Функция чтения файлов
def read_files():
    # Получение списка всех файлов в заданной директории
    path = f'{os.getcwd()}/sorted'
    files = os.listdir(path)
    # Присваивание параметров для чтения файлов
    mode = 'r'
    encoding = 'utf-8'
    # Получение информации по каждому из файлов
    files_info = []
    for file_name in files:
        file_path = f'{path}/{file_name}'
        with open(file_path, mode=mode, encoding=encoding) as file:
            count = len(file.readlines())
            file.seek(0)  # возврат курсора в самое начало текущего файла
            data = file.read()
            files_info.append(
                {
                    'file_name': file_name,
                    'rows': count,
                    'text': data
                }
            )
    return files_info


# Функция записи информации по каждому из файлов в один общий файл в отсортированном порядке
def write_data(sorted_list):
    mode = 'w'
    encoding = 'utf-8'
    sorted_file_name = 'sorted.txt'
    with open(sorted_file_name, mode=mode, encoding=encoding) as file:
        for file_info in sorted_list:
            file_name = file_info['file_name']
            rows = str(file_info['rows'])
            text = file_info['text']
            file.write(file_name + '\n' + rows + '\n' + text)


# Функция создания файла хранящего информацию из нескольких файлов в отсортированном виде
def create_sorted_file():
    files_info = read_files()
    sorted_list = sort_files_info_list(files_info)
    write_data(sorted_list)


create_sorted_file()
