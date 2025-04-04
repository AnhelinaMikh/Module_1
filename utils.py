# utils.py
from config import *
from files import read_file, save_file

# Создание новой задачи
def create_task() -> None:
    tasks: Tasks = read_file()

    task_id = max(tasks.keys(), default=0) + 1

    title = input("Введите название задачи: ").strip()
    while not title:
        title = input("Название не может быть пустым! Введите заново: ").strip()

    description = input("Введите краткое описание задачи: ").strip()
    while not description:
        description = input("Описание не может быть пустым! Введите заново: ").strip()

    priority = input("Приоритет задачи (1 - Высокий, 2 - Средний, 3 - Низкий): ").strip()
    while priority not in PRIORITY_TASK.values():
        priority = input("Некорректный приоритет. Введите снова: ").strip()

    status = input("Статус задачи (1 - Новая, 2 - В процессе, 3 - Завершена): ").strip()
    while status not in STATUS_TASK.values():
        status = input("Некорректный статус. Введите снова: ").strip()

    tasks[task_id] = {
        "Название": title,
        "описание": description,
        "приоритет": priority,
        "статус": status
    }

    save_file(tasks)
    print(f"Задача {task_id} создана!")

# Просмотр задач
# Функция просмотра задач
def view_tasks() -> None:
    tasks: Tasks = read_file()

    if not tasks:
        print("Нет задач.\n")
        return

    view_user_choice: str = input("Выберите вариант просмотра задач: \n1 - В изначальном виде \n2 - По статусу \n3 - По приоритету \n4 - Поиск по названию\n").strip()

    if view_user_choice == ORIGINAL:
        for key, value in tasks.items():
            print(f"{key}: {value}")

    elif view_user_choice == BY_STATUS:
        sorted_tasks_status: list[tuple[int, Task]] = sorted(tasks.items(), key=lambda x: int(x[1]["статус"]))
        for task in sorted_tasks_status:
            status_name = {NEW: "новая", IN_PROGRESS: "в процессе", COMPLETED: "завершена"}[task[1]["статус"]]
            print(f"{task[0]}: {task[1]['Название']} - {task[1]['описание']} - Статус: {status_name}")

    elif view_user_choice == BY_PRIORITY:
        sorted_tasks_priority: list[tuple[int, Task]] = sorted(tasks.items(), key=lambda x: int(x[1]["приоритет"]))
        for task in sorted_tasks_priority:
            priority_name: str = {HIGH: "высокий", MEDIUM: "средний", LOW: "низкий"}[task[1]["приоритет"]]
            print(f"{task[0]}: {task[1]['Название']} - {task[1]['описание']} - Приоритет: {priority_name}")
    elif view_user_choice == SEARCH:
        user_word: str = input("Введите ключевое слово для поиска: ").strip().lower()

        search_results:Tasks = {}

        for x, y in tasks.items():
            title: str = y["Название"].lower()
            description: str = y["описание"].lower()

            if user_word in title or user_word in description:
                search_results[x] = y
                print(f"{x}: {y}")

        if not search_results:
            print("Задачи не найдены.")

    save_file(tasks)

# Обновление задачи
def update_tasks() -> None:
    tasks: Tasks = read_file()
    task_id = input("Введите ID задачи для обновления: ").strip()

    if not task_id.isdigit() or int(task_id) not in tasks:
        print("Задача не найдена.")
        return

    task_id = int(task_id)
    field = input("Что обновить? (1 - Название, 2 - Описание, 3 - Приоритет, 4 - Статус): ").strip()

    if field == NAME:
        tasks[task_id]["Название"] = input("Введите новое название: ").strip()
    elif field == DESCRIPTION:
        tasks[task_id]["описание"] = input("Введите новое описание: ").strip()
    elif field == PRIORITY:
        tasks[task_id]["приоритет"] = input("Введите новый приоритет: ").strip()
    elif field == STATUS:
        tasks[task_id]["статус"] = input("Введите новый статус: ").strip()
    else:
        print("Некорректный ввод.")
        return

    save_file(tasks)
    print("Задача обновлена!")

# Удаление задачи
def delete_tasks() -> None:
    tasks: Tasks = read_file()
    task_id = input("Введите ID задачи для удаления: ").strip()

    if not task_id.isdigit() or int(task_id) not in tasks:
        print("Задача не найдена.")
        return

    del tasks[int(task_id)]
    save_file(tasks)
    print("Задача удалена!")
