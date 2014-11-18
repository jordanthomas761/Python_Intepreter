__author__ = 'Jordan Thomas'

class BooleanExpression(object):
    '''
    classdocs
    '''
    class RelativeOperator(object):
        (LE, LT, GE, GT, EQ, NE) = range(0, 6)


    def __init__(self, op , expr1, expr2):
        '''
        Constructor
        '''
        if(expr1==None or expr2==None):
            raise ValueError("null expression argument")
        self.op=op
        self.expr1=expr1
        self.expr2=expr2

    def evaluate(self):
        value=False
        if(self.op==self.RelativeOperator.LE):
            value = self.expr1.evaluate() <= self.expr2.evaluate()
        elif(self.op==self.RelativeOperator.LT):
            value = self.expr1.evaluate() < self.expr2.evaluate()
        elif(self.op==self.RelativeOperator.GE):
            value = self.expr1.evaluate() >= self.expr2.evaluate()
        elif(self.op==self.RelativeOperator.GT):
            value = self.expr1.evaluate() > self.expr2.evaluate()
        elif(self.op==self.RelativeOperator.EQ):
            value = self.expr1.evaluate() == self.expr2.evaluate()
        elif(self.op==self.RelativeOperator.NE):
            value = self.expr1.evaluate() != self.expr2.evaluate()
        else:
            raise ValueError("Not a valid relative operator")
        return value
