from opt_candidate import Candidate


# The specification of an Invitation problem in the shape of candidates and
# the constraints
class InvitationProblem:

    all_candidates = Candidate.candidates

    # The ideal number of people is 12
    @staticmethod
    def constraint1(assignment):
        count = 0
        for c in InvitationProblem.all_candidates:
            if assignment.is_invited(c):
                count += 1

        diff = abs(12 - count)
        if diff == 0:
            return 30.0
        if diff == 1:
            return 20.0
        if diff == 2:
            return 10.0
        if diff == 3:
            return 5.0
        return 0.0

    # Same number of men and women
    @staticmethod
    def constraint2(assignment):
        count_men = 0
        count_women = 0
        for candidate in InvitationProblem.all_candidates:
            if assignment.is_invited(candidate):
                if candidate.woman:
                    count_women += 1
                else:
                    count_men += 1
        diff = abs(count_men - count_women)
        if diff == 0:
            return 20.0
        if diff == 1:
            return 15.0
        if diff == 2:
            return 10.0
        if diff == 3:
            return 5.0
        return 0.0

    # anne does not like ola. Do not invite both
    @staticmethod
    def constraint3(assignment):
        if assignment.is_invited(Candidate.anne) and assignment.is_invited(Candidate.ola):
            return -5.0
        else:
            return 0.0

    # Return a lower score if more than two of the
    # boys (Ivar, Lars, Rune and Helge) is invited
    @staticmethod
    def constraint4(assignment):
        count = 0

        if assignment.is_invited(Candidate.ivar):
            count += 1
        if assignment.is_invited(Candidate.lars):
            count += 1
        if assignment.is_invited(Candidate.rune):
            count += 1
        if assignment.is_invited(Candidate.helge):
            count += 1

        if count > 2:
            return -6.0
        else:
            return 0.0

    # Add the constraint functions here
    @staticmethod
    def constraint5(assignment):
        if assignment.is_invited(Candidate.sofie) and assignment.is_invited(Candidate.tom):
            return 5.0
        else: return 0.0

    def constraint6(assignment):
        first_letters = []
        for i in Candidate.candidates:
            if i not in first_letters:
                first_letters.append(i)
            if i in first_letters:
                return 0
        
        return 20
        
        
    @staticmethod
    def constraint_score(assignment):
        result = 0.0
        result += InvitationProblem.constraint1(assignment)
        result += InvitationProblem.constraint2(assignment)
        result += InvitationProblem.constraint3(assignment)
        result += InvitationProblem.constraint4(assignment)
        result += InvitationProblem.constraint5(assignment)
        result += InvitationProblem.constraint6(assignment)
        return result
