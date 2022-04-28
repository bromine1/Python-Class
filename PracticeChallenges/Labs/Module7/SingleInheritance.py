class bacteria():
    def __init__(self, name):
        self.name = name

class SuperBacteria(bacteria):
    def __init__(self, name):
        super().__init__(name)

Disease = SuperBacteria("Providencia")

print(Disease.name)

