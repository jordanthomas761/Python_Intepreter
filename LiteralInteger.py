__author__ = 'Jordan Thomas'

from Expression import Expression
class LiteralInteger(Expression):
    '''
    classdocs
    '''


    def __init__(self, value):
        '''
        Constructor
        '''
        self.value=value



    def evaluate(self):
        return self.value