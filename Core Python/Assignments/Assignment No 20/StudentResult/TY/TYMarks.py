class TYMarks:
    def __init__(self, theory, practical):
        self.theory = theory
        self.practical = practical

    def total(self):
        return self.theory + self.practical