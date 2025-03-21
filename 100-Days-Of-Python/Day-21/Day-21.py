class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self) -> None:
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self) -> None:
        super().breathe()
        print("doing this underwater")
    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breathe()
nemo.swim()
print(nemo.num_eyes)