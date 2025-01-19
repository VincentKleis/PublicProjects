
# Class representing all the possible candidates to be invited
class Candidate:

    def __init__(self, name, likeability, woman):
        self.name = name
        self.likeability = likeability
        self.woman = woman

    def __hash__(self):
        result = self.name.__hash__() + int(self.likeability)
        if self.woman:
            result += 100
        return result

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.likeability != other.likeability:
            return False
        if self.woman != other.woman:
            return False
        return True


Candidate.anne = Candidate("Anne", 1.5, True)
Candidate.guri = Candidate("Guri", 0.3, True)
Candidate.nina = Candidate("Nina", 1.2, True)
Candidate.emma = Candidate("Emma", 0.1, True)
Candidate.berit = Candidate("Berit", 0.6, True)
Candidate.sofie = Candidate("Sofie", 0.3, True)
Candidate.kristin = Candidate("Kristin", 0.9, True)
Candidate.kari = Candidate("Kari", 1.0, True)
Candidate.solveig = Candidate("Solveig", 1.4, True)
Candidate.britt = Candidate("Britt", 0.8, True)
Candidate.marit = Candidate("Marit", 1.0, True)
Candidate.aud = Candidate("Aud", 1.1, True)
Candidate.elsa = Candidate("Elsa", 0.2, True)
Candidate.astrid = Candidate("Astrid", 0.7, True)
Candidate.tone = Candidate("Tone", 1.2, True)
Candidate.per = Candidate("Per", 1.3, False)
Candidate.ola = Candidate("Ola", 0.9, False)
Candidate.knut = Candidate("Knut", 0.3, False)
Candidate.ivar = Candidate("Ivar", 1.4, False)
Candidate.nils = Candidate("Nils", 1.1, False)
Candidate.dag = Candidate("Dag", 0.6, False)
Candidate.jens = Candidate("Jens", 0.7, False)
Candidate.tom = Candidate("Tom", 0.3, False)
Candidate.inge = Candidate("Inge", 0.8, False)
Candidate.lars = Candidate("Lars", 1.1, False)
Candidate.even = Candidate("Even", 1.0, False)
Candidate.erik = Candidate("Erik", 0.4, False)
Candidate.artur = Candidate("Artur", 0.9, False)
Candidate.helge = Candidate("Helge", 1.1, False)
Candidate.rune = Candidate("Rune", 0.8, False)

Candidate.candidates = [Candidate.anne, Candidate.guri, Candidate.nina, Candidate.emma, Candidate.berit, Candidate.sofie, \
                        Candidate.kristin, Candidate.kari, Candidate.solveig, Candidate.britt, Candidate.marit, \
                        Candidate.aud, Candidate.elsa, Candidate.astrid, Candidate.tone, Candidate.per, Candidate.ola, \
                        Candidate.knut, Candidate.ivar, Candidate.nils, Candidate.dag, Candidate.jens, Candidate.tom, Candidate.inge, \
                        Candidate.lars, Candidate.even, Candidate.erik, Candidate.artur, Candidate.helge, Candidate.rune]