__author__ = 'Jordan Thomas'

from Expression import Expression
from Statement import Statement
from Memory import Memory

class AssignmentStatement(Statement):
    '''
    classdocs
    '''


    def __init__(self, var, expr):
        '''
        Constructor
        '''
        if(expr==None):
            raise ValueError("invalid expression argument")
        self.expr=expr
        if(var==None):
            raise ValueError("invalid variable argument")
        self.var=var

    def execute(self):
        self.var.setValue(self.expr.evaluate())