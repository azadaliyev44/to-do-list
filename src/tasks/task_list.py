class TaskList:
    def __init__(self):
        self.tasks = []
        self.archive = []

    def __str__(self):  # We need to be able to print list as string not their address
        task_list_str = "\n".join(
            [
                "[{}] {} (Due: {}, Priority: {}, Category: {})".format(
                    index, task.title, task.due_date, task.priority, task.category
                )
                for index, task in enumerate(self.tasks)
            ]
        )
        return "<-----------------Task List----------------->\n{}".format(task_list_str)

    def add_task(self, task):  # Function to add new task to Task List
        self.tasks.append(task)
        self.tasks = sorted(
            self.tasks, key=lambda x: x.priority
        )  # Reorder list based on priority level after each input

    def edit_task(
        self, index, new_title, new_due_date=None, new_priority=0, new_category=None
    ):  # Function to eedit the task in the list
        index = int(index) - 1
        new_priority = int(new_priority)
        if (
            0 <= int(index) < len(self.tasks)
        ):  # We don't want to get crash because of wrong index
            # Updating task elements with new values
            task = self.tasks[int(index)]
            task.title = new_title if new_title != "-" else task.title
            task.due_date = new_due_date if new_due_date != "-" else task.due_date
            task.priority = new_priority if new_priority != "-" else task.priority
            task.category = new_category if new_category != "-" else task.category
            self.tasks = sorted(
                self.tasks, key=lambda x: x.priority
            )  # Reorder list based on priority level after each modification
            print(f"Task at index {index+1} edited: {new_title}")
        else:
            print(f"Invalid index. Edit failed.")

    def delete_task(self, index):  # Function to delete existing task
        index = int(index) - 1
        if 0 <= index < len(self.tasks):  #  Make sure no crash
            self.tasks.pop(index)
            print(f"Task at index {index+1} deleted")
        else:
            print("Invalid index.")

    def filter_tasks(self, category):  # To print the tasks with specifig category
        filtered_tasks = []
        for task in self.tasks:
            if task.category == category:
                filtered_tasks.append(
                    task
                )  # Create list that contains filtered tasks based on category
        filtered_task_list_str = "\n".join(
            [
                "[{}] {} (Due: {}, Priority: {}, Category: {})".format(
                    index, task.title, task.due_date, task.priority, task.category
                )
                for index, task in enumerate(filtered_tasks)
            ]
        )
        print(
            "<-------------Filtered Task List------------>\n{}".format(
                filtered_task_list_str
            )
        )  # Print filtered elements in readable form not their memory adress
        return filtered_tasks

    def task_completed(self, index):
        index = int(index) - 1
        if 0 <= index < len(self.tasks):
            completed_task = self.tasks.pop(index)
            self.archive.append(completed_task)
            print(f"Task at index {index+1} moved to archive: {completed_task.title}")
        else:
            print("Invalid index.")

    def archive_show(self):
        archive_str = "\n".join(
            [
                "[{}] {} (Due: {}, Priority: {}, Category: {})".format(
                    index, task.title, task.due_date, task.priority, task.category
                )
                for index, task in enumerate(self.archive)
            ]
        )
        print(
            "<-------------Archive------------>\n{}".format(archive_str)
        )  # Print filtered elements in readable form not their memory adress

    def print_tasks(self):
        if not self.tasks:
            print("Task list is empty.")
        else:
            task_list_str = "\n".join(
                [
                    "[{}] {} (Due: {}, Priority: {}, Category: {})".format(
                        index, task.title, task.due_date, task.priority, task.category
                    )
                    for index, task in enumerate(self.tasks, start=1)
                ]
            )
            return "<-----------------Task List----------------->\n{}".format(
                task_list_str
            )
