import  os

# file_names = os.path.join(os.getcwd(),'sorted')
# print(file_names)

def read_and_sort(file_names): #функция принимает список имен файлов, читает их содержимое и возвращает список
    files_data = [] #Пустой список
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file: #открывает файл только для чтения
            lines = file.readlines()
            files_data.append((file_name, len(lines), lines)) #Создаются кортежи ('1.txt', 2, ['Строка 1 в файле 1\n', 'Строка 2 в файле 1\n']),
    return sorted(files_data, key=lambda x: x[1]) #функция возвращает кортеж с отсортированными кортежами по кол-ву строк

def merge_to_result(file_names, result_file): #функция принимает список имен файлов и имя результирующего файла
    sorted_files = read_and_sort(file_names)
    with open(result_file, 'w', encoding='utf-8') as result: #открытие файла в режиме открыт для записи
        for file_name, line_count, lines in sorted_files: #цикл записи строк в новый файл
            result.write(f"{file_name}\n{line_count}\n")
            for line in lines:
                result.write(line)
            result.write("\n")

# Запуск функций
a1 = os.path.join(os.getcwd(), '1.txt') # Как я не пытался я не смог переписать код таким образом что бы Task3_File
a2 = os.path.join(os.getcwd(), '2.txt')  # работал бы не находясь вместе с файлами 1,2,3 в папке sorted
a3 = os.path.join(os.getcwd(), '3.txt')
a4 = os.path.join(os.getcwd(), 'result.txt')
# a5 = real_path = os.path.realpath('result.txt')

file_names = [a1 , a2, a3]
result_file = a4
merge_to_result(file_names, result_file)
print(a1)