from tasks.task import Task
from tasks.task_list import TaskList
import datetime


task_list = TaskList()
filtered_tasks = task_list



task1 = Task('asdasdasd', datetime.date(2021,5,5), 5, 'a')


task_list.add_task(task1)
task_list.add_task(Task('asdaksjdaudgas', category='a'))
task_list.add_task(Task('salamudgas', category='b'))

# print(task_list)

# task_list.edit_task(0, 'asdajbkfbaffffifuuuufufuj')

# print(task_list)

# task_list.delete_task(0)

print(task_list)



print(filtered_tasks.filter_tasks('b'))
