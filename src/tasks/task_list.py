class TaskList:
    def __init__(self):
        self.tasks = []

    def __str__(self): # We need to be able to print list as string 
        task_list_str = "\n".join(["[{}] {} (Due: {}, Priority: {}, Category: {})".format(
            index, task.title, task.due_date, task.priority, task.category) for index, task in enumerate(self.tasks)])
        return "<-----------------Task List----------------->\n{}".format(task_list_str)


    def add_task(self, task): #Function to add new task to Task List
        self.tasks.append(task)

    def edit_task(self, index, new_title, new_due_date = None, new_priority = 0, new_category = None): #Function to eedit the task in the list
        if 0 <= index < len(self.tasks): # We don't want to get crash because of wrong index
            # Updating task elements with new values
            task = self.tasks[index]
            task.title = new_title
            task.due_date = new_due_date
            task.priority = new_priority
            task.category = new_category
            print(f'Task at index {index} edited: {new_title}')
        else:
            print(f'Invalid index. Edit failed.')


    def delete_task(self, index): #Function to delete existing task
        if 0 <= index < len(self.tasks): #  Make sure no crash
            self.tasks.pop(index)
            print(f'Task at index {index} deleted')
        else:
            print('Invalid index.')

    def filter_tasks(self, category): # To print the tasks with specifig category
        filtered_tasks = []
        for task in self.tasks:
            if task.category == category:
                filtered_tasks.append(task)
        return filtered_tasks



        # filtered_tasks = [task for task in self.tasks if task.category == category]
        # return filtered_tasks
    
