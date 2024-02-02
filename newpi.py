import math
from decimal import *
getcontext().prec = 100
class pi:
    def __init__(self, n, p):
        self.n = n
        self.p = p
    
    def new(self):
        try:
            return (self.p-self.p/self.n)
        except:
            print(self.p-self.p/self.n)

    def alt(self):
        try:   
            n = self.p-self.p/self.n
            return self.p-self.p/n
        except:
            return self.p-self.p/n
class soical(pi):
    def __init__(self, n, p):
        super(soical, self).__init__(n, p)
initiate = soical(Decimal(8.29), Decimal(3.58))
afterburn = soical(8.29, 3.58)
x = afterburn.new()
v = (afterburn.new() % math.pi) * (afterburn.new() / math.pi) + (afterburn.new() + math.pi) - (math.sqrt(afterburn.new()) * math.sqrt(math.pi))
c = (v-x)+math.pi-(v%x)
print(initiate.new())
print((afterburn.new() % math.pi) * (afterburn.new() / math.pi) + (afterburn.new() + math.pi) - (math.sqrt(afterburn.new()) * math.sqrt(math.pi)))
print(c)
print("last calculation has to be seperate from the super so it is printed, not calculated, the calculation is the above around super, below without it")
print("-3.1415652429362213")
#only works outside of super, test it in a python3 env, comes out to -3.1415652429362213 despite being written the same way as c without super
# import math
# (((3.58-3.58/8.29) % math.pi) * ((3.58-3.58/8.29) / math.pi) + ((3.58-3.58/8.29) + math.pi) - (math.sqrt(3.58-3.58/8.29) * math.sqrt(math.pi)) - (3.58-3.58/8.29)) + math.pi - ((3.58-3.58/8.29) - ((3.58-3.58/8.29) % math.pi) * ((3.58-3.58/8.29) / math.pi) + ((3.58-3.58/8.29) + math.pi) - math.sqrt(3.58-3.58/8.29) * math.sqrt(math.pi) % (3.58-3.58/8.29))