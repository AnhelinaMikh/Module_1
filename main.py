# main.py
from utils import create_task, view_tasks, update_tasks, delete_tasks
from config import CREATE, VIEW, UPDATE, DELETE, EXIT

def menu() -> None:
    while True:
        user_input = input("\n1 - Создать задачу\n2 - Просмотреть задачи\n3 - Обновить задачу\n4 - Удалить задачу\n0 - Выход\nВаш выбор: ").strip()

        if user_input == CREATE:
            create_task()
        elif user_input == VIEW:
            view_tasks()
        elif user_input == UPDATE:
            update_tasks()
        elif user_input == DELETE:
            delete_tasks()
        elif user_input == EXIT:
            print("Выход.")
            break
        else:
            print("Некорректный ввод.")

# Запуск программы
if __name__ == "__main__":
    menu()
