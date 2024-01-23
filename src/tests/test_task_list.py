import unittest
from tasks.task import Task
from tasks.task_list import TaskList

class TestTaskList(unittest.TestCase):

    def setUp(self):
        self.task_list = TaskList()

    def test_add_task(self):
        task = Task("Test Task", "2023-01-01", 1, "Testing")
        self.task_list.add_task(task)
        self.assertEqual(len(self.task_list.tasks), 1)

    def test_edit_task(self):
        task = Task("Test Task", "2023-01-01", 1, "Testing")
        self.task_list.add_task(task)

        self.task_list.edit_task(1, "Edited Task", "2023-02-02", 2, "Updated")
        edited_task = self.task_list.tasks[0]

        self.assertEqual(edited_task.title, "Edited Task")
        self.assertEqual(edited_task.due_date, "2023-02-02")
        self.assertEqual(edited_task.priority, 2)
        self.assertEqual(edited_task.category, "Updated")

    def test_delete_task(self):
        task = Task("Test Task", "2023-01-01", 1, "Testing")
        self.task_list.add_task(task)

        self.task_list.delete_task(1)
        self.assertEqual(len(self.task_list.tasks), 0)

    def test_filter_tasks(self):
        task1 = Task("Task 1", "2023-01-01", 1, "Category1")
        task2 = Task("Task 2", "2023-01-02", 2, "Category2")
        task3 = Task("Task 3", "2023-01-03", 3, "Category1")

        self.task_list.add_task(task1)
        self.task_list.add_task(task2)
        self.task_list.add_task(task3)

        filtered_tasks = self.task_list.filter_tasks("Category1")
        self.assertEqual(len(filtered_tasks), 2)

    def test_task_completed(self):
        task = Task("Test Task", "2023-01-01", 1, "Testing")
        self.task_list.add_task(task)

        self.task_list.task_completed(1)
        self.assertEqual(len(self.task_list.tasks), 0)
        self.assertEqual(len(self.task_list.archive), 1)

if __name__ == '__main__':
    unittest.main()
