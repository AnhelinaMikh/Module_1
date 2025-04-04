# config.py

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

# Файл для хранения задач
FILE_TASKS = "tasks.txt"

# Типизация для задач
Task = dict[str, str]
Tasks = dict[int, Task]
