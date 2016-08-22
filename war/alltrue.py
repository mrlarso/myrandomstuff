class anything():
    def __init__(self,other):
        pass
    def __eq__(self,other):
        return True
    __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__

print anything("yo") > 10

print anything(81) < 82
