class Module:
    def __init__(self, module_id, title, content):
        self.module_id = module_id
        self.title = title
        self.content = content
        self.assignments = []

    def add_content(self, content):
        self.content = content

    def get_module_content(self):
        return self.content

    def add_assignment(self, assignment):
        self.assignments.append(assignment)
