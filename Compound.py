__author__ = 'Jordan Thomas'

class Compound(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.stmts = list()


    def add (self, s):
        self.stmts.append(s)

    def execute(self):
        for i in range (0,len(self.stmts)):
            self.stmts[i].execute()