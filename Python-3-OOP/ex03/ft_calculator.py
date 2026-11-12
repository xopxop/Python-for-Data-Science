class calculator:
    def __init__(self, numbs: list):
        self.numbs = numbs

    def __add__(self, object) -> None:
        for i in range(len(self.numbs)):
            self.numbs[i] += object
        print(self.numbs)

    def __mul__(self, object) -> None:
        for i in range(len(self.numbs)):
            self.numbs[i] *= object
        print(self.numbs)

    def __sub__(self, object) -> None:
        # In-place mutation
        self.numbs[:] = [x - object for x in self.numbs]
        print(self.numbs)

    def __truediv__(self, object) -> None:
        if object == 0:
            raise ZeroDivisionError()
        #  In-place mutation
        self.numbs[:] = [x / object for x in self.numbs]
        print(self.numbs)
