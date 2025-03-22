# Ввод пользователя или Меню
CREATE: str = "1"
VIEW: str = "2"
UPDATE: str = "3"
DELETE: str = "4"
EXIT: str = "0"

# Приоритеты
HIGH: str = "1"
MEDIUM: str = "2"
LOW: str = "3"

PRIORITY_TASK: dict[str, str] = {
    "высокий": HIGH,
    "средний": MEDIUM,
    "низкий": LOW
}

# Статусы
NEW: str = "1"
IN_PROGRESS: str = "2"
COMPLETED: str = "3"

STATUS_TASK: dict[str, str] = {
    "новая": NEW,
    "в процессе": IN_PROGRESS,
    "завершена": COMPLETED
}

# Просмотр задач
ORIGINAL: str = "1"
BY_STATUS: str = "2"
BY_PRIORITY: str = "3"
SEARCH: str = "4"

VIEW_TASK: dict[str, str] = {
    ORIGINAL: "задачи в изначальном виде",
    BY_STATUS: "отсортированы по статусу",
    BY_PRIORITY: "отсортированы по приоритету",
}

# Обновление поля
NAME: str = "1"
DESCRIPTION: str = "2"
PRIORITY: str = "3"
STATUS: str = "4"

UPDATE_TASK: dict[str, str] = {
    NAME: "название",
    DESCRIPTION: "описание",
    PRIORITY: "приоритет",
    STATUS: "статус",
    SEARCH: "поиск"
}

FILE_TASKS = "tasks.txt"

# Типизация для задач
Task = dict[str, str]
Tasks = dict[int, Task]

# Чтение задач из файла
def read_file() -> Tasks:
    tasks: Tasks = {}
    try:
        with open(FILE_TASKS, "r") as file:
            for line in file:
                part_of_task: list[str] = line.strip().split("|")
                if len(part_of_task) == 5:
                    task_id: int = int(part_of_task[0])
                    tasks[task_id] = {
                        "Название": part_of_task[1],
                        "описание": part_of_task[2],
                        "приоритет": part_of_task[3],
                        "статус": part_of_task[4]
                    }
    except FileNotFoundError:
        print("Файл с задачами не найден. Создан новый файл.")
    return tasks

# Сохранение задач в файл
def save_file(tasks:Tasks) -> None:
    with open(FILE_TASKS, "w") as file:
        for task_id, task in tasks.items():
            line: str = f"{task_id}|{task['Название']}|{task['описание']}|{task['приоритет']}|{task['статус']}"
            file.write(line + "\n")

# Создание новой задачи
def create_task() -> None:
    tasks: Tasks = read_file()

    # Максимальный существующий task_id
    if tasks:
        task_id: int = max(tasks.keys()) + 1
    else:
        task_id = 1

    title: str = input("Введите название задачи: ").strip()
    while not title:
        print("Название не может быть пустым!")
        title = input("Введите название задачи: ").strip()

    description: str = input("Введите краткое описание задачи: ").strip()
    while not description:
        description = input("Введите краткое описание задачи: ").strip()

    priority: str = input("Введите приоритет задачи: \nВысокий = 1 \nСредний = 2 \nНизкий = 3 ").strip()
    while priority not in PRIORITY_TASK.values():
        print("Некорректный приоритет! Попробуйте снова.")
        priority = input("Введите приоритет задачи: \nВысокий = 1 \nСредний = 2 \nНизкий = 3 ").strip()

    status: str = input("Введите статус задачи: \nНовая = 1 \nВ процессе = 2 \nЗавершена = 3 ").strip()
    while status not in STATUS_TASK.values():
        print("Некорректный статус! Попробуйте снова.")
        status = input("Введите статус задачи: \nНовая = 1 \nВ процессе = 2 \nЗавершена = 3 ").strip()

    tasks[task_id] = {
        "Название": title,
        "описание": description,
        "приоритет": priority,
        "статус": status
    }

    save_file(tasks)
    print(f"Задача {task_id} '{title}' {description} была создана. Приоритет: {priority}, статус: {status}")

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

    user_update: str = input("Введите ID задачи, которую хотите обновить: ").strip()

    if not user_update.isdigit() or int(user_update) not in tasks:
        print("Такой задачи не существует.")
        return

    task_id: int = int(user_update)

    user_update_choice: str = input("Укажите, какое поле хотите обновить: \n1 - название \n2 - описание \n3 - приоритет \n4 - статус\n").strip()

    if user_update_choice == NAME:
        user_title = input("Введите новое название задачи: ").strip()
        tasks[task_id]["Название"] = user_title
        print(f"Название задачи {task_id} обновлено на '{user_title}'")

    elif user_update_choice == DESCRIPTION:
        user_description: str = input("Введите новое описание задачи: ").strip()
        tasks[task_id]["описание"] = user_description
        print(f"Описание задачи {task_id} обновлено на '{user_description}'")

    elif user_update_choice == PRIORITY:
        user_priority: str = input("Введите новый приоритет для задачи: \nВысокий = 1 \nСредний = 2 \nНизкий = 3\n").strip()
        if user_priority in PRIORITY_TASK.values():
            tasks[task_id]["приоритет"] = user_priority
            print(f"Приоритет задачи {task_id} изменен на {user_priority}")
        else:
            print("Некорректный приоритет")
            return

    elif user_update_choice == STATUS:
        user_status: str = input("Введите новый статус: \nНовая = 1 \nВ процессе = 2 \nЗавершена = 3\n").strip()
        if user_status in STATUS_TASK.values():
            tasks[task_id]["статус"] = user_status
            print(f"Статус задачи {task_id} изменен на {user_status}")
        else:
            print("Некорректный статус")
            return
    else:
        print("Некорректный ввод.")
        return

    save_file(tasks)

# Удаление задачи
def delete_tasks() -> None:
    tasks: Tasks = read_file()
    user_delete: str = input("Введите ID задачи, которую хотите удалить: ").strip()

    if not user_delete.isdigit() or int(user_delete) not in tasks:
        print("Такой задачи не существует.")
        return

    task_id: int = int(user_delete)

    del tasks[task_id]

    save_file(tasks)
    print(f"Задача с ID {task_id} была удалена")

# Главное меню
def menu() -> None:
    while True:
        user_input: str = input("\nВведите цифру для желаемого действия:\n1 - Создать новую задачу \n2 - Просмотреть задачи \n3 - Обновить задачу \n4 - Удалить задачу \n0 - Выйти из программы\n").strip()

        if user_input == CREATE:
            create_task()

        elif user_input == VIEW:
            view_tasks()

        elif user_input == UPDATE:
            update_tasks()

        elif user_input == DELETE:
            delete_tasks()

        elif user_input == EXIT:
            print("Выход")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")

# Запуск программы
menu()