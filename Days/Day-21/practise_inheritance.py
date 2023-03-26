class Animal:

    def __init__(self) :
        self.num_eyes =2

    def breathe(self):
        print("Inhale and Exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("We are doing this under water")
    
    
    def swim(self):
        print("Moving in water")

f = Fish()
f.swim()
f.breathe()
print(f.num_eyes)
