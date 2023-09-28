class Queue:
    line = []
    def __init__(self, name = []):
        self.line.extend(name)

    def add(self, person):
        self.line.append(person)

    def remove(self):
        return self.line.pop(0)

    def number_in_queue(self, person):
        return self.line.index(person)

que_1 = Queue(['Abraham','Joakim'])
que_1.add('Ismael')
que_1.add('Hanne')
que_1.number_in_queue('Ismael')

print(que_1.line, que_1.number_in_queue('Ismael'))