class Animals:
    pass
class pat(Animals):
    pass
class dog(pat):
    @staticmethod
    def bark(self):
        print("the dog was bark: bow bow  ")

s1 = dog()
s1.bark()        