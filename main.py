import os
import datetime

#Проверка на наличие файла в папке Catalogs
def check_file_in_Catalogs(filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    catalogs_directory = os.path.join(current_directory, "Catalogs")
    full_file_path = os.path.join(catalogs_directory, filename  + ".txt")
    return os.path.isfile(full_file_path)

#Создание каталога пользователем
def create_catalog():
    while True:
        title = input("Введите название для вашего каталога: ")

        if not check_file_in_Catalogs(title):
            #Нахождение нынешней даты
            now = datetime.datetime.now()
            date_string = now.strftime("%d.%m.%Y")

            #Определяет где находится main.py; находит путь к папке Catalogs; создает полный путь к файлу из папки Catalogs
            current_dir = os.path.dirname(os.path.abspath(__file__))
            catalogs_path = os.path.join(current_dir, "Catalogs")
            filepath = os.path.join(catalogs_path, f"{title}.txt")

            #Создание файла, запись количества рецептов в нём, запись даты создания
            file = open(filepath, "w", encoding="utf-8")
            file.write(f"Кол-во рецептов в каталоге: 0\nДата создания: {date_string}\n{"-" * 20 + "\n"}")
            file.close()

            print(f"Каталог с названием «{title}» успешно создан!")

            break
        else:
            print(f"Каталог с названием «{title}» уже существует, попробуйте ещё раз.")

#Удаление каталога пользователем
def remove_catalog():
    while True:
        title = input("Введите название каталога, которое хотите удалить: ")
        
        if check_file_in_Catalogs(title):
            answer = input(f"Каталог «{title}» найден, вы уверены, что хотите его удалить? (Y/N): ")

            if answer.lower() == "y":
                current_dir = os.path.dirname(os.path.abspath(__file__))
                catalogs_path = os.path.join(current_dir, "Catalogs")
                filepath = os.path.join(catalogs_path, f"{title}.txt")

                os.remove(filepath)
                print(f"Данный каталог успешно удалён.")
                break

            elif answer.lower() == "n":
                print("Удаление каталога отменено.")
                break

            else:
                print("Некорректный ввод. Пожалуйста, введите 'Y' или 'N'.")

        else:
            print(f"Каталог с названием «{title}» не найден.")

#Получение списка всех каталогов
def list_of_all_catalogs():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalogs_path = os.path.join(current_dir, "Catalogs")
    files = os.listdir(catalogs_path)

    #Фильтрует список, оставляя только файлы с расширением .txt"
    all_catalogs = [
        filename[:-4] #Удаляет расширение .txt
        for filename in files
        if filename.endswith(".txt")
    ]

    print("Список всех каталогов: " + ", ".join(all_catalogs), end=".\n")

#Добавления рецепта в каталог
def add_recipe():
    required_catalog = input("Введите каталог, в который вы хотите записать рецепт: ")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalogs_path = os.path.join(current_dir, "Catalogs")
    file_path = os.path.join(catalogs_path, f"{required_catalog}.txt")
    files = os.listdir(catalogs_path)

    file_found = False

    all_catalogs = [
        filename[:-4]
        for filename in files
        if filename.endswith(".txt")
    ]

    for catalog in all_catalogs:
        if catalog == required_catalog:
            file_found = True
            break
        
    if file_found == True:
        recipe_title = input("Введите название для рецепта: ")
        ingredients = input("Введите ингредиенты (через запятую): ")
        manual = input("Введите инструкцию приготовления: ")

        catalog = open(file_path, "a", encoding="utf-8")
        catalog.write(f"Название: {recipe_title}\n")
        catalog.write(f"Ингредиенты: {ingredients}\n")
        catalog.write(f"Инструкция: {manual}\n")
        catalog.write("-" * 20 + "\n") #Разделитель между рецептами
        catalog.close()

        catalog = open(file_path, "r+", encoding="utf-8")
        first_line = catalog.readline().strip()

        number_string = first_line.replace("Кол-во рецептов в каталоге:", "").strip() #Удаляет текст и пробелы

        recipe_count = int(number_string)
        recipe_count += 1
        catalog.seek(0)
        catalog.write(f"Кол-во рецептов в каталоге: {recipe_count}\n") #Перезаписывает строчку с новым числом
        catalog.close()

        print("Рецепт успешно записан!")
    else:
        print(f"К сожалению, каталог с названием «{required_catalog}» не был найден.")

#Вывод на экран всех рецептов в выбранном каталоге
def print_all_recipes_in_catalog():
    catalog_name = input("Введите название каталога, рецепты которого хотите посмотреть: ")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalogs_path = os.path.join(current_dir, "Catalogs")
    filepath = os.path.join(catalogs_path, f"{catalog_name}.txt")

    catalog = open(filepath, "r", encoding="utf-8")
    content = catalog.read()
    print("-" * 20)
    print(content)
    catalog.close()

#Поиск рецепта по его наименованию
def find_recipe():
    need_recipe = input("Введите название рецепта для его поиска: ")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalogs_path = os.path.join(current_dir, "Catalogs")

    recipe_found = False

    for filename in os.listdir(catalogs_path):
        filepath = os.path.join(catalogs_path, filename)

        catalog = open(filepath, "r", encoding="utf-8")

        for line in catalog:
            if line.startswith("Название:") and need_recipe.lower() in line.lower():
                catalog_name = filename[:-4]
                print(f"Рецепт найден в каталоге: {catalog_name}")
                recipe_found = True
                break 

        catalog.close()

    if recipe_found == False:
        print(f"Рецепт с названием «{need_recipe}» не найден ни в одном каталоге.")

#Удаление рецепта
def delete_recipe():
    catalog_name = input("Введите название каталога, из которого нужно удалить рецепт: ")
    recipe_to_delete = input("Введите название рецепта, который нужно удалить: ")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalogs_path = os.path.join(current_dir, "Catalogs")
    filepath = os.path.join(catalogs_path, f"{catalog_name}.txt")

    catalog = open(filepath, "r", encoding="utf-8")
    content = catalog.read()
    catalog.close()

    recipes = content.split("-" * 20 + "\n")

    updated_recipes = []
    recipe_deleted = False

    for recipe in recipes:
        if recipe.strip():
            if "Название:" in recipe:
                recipe_name = recipe.split("Название:")[1].split("\n")[0].strip()
                
                if recipe_name.lower() == recipe_to_delete.lower():
                    print(f"Рецепт «{recipe_to_delete}» удален из каталога «{catalog_name}».")
                    recipe_deleted = True
                    continue

            updated_recipes.append(recipe + "-" * 20 + "\n")

    if not recipe_deleted:
        print(f"Рецепт с названием «{recipe_to_delete}» не найден в каталоге «{catalog_name}».")
        return

    catalog = open(filepath, "w", encoding="utf-8")

    #Перезапись кол-во рецептов
    first_line = f"Кол-во рецептов в каталоге: {len(updated_recipes) - 1}\n"
    catalog.write(first_line)

    #Запись даты
    second_line = f"Дата создания: 06.04.2025\n"
    catalog.write(second_line)

    catalog.write("-" * 20 + "\n")

    #Запись всего остального
    for recipe in updated_recipes[1:]:
        catalog.write(recipe)

    catalog.close()

#Редактирование рецепта
def edit_recipe():
    catalog_name = input("Введите название каталога, в котором находится рецепт: ")
    recipe_to_edit = input("Введите название рецепта, который нужно отредактировать: ")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalogs_path = os.path.join(current_dir, "Catalogs")
    filepath = os.path.join(catalogs_path, f"{catalog_name}.txt")

    if not os.path.exists(filepath):
        print(f"Каталог «{catalog_name}» не найден.")
        return

    catalog = open(filepath, "r", encoding="utf-8")
    lines = catalog.readlines()
    catalog.close()

    recipe_edited = False
    updated_recipes = []

    #Сохраняет первые две строки
    updated_recipes.append(lines[0])
    updated_recipes.append(lines[1])

    i = 2

    while i < len(lines):
        if lines[i].strip() == "--------------------":
            updated_recipes.append(lines[i])
            i += 1
            continue

        if "Название:" in lines[i]:
            recipe_name = lines[i].split("Название:")[1].strip()

            if recipe_name.lower() == recipe_to_edit.lower():
                print(f"Редактирование рецепта «{recipe_to_edit}»:")

                new_name = input("Введите новое название рецепта (или нажмите Enter, чтобы оставить прежним): ")
                new_ingredients = input("Введите новые ингредиенты (или нажмите Enter, чтобы оставить прежним): ")
                new_instructions = input("Введите новые инструкции (или нажмите Enter, чтобы оставить прежним): ")

                #Получает старые значения из файла
                old_ingredients = ""
                old_instructions = ""

                if i + 1 < len(lines) and "Ингредиенты:" in lines[i+1]:
                    old_ingredients = lines[i+1].split("Ингредиенты:")[1].strip()
                if i + 2 < len(lines) and "Инструкция:" in lines[i+2]:
                    old_instructions = lines[i+2].split("Инструкция:")[1].strip()

                #Сохраняет новые или старые значения
                name = new_name if new_name else recipe_name
                ingredients = new_ingredients if new_ingredients else old_ingredients
                instructions = new_instructions if new_instructions else old_instructions

                #Формирует отредактированный рецепт
                edited_recipe = f"Название: {name}\nИнгредиенты: {ingredients}\nИнструкция: {instructions}\n"
                updated_recipes.append(edited_recipe)
                recipe_edited = True

                print("Рецепт успешно отредактирован!")

                i += 3
                continue

        #Сохраняет остальные строки
        updated_recipes.append(lines[i])
        i += 1

    if recipe_edited == False:
        print(f"Рецепт с названием «{recipe_to_edit}» не найден в каталоге «{catalog_name}».")

    catalog = open(filepath, "w", encoding="utf-8")

    #Считает кол-во рецептов
    recipe_count = 0
    for line in updated_recipes:
        if "Название:" in line:
            recipe_count += 1

    catalog.write(f"Кол-во рецептов в каталоге: {recipe_count}\n")
    catalog.write(f"Дата создания: 06.04.2025\n")

    #Записывает рецепты
    for line in updated_recipes[2:]:
        catalog.write(line)

    catalog.close()

#Связывание всех функций в одно приложение
print("┌────────────────────────────────────────────────────────┐")
print("| Консольное приложение для хранения кулинарных рецептов |")
print("└────────────────────────────────────────────────────────┘")
print("Для просмотра команд введите \"help\".")

exit = False

while exit != True:
    action = input("> ")

    if action == "help":
        print("(1) create - Создание каталога, в который вы можете записать свои рецепты.")
        print("(2) remove - Удаление выбранного вами каталога.")
        print("(3)  list  - Вывод на экран всех существующих каталогов.")
        print("(4)  add   - Добавление вашего рецепта в каталог.")
        print("(5) delete - Удаление выбранного вами рецепта из каталога.")
        print("(6)  read  - Чтение рецептов в выбранном каталоге.")
        print("(7)  find  - Нахождение каталога, в котором находится рецепт.")
        print("(8)  edit  - Редактирование рецепта из каталога.")
        print("(9)  exit  - Завершение работы приложения.")
        print("(10) help  - Помощь с командами.")

    elif action == "create":
        create_catalog()

    elif action == "remove":
        remove_catalog()

    elif action == "list":
        list_of_all_catalogs()
    
    elif action == "add":
        add_recipe()

    elif action == "delete":
        delete_recipe()

    elif action == "read":
        print_all_recipes_in_catalog()

    elif action == "find":
        find_recipe()

    elif action == "edit":
        edit_recipe()

    elif action == "exit":
        print("Приложение завершило свою работу.")
        exit = True
        break

    else:
        print("Ошибка. Данной команды не существует.")