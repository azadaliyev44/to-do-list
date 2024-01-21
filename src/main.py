from tasks.task import Task
from tasks.task_list import TaskList
from email1.email_service import EmailService



def main():
    print("help, add, exit, list, edit , delete, filter, complete, email, archive")
    task_list = TaskList()

    while True:
        # Get user input
        user_input = input("Enter command: ")

        # Split user input into command and arguments
        tokens = user_input.split()
        command = tokens[0].lower() 
        
         
        if command == 'add':
            if len(tokens) >= 2: 
                args = eval(str(tokens[1:]))
                task = Task(*args)
                task_list.add_task(task)
                print("Task added successfully.")
                
            else:
                print("Invalid arguments for 'add' command.")

        elif command == 'edit':
            if len(tokens) >= 2: 
                args = eval(str(tokens[1:])) 
                task_list.edit_task(*args)
                print("Task edited successfully.")
                
            else:
                print("Invalid arguments for 'edit' command.")

        elif command == 'delete':
            if len(tokens) >= 2: 
                args = eval(str(tokens[1:])) 
                task_list.delete_task(*args)
                print("Task deleted successfully.")
                
            else:
                print("Invalid arguments for 'delete' command.")

        elif command == 'filter':
            if len(tokens) >= 2: 
                args = eval(str(tokens[1:])) 
                task_list.filter_tasks(*args)
                print("Task filtered successfully.")
                
            else:
                print("Invalid arguments for 'filter' command.")
        
        elif command == 'complete':
            if len(tokens) >= 2: 
                args = eval(str(tokens[1:])) 
                task_list.task_completed(*args)
                print("Task completed successfully.")
                
            else:
                print("Invalid arguments for 'complete' command.")

        elif command == 'email':
            if len(tokens) >= 2: 
                EmailService.send_email(task_list.print_tasks(), tokens[1])

        elif command == 'archive':
                task_list.archive_show()


        elif command == 'list':
            # Example: list
            print(task_list.print_tasks())

        elif command == 'help':
            # Example: list
            print('add -> add task in format : add Title DueDate Priority Category (use "-" for empty input) \n' 
                  'edit -> edit task in format : edit Index Title DueDate Priority Category (use "-" for empty input) \n'
                  'delete -> delete task in format : delete Index \n'
                  'filter -> filter tasks in format : filter Category \n'
                  'complete -> complete task in format : complete Index \n'
                  'list -> list tasks \n'
                  'archive -> list archived tasks \n'
                  'email -> send tasks to email in format : email your_email@example.com \n'
                  'exit -> exit program \n'
                  )

        elif command == 'exit':
            # Example: exit
            print("Exiting the program.")
            break



        else:
            print("Invalid command. Available commands: help, add, exit, list, edit, delete, filter, complete, email, archive")

if __name__ == "__main__":
    main()