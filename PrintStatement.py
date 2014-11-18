__author__ = 'Jordan Thomas'


from Statement import Statement
from Expression import Expression

class PrintStatement(Statement):
    '''
    classdocs
    '''


    def __init__(self, expr):
        '''
        Constructor
        '''
        if expr == None:
            raise ValueError("null expression argument")
        self.expr = expr

    def execute(self):
        print(str(self.expr.evaluate()))
