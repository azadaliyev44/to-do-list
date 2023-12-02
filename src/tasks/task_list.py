class TaskList:
    def __init__(self):
        self.tasks = []
        self.archive = []

    def __str__(self): # We need to be able to print list as string 
        task_list_str = "\n".join(["[{}] {} (Due: {}, Priority: {}, Category: {})".format(
            index, task.title, task.due_date, task.priority, task.category) for index, task in enumerate(self.tasks)])
        return "<-----------------Task List----------------->\n{}".format(task_list_str)

    def add_task(self, task): #Function to add new task to Task List
        self.tasks.append(task)
        self.tasks = sorted(self.tasks,key=lambda x: x.priority) # Reorder list based on priority level after each input 

    def add_subtask(self,index, subtask):
        if 0 <= index < len(self.tasks) and len(self.tasks != 0):
            pass
            


    def edit_task(self, index, new_title, new_due_date = None, new_priority = 0, new_category = None): #Function to eedit the task in the list
        if 0 <= index < len(self.tasks): # We don't want to get crash because of wrong index
            # Updating task elements with new values
            task = self.tasks[index]
            task.title = new_title
            task.due_date = new_due_date
            task.priority = new_priority
            task.category = new_category
            self.tasks = sorted(self.tasks,key=lambda x: x.priority) # Reorder list based on priority level after each modification 
            print(f'Task at index {index} edited: {new_title}')
        else:
            print(f'Invalid index. Edit failed.')


    def delete_task(self, index): #Function to delete existing task
        if 0 <= index < len(self.tasks): #  Make sure no crash
            self.tasks.pop(index)
            print(f'Task at index {index} deleted')
        else:
            print('Invalid index.')

    def filter_tasks(self , category): # To print the tasks with specifig category
        filtered_tasks = []
        for task in self.tasks:
            if task.category == category:
                filtered_tasks.append(task) #Create list that contains filtered tasks based on category
        filtered_task_list_str = "\n".join(["[{}] {} (Due: {}, Priority: {}, Category: {})".format(
            index, task.title, task.due_date, task.priority, task.category) for index, task in enumerate(filtered_tasks)])
        return "<-------------Filtered Task List------------>\n{}".format(filtered_task_list_str) #Print filtered elements in readable form not their memory adress
    
    def task_completed (self, index):
        if 0 <= index < len(self.tasks):
            completed_task = self.tasks.pop(index)
            self.archive.append(completed_task)
            print(f'Task at index {index} moved to archive: {completed_task.title}')
        else:
            print('Invalid index.')

    def archive_show(self):
        archive_str = "\n".join(["[{}] {} (Due: {}, Priority: {}, Category: {})".format(
            index, task.title, task.due_date, task.priority, task.category) for index, task in enumerate(self.archive)])
        return "<-------------Archive------------>\n{}".format(archive_str) #Print filtered elements in readable form not their memory adress

    
