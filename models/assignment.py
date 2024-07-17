class Assignment:
    def __init__(self, assignment_id, description):
        self.assignment_id = assignment_id
        self.description = description
        self.solution = None
        self.feedback = None

    def submit_solution(self, solution):
        self.solution = solution

    def provide_feedback(self, feedback):
        self.feedback = feedback
