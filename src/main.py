from tasks.task import Task
from tasks.task_list import TaskList
from archive import Archive
import datetime

archive = Archive()
task_list = TaskList()
filtered_tasks = task_list



task1 = Task('asdasdasd', datetime.date(2021,5,5), 5, 'a')


task_list.add_task(task1)
task_list.add_task(Task('asdaksjdaudgas', category='a', priority=7))
task_list.add_task(Task('salamudgas', category='b', priority=1))

print(task_list)

task_list.edit_task(0, 'asdajbkfbaffffifuuuufufuj', new_priority=9)

# print(task_list)

# task_list.delete_task(0)

print(task_list)

task_list.task_completed(0)

archive.print_archive()
print(archive)

# print(task_list.filter_tasks('b'))
