__author__ = 'Jordan Thomas'

from Statement import Statement
from Expression import Expression

class IfStatement(Statement):
    '''
    classdocs
    '''


    def __init__(self, expr, comp1, comp2):
        '''
        Constructor
        '''
        if (expr == None):
            raise ValueError ("null exception argument")
        if (comp1 == None or comp2 == None):
            raise ValueError ("null statement list argument")
        self.expr=expr
        self.comp1=comp1
        self.comp2=comp2


    def execute(self):
        if(self.expr.evaluate()):
            self.comp1.execute()
        else:
            self.comp2.execute()