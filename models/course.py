class Course:
    def __init__(self, course_id, title, description):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def get_course_content(self):
        return self.modules

    def update_course(self, title, description):
        self.title = title
        self.description = description
