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

            #Определяет где находится main.py; находит путь к папке Catalogs; создает полный путь к файлу внутри Catalogs
            current_dir = os.path.dirname(os.path.abspath(__file__))
            catalogs_path = os.path.join(current_dir, "Catalogs")
            filepath = os.path.join(catalogs_path, f"{title}.txt")

            #Создание файла, запись количества рецептов в нём, запись даты создания
            file = open(filepath, "w", encoding="utf-8")
            file.write(f"0\n{date_string}")
            file.close()

            print(f"Каталог с названием «{title}» успешно создан!")

            break
        else:
            print(f"Каталог с названием {title} уже существует, попробуйте ещё раз.")

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

create_catalog()
remove_catalog()