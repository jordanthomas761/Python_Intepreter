__author__ = 'Jordan Thomas'

from Expression import Expression
from Memory import Memory

class Id(Expression):
    '''
    classdocs
    '''


    def __init__(self, var):
        '''
        Constructor
        '''
        self.var=var

    def evaluate(self):
        return Memory.fetch(self.var)

    def setValue(self, value):
        Memory.store(self.var, value)

    def __str__(self):
        return self.var