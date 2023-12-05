from tasks.task import Task
from tasks.task_list import TaskList
from tasks.subtask import Subtask
import datetime

archive = TaskList().archive
task_list = TaskList()




task1 = Task('asdasdasd', datetime.date(2021,5,5), 5, 'a')


task_list.add_task(task1)
task_list.add_task(Task('asdaksjdaudgas', category='a', priority=7))
task_list.add_task(Task('salamudgas', category='b', priority=1))

# print(task_list)
task_list.edit_task(0, 'asdajbkfbaffffifuuuufufuj', new_priority=9)

# print(task_list)

# task_list.delete_task(0)

print(task_list)

task_list.task_completed(0)

print(task_list)


print(task_list.archive_show())

# print(task_list.filter_tasks('b'))
