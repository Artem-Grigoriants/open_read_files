def read_cook_book(filename): #Функция read_cook_book принимает имя файла и открывает его для чтения.
    with open(filename, encoding='utf-8') as file:
        cook_book = {} #создается пустой словарь cook_book
        while True: #цикл while True для чтения данных из файла построчно
            dishes = file.readline().strip()
            if not dishes: #Если нет содержимого цикл останавливает свою работу
                break
            ingredient_count = int(file.readline().strip()) #Количество ингридиентов в блюде
            ingredients = [] #Создается пустой список для добавления ингридиентов
            for _ in range(ingredient_count): #Цикл для чтения название блюд и количество ингредиентов.
                ingredient_data = file.readline().strip().split(" | ")
                ingredient_name = ingredient_data[0]
                quantity = int(ingredient_data[1])
                measure = ingredient_data[2]
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            cook_book[dishes] = ingredients
            file.readline()
        return cook_book

# Запуск функции и вывод на печать
cook_book = read_cook_book("dishes.txt")
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count): #Функция get_shop_list_by_dishes принимает список блюд dishes и количество персон person_count
    shop_list = {} #В функции get_shop_list_by_dishes создается пустой словарь shop_list
    for dish in dishes:
        if dish in cook_book: #Проверка наличия рецептов
            for ingredient in cook_book[dish]: #Цикл сопоставления и расчета необходимого кол-ва ингридиентов
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if name in shop_list: #работа с совпадающими именами ингридиентов
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list

# Запуск функции и вывод на печать
cook_book = read_cook_book("dishes.txt")
shopping_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shopping_list)

