
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты:
# описание задачи,
# срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач,
# вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True


class TaskManager:
    def __init__(self):
        self.tasks_list = []

    def add_task (self, description, due_date):
        new_task = Task (description, due_date)
        self.tasks_list.append (new_task)

    def completed_task (self, task_index):
        if 0 <= task_index < len (self.tasks_list):
            self.tasks_list [task_index].mark_as_completed()
        else:
            print ("Задача с таким индексом не найдена!")

    def show_current_tasks (self):
        print("Текущие задачи:")
        for index, task in enumerate (self.tasks_list):
            if not task.is_completed:
                print(f"Задача {index+1}. {task.description}, cрок {task.due_date}.")

task_manager = TaskManager()

task_manager.add_task("Изучить урок 1","2024.08.19")
task_manager.add_task("Изучить урок 2","2024.08.20")
task_manager.add_task("Изучить урок 3","2024.08.21")
task_manager.add_task("Изучить урок 4","2024.08.22")
task_manager.add_task("Изучить урок 5","2024.08.23")

task_manager.show_current_tasks()

num_completed_task = int(input ("Введите номер выполненной задачи :"))
task_manager.completed_task(num_completed_task - 1)

task_manager.show_current_tasks()
