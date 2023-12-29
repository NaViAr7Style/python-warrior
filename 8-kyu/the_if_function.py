def _if(condition, first, second):
    first() if condition else second()

# Cool example with lambda
_if = lambda x, y, z: (x and y or z)()

def first():
    print("First Function")

def second():
    print("Second Function")

if __name__ == "__main__":
    _if(False, first, second)