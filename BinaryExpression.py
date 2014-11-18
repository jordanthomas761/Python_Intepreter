__author__ = 'Jordan Thomas'

from Expression import Expression

class BinaryExpression(Expression):
    '''
    classdocs
    '''
    class ArithmeticOperator(object):
        (ADD_OP, SUB_OP, MUL_OP, DIV_OP) = range(0, 4)


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
        value=0
        if(self.op==self.ArithmeticOperator.ADD_OP):
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif(self.op==self.ArithmeticOperator.SUB_OP):
            value = self.expr1.evaluate() - self.expr2.evaluate()
        elif(self.op==self.ArithmeticOperator.MUL_OP):
            value = self.expr1.evaluate() * self.expr2.evaluate()
        elif(self.op==self.ArithmeticOperator.DIV_OP):
            value = self.expr1.evaluate() / self.expr2.evaluate()
        else:
            raise ValueError("Incorrect arithmetic operator")
        return value
