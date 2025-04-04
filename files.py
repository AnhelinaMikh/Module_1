# files.py
from config import FILE_TASKS, Tasks

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
def save_file(tasks: Tasks) -> None:
    with open(FILE_TASKS, "w") as file:
        for task_id, task in tasks.items():
            line: str = f"{task_id}|{task['Название']}|{task['описание']}|{task['приоритет']}|{task['статус']}"
            file.write(line + "\n")
