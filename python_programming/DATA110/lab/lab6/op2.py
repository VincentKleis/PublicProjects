class fibonacci:
    fibonacci_list = []
    n = 0
    def neste(self):
        if self.n == 0 or self.n == 1:
            currant = 1
            self.fibonacci_list.append(currant)
            self.n += 1
            print(currant)
        else:
            currant = sum(self.fibonacci_list[self.n-2:self.n])
            self.fibonacci_list.append(currant)
            self.n += 1
            print(currant)

g = fibonacci()
g.neste()
g.neste()
g.neste()
g.neste()
g.neste()
g.neste()
g.neste()
g.neste()