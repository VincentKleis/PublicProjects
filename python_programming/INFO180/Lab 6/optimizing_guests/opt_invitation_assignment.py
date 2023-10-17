import copy
from opt_candidate import Candidate

# A representation of an assignment of invitations
class InvitationAssignment:

    def __init__(self, original=None):
        if original is None:
            self.the_assignment = dict()
        else:
            self.the_assignment = copy.deepcopy(original.the_assignment)

    # Is the candidate invited?
    def is_invited(self, candidate):
        return self.the_assignment[candidate]

    # Inverts the value of if the candidate is invited or not
    def invert(self, candidate):
        if not isinstance(candidate, Candidate):
            return
        old_assignment = self.the_assignment[candidate]
        self.the_assignment[candidate] = not old_assignment

    def set(self, candidate, assignment):
        self.the_assignment[candidate] = assignment

    def __str__(self):
        string = ""
        for candidate in self.the_assignment:
            if self.the_assignment.get(candidate):
                string += candidate.name + " "
        return string