def read_cook_book(filename):
    with open(filename, encoding='utf-8') as file:
        cook_book = {}
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_data = file.readline().strip().split(" | ")
                ingredient_name = ingredient_data[0]
                quantity = int(ingredient_data[1])
                measure = ingredient_data[2]
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            file.readline()  # Skip the separator line (---)
        return cook_book

# Пример использования
cook_book = read_cook_book("dishes.txt")
print(cook_book)