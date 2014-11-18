__author__ = 'Jordan Thomas'

class Memory(object):
    '''
    classdocs
    '''
    mem = dict()


    def __init__(self):
        '''
        Constructor
        '''
    @classmethod
    def store (self, var, value):
        if(var == None):
            raise RuntimeError("invalid memory access");
        if(str(var).isupper()):
            var = var.lower()
        self.mem[var]=value

    @classmethod
    def fetch(self, var):
        if(var==None):
            raise RuntimeError("invalid memory access");
        if(str(var).isupper()):
            var = var.lower()
        return self.mem[var]