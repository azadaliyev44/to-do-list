## 1.Git
Github activity for this project

[Activity](https://github.com/azadaliyev44/to-do-list/activity)

## 2.UML
Links to UML Diagrams(Activity Diagram, Class Diagram and Use Case Diagram)

[Activity Diagram](https://github.com/azadaliyev44/to-do-list/blob/main/media/activity%20diagram.png)  
[Class Diagram](https://github.com/azadaliyev44/to-do-list/blob/main/media/Class%20diagram.png)  
[Use Case Diagram](https://github.com/azadaliyev44/to-do-list/blob/main/media/use%20case%20diagram.png)  

## 3.Description of project with the methods of Requirements Engineering
**Overview**

**Name of Product**: To-Do List App

**Product Description**: This To-Do List application is to manage, keep track of tasks and complete them on time for users.The user can create, edit, and delete tasks, put due dates, make prioritization for tasks,categorize tasks, add subtasks, filter the tasks based on priority or categroy, see completed tasks in archive, send tasks by email.

**Target Audience**: Everyone

**Functional Requirements**

**Create tasks**: Users should be able to create new tasks, due dates,categories, and priorities.

**Edit tasks**: Users should be able to edit existing tasks, including their categoriesw, due dates, and priorities.

**Delete tasks**: Users should be able to delete tasks.

**Set due dates**: Users should be able to set due dates for tasks.

**Categorize tasks**: Users should be able to categorize tasks based on their choice.

**Prioritize tasks**: Users should be able to prioritize tasks based on their importance. The app should display tasks in order of priority.

**Track progress**: Users should be able to track their progress on tasks by marking them as completed.

**See completed tasks**: Users should be able to see the tasks which have been completed and stored in archive.

**Search for tasks**: Users should be able to search for tasks by name or description.

**Send email**: Users should be able to send tasks with email.

**Non-Functional Requirements**

**Usability**: The app should be easy to use and navigate for users.

**Performance**: The app should be fast and responsive.

**Security**: The app should protect user data from unauthorized access.

**Reliability**: The app should be reliable and should not crash or freeze.

**Scalability**: The app should be able to scale to accommodate a large number of users and tasks.

[Link for Trello](https://trello.com/invite/b/JMSsv8YF/ATTI3ecffc1dc436fb20e9cd2d437df229808D908298/to-do-list-app)  
[Link for Monday](https://view.monday.com/1368315352-e9b36ecee3e8ec195e4deb2aa7667410?r=euc1)
 

## 4.Analysis

**A.Checklist for To-Do List App Analysis**

1. Defining the Problem 
2. Market analysis
3. Business Model and Profit
4. Development
5. Competitive Analysis
6. Target Audience
7. Needs and Requirements of Users
8. Competitive points
9. Marketing and Market Strategy

**B.Analysis of To-Do List App**

1. Defining the Problem 

The main problem to be mentioned is the difficulty of managing tasks and deadlines efficiently and in the right order, So, many people have difficulties while keeping track of their tasks, which can lead to missed deadlines, forgotten tasks and stress. A to-do list app can help to solve this problem by providing a centralized manging point for tasks, reminders.

2. Market analysis

The To-do list app market is hard to estimate a worth for it, it can be as high as you can imagine, because of a growing demand for innovative and user-friendly solutions. The market is expected to continue expanding in the coming years as it has been growing for years, driven by increasing smartphone usage and the growing need for effective task management tools.

3. Business Model and Profit

A freemium business model can be best option to make profit form this project, it is offering a basic version of the app for free and providing premium features with in-app purchases. This approach will allow us to reach a wider audience as it is free while monetizing our app effectively with users who wants to use premium features. Placing ads may not be best option because ads can be annoying sometimes so it can lead a bad reputation for our project

4. Development

The development of our To-do list app is being developed by a team of experienced software developers who are expert in using effective methods of development. Our focus is on making sure that the app is scalable, secure,user friendly for all ages, and integrates with other productivity tools.

5. Competitive Analysis

Of course there are some existing to-do list apps in the market, such as Todoist, Wunderlist, and Evernote. These apps have a variety of features. Like feature to create lists, set reminders, and sync across your devices, but there is still room for new features in the to-do list app market, for example, many current apps lack the feature to prioritize tasks, track your time spent on each tasks, or collaborate with others on tasks and make changes on the current situation of the task.

6. Target Audience

Our To-Do List app targets a wide range of users, such as students, professionals, teachers or even individuals who wants to improve their own productivity. Our app will provide service to a wide range of tasks, from personal tasks to work-related projects, from creative tasks to personal goals.
As our app have unique features which others do not have:  
**I Integrations**: Our application integrates other productivity tools, such as calendars apps, email apps, and note-taking apps, giving a centralized experience for managing tasks and duties.
**II Task Management**: This to-do app offers better task management features, which create possibilites for users to customize their path of work, set reminders, prioritize their tasks,caategorize their tasks, and keep the track of progress.
**III AI Assistant**: This to-do app comes with an AI that actively suggests tasks based on current tasks, makes reminders, and offers to the user personalized recommendations based on their behavior.
**IV Multiplatform Application**: This to-do app will be available on all platforms, including desktops, smartphones, and tablets.

7. Needs and Requirements of Users

User have a number of key needs and requirements that users seek in a To-do list app. The most important key points for us are seamless integrations with other productivity tools, personalized task management features, and AI-powered assistants to provide productive support and recommendations as there is lack of these features in market.

8. Competitive points

Our To-do list app will take place in the competition by offering a unique and different features, such as personalization options, and seamless integrations with other productive applications. We will have diffences by emphasizing our focus on user needs, personalization, and AI-powered assistance.

9. Marketing and Market Strategy

Our marketing and market strategy will be open to new trends and targeted by utilizing a mix of online and offline channels to reach our target users and create interest in our app forr users. We will utilize social media platforms, create content that are different from standard contents of other companies, influencer partners, and run targeted advertising campaigns to effectively reach our potential users.


## 5.DDD

Links for DDD  

[Visual Event Storming](https://github.com/azadaliyev44/to-do-list/blob/main/media/visual%20event%20storming.png)  
[Core Domain Chart](https://github.com/azadaliyev44/to-do-list/blob/main/media/Core%20Domain%20Chart.png)  
[Domain Mapping and Relations](https://github.com/azadaliyev44/to-do-list/blob/main/media/Domain%20Mapping.png)  


## 7.Clean Code Development

**A.**  
1.Single Responsibility Principle:  
Each methods in project has a clear and single responsiblity. SRP has been focused during development of this project. Such as add_task, edit_task, delete_task, filter_tasks and so on.
This kind of managing methods aligns with this principle which makes maintaining and reading codes more convinient.  
2.Error Handling  
The arguments passed in methods are checked before the rest is performed if they are valid to avoid crashes.  
Example: 
```
def edit_task(
        self, index, new_title, new_due_date=None, new_priority=0, new_category=None
        ):  # Function to eedit the task in the list
        index = int(index) - 1
        new_priority = int(new_priority)
        if (0 <= int(index) < len(self.tasks)):  # We don't want to get crash because of wrong index
            ...
        else:
            print(f"Invalid index. Edit failed.")

def command_add(task_list, tokens):
        if len(tokens) >= 2: #Here argument is checked if it is vaild
            args = eval(str(tokens[1:]))
            task = Task(*args)
            task_list.add_task(task)
            print("Task added successfully.")
        
         else:
            print("Invalid arguments for 'add' command.")
```
3.Encapsulated methods  
Creating methods separatedly and calling it where needed enhances readability and maintainability.
Example:
```
if command == 'add':
            command_add(task_list, tokens)

def command_add(task_list, tokens):
    if len(tokens) >= 2: 
        args = eval(str(tokens[1:]))
        task = Task(*args)
        task_list.add_task(task)
        print("Task added successfully.")
                
    else:
        print("Invalid arguments for 'add' command.")
```
4.Meaningful Function and Variable Names  
Naming functions variables, classes and so on is important part of Clean Code Development as it makes code understandable.
Random or irrelevant naming creates challange to find out for what variable or function is used.
Examples:  
```
def filter_tasks(self, category):  # To print the tasks with specifig category
        (
        ...
        )

def add_task(self, task):  # Function to add new task to Task List
    (
    ...
    ) 
```  
5.Comments  
Comments makes it easier for others to understand or to remember for author what does a specific line or function, why certain code decisions made.  
Example:
```
class EmailService:
    def send_email(body, to_email):
        # email server details
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'ourtodoapp@gmail.com'
        smtp_password = 'wxcu eqbg hscg snnh'
        # Sender and recipient email addresses
        sender_email = 'ourtodoapp@gmail.com'
        recipient_email = to_email

        # We construct the email message
        message = MIMEText(body)
        message['Subject'] = "Task List"
        message['From'] = sender_email
        message['To'] = recipient_email

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

```  
6.Formatting
Using spaces and new lines are important for better view and readability of the code. FOrtunately, there are some tools to do it 
automatically. For this project "black" is used to improve formatting.    

**B.** [Link for CCD Cheat Sheet PDF](https://github.com/azadaliyev44/to-do-list/blob/main/media/CCD%20CheatSheet.pdf)  



## 10.IDE
I use generally Viual Studio for project development. Some extensions are very usefull which are very useful during   
development such as "Regex Previewer", "Live Server", "VS Code Counter" however not all of these were used   
during this project

-Ctrl+/      : Comment selected or current line    
-Alt+Up      : Move up line      
-Alt+Down    : Move down line    
-F5          : Debug   
-Shift+F5    : Stop debug  
-Alt+Left Click    :to add cursor multiple places in code (Especially very usefull when you need to correct a TYPO)  
-Hold down Scoll button and move     : Similar to Alt+Left Click, select a part of multiple lines and adds cursor to each line  
-Shift+Arrow buttons  : Select a part of line or whole multiple lines  
-Ctrl+Arrow buttons   : Jump over the whole word   
-Ctrl+Backspace       : Delete the whole word  
these are most used shortcuts for me.  
And of course   
-Ctrl+C   
-Ctrl+V to copy and paste



## 0.Project description
Azad Aliyev - To-Do List  

**How to use commands**  
"-" is reserved character, it cannot be used in text, it is used for empty input    
*Example :* `add Hello - 1 -`    
*Output ->  Title: Hello, DueDate: None, Priority: 1, Category: None*  

add -> add task in format : add Title DueDate Priority Category (use "-" for empty input)   
edit -> edit task in format : edit Index Title DueDate Priority Category (use "-" for empty input)  
delete -> delete task in format : delete Index  
filter -> filter tasks in format : filter Category  
complete -> complete task in format : complete Index  
list -> list tasks  
archive -> list archived tasks  
email -> send tasks to email in format : email your_email@example.com  
exit -> exit program  

---

This To-Do List program will have functions to add, edit and delete tasks. Priority level can be applied for each task, 
fulfilled tasks can be removed form main list and stored in archive. Tasks can be categorized under desired name.
User can send the tasks via email.
