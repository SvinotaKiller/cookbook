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

    print("Список всех каталогов: " + ", ".join(all_catalogs), end=".")

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

create_catalog()
add_recipe()