class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.progress = {}

    def register(self):
        # Code for registering user
        pass

    def login(self):
        # Code for user login
        pass

    def update_progress(self, course_id, progress):
        self.progress[course_id] = progress
