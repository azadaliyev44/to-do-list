class Task:
    def __init__(self, title, due_date=None, priority=0, category=None):
        self.title = title
        self.priority = int(priority) if priority != "-" else 0
        self.due_date = due_date if due_date != "-" else None
        self.category = category if category != "-" else None

