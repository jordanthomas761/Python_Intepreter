__author__ = 'Jordan Thomas'
from Statement import Statement
from Expression import Expression

class LoopStatement(Statement):
    '''
    classdocs
    '''


    def __init__(self, ass, expr, comp):
        '''
        Constructor
        '''
        if ass == None:
            raise ValueError ("invalid variable argument")
        if expr == None:
            raise ValueError ("invalid boolean expression arguments")
        if comp == None:
            raise ValueError ("null Compound argument")
        self.ass = ass
        self.expr = expr
        self.comp = comp


    def execute(self):
        self.ass.execute()
        while not self.expr.evaluate():
            self.comp.execute()
