__author__ = 'Jordan Thomas'

from LexicalAnalyzer import LexicalAnalyzer
from Token import Token
from TokenType import TokenType
from ParserException import ParserException
from Feature import Feature
from Compound import Compound
from PrintStatement import PrintStatement
from AssignmentStatement import AssignmentStatement
from LoopStatement import LoopStatement
from IfStatement import IfStatement
from Id import Id
from BooleanExpression import BooleanExpression
from LiteralInteger import LiteralInteger
from BinaryExpression import BinaryExpression

class Parser(object):
    '''
    classdocs
    '''


    def __init__(self, fileName):
        '''
        Constructor
        '''
        if fileName == None:
            raise ValueError("null file name")
        self.lex= LexicalAnalyzer(fileName)

    def parse(self):
        tok= self.lex.getNextToken()
        self.match(tok, TokenType.FEATURE_TOK)
        iden = self.getID()
        tok= self.lex.getNextToken()
        self.match(tok, TokenType.IS_TOK)
        tok= self.lex.getNextToken()
        self.match(tok, TokenType.DO_TOK)
        comp = self.getCompound()
        tok= self.lex.getNextToken()
        self.match(tok, TokenType.END_TOK)
        '''if iden!=tok.getLexeme():
            raise ParserException ("invalid id", tok.getRowNum(), tok.getColumnNum())'''
        return Feature(comp)

    def getCompound(self):
        comp= Compound()
        s = self.getStatement()
        comp.add(s)
        tok = self.lex.getLookaheadToken()
        while self.isValidStartOfStatement(tok):
            s= self.getStatement()
            comp.add(s)
            tok= self.lex.getLookaheadToken()
        return comp

    def isValidStartOfStatement(self, tok):
        assert tok != None
        return tok.getTokenType() == TokenType.ID_TOK or tok.getTokenType() == TokenType.IF_TOK or tok.getTokenType() == TokenType.FROM_TOK or tok.getTokenType() == TokenType.PRINT_TOK


    def getStatement(self):
        tok=self.lex.getLookaheadToken()
        if tok.getTokenType() == TokenType.IF_TOK:
            s=self.getIfStatement()
        elif tok.getTokenType() == TokenType.ID_TOK:
            s = self.getAssignmentStatement()
        elif tok.getTokenType() == TokenType.FROM_TOK:
            s = self.getLoopStatement()
        elif tok.getTokenType() == TokenType.PRINT_TOK:
            s = self.getPrintStatement()
        else:
            raise ParserException ("statement expected", tok.getRowNum(), tok.getColumnNum())
        return s

    def getPrintStatement(self):
        tok = self.lex.getNextToken()
        self.match (tok, TokenType.PRINT_TOK)
        tok = self.lex.getNextToken()
        self.match (tok, TokenType.LEFT_PAREN_TOK)
        expr = self.getExpression()
        tok = self.lex.getNextToken()
        self.match (tok, TokenType.RIGHT_PAREN_TOK)
        return PrintStatement (expr)


    def getLoopStatement(self):
        tok= self.lex.getNextToken()
        self.match(tok, TokenType.FROM_TOK)
        ass = self.getAssignmentStatement()
        tok= self.lex.getNextToken()
        self.match(tok, TokenType.UNTIL_TOK)
        expr = self.getBooleanExpression()
        tok= self.lex.getNextToken()
        self.match(tok, TokenType.LOOP_TOK)
        comp = self.getCompound()
        tok= self.lex.getNextToken()
        self.match(tok, TokenType.END_TOK)
        return LoopStatement(ass, expr, comp)


    def getAssignmentStatement(self):
        var= self.getID()
        tok = self.lex.getNextToken()
        self.match (tok, TokenType.ASSIGN_TOK)
        expr = self.getExpression()
        return AssignmentStatement(var, expr)

    def getIfStatement(self):
        tok = self.lex.getNextToken()
        self.match (tok, TokenType.IF_TOK)
        expr = self.getBooleanExpression ()
        tok = self.lex.getNextToken()
        self.match (tok, TokenType.THEN_TOK)
        comp1 = self.getCompound()
        tok = self.lex.getNextToken()
        self.match (tok, TokenType.ELSE_TOK)
        comp2 = self.getCompound()
        tok = self.lex.getNextToken()
        self.match (tok, TokenType.END_TOK)
        return IfStatement (expr, comp1, comp2)

    def getID(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.ID_TOK)
        if len(tok.getLexeme()) !=1:
            raise ParserException("invalid identifier", tok.getRowNum(), tok.getColumnNum())
        return Id(tok.getLexeme()[0:1])

    def getLiteralInteger(self):
        tok= self.lex.getNextToken()
        self.match(tok,TokenType.LIT_INT_TOK)
        value = 0
        try:
            value = int(tok.getLexeme())
        except:
            raise ParserException("Literal integer expected", tok.getRowNum, tok.getColumnNum)
        return LiteralInteger(value)

    def getBooleanExpression(self):
        op= self.getRelativeOperator()
        expr1= self.getExpression()
        expr2= self.getExpression()
        return BooleanExpression(op, expr1, expr2)

    def getRelativeOperator(self):
        tok= self.lex.getNextToken()
        if(tok.getTokenType()==TokenType.LT_TOK):
            op=BooleanExpression.RelativeOperator.LT
        elif(tok.getTokenType()==TokenType.LE_TOK):
            op=BooleanExpression.RelativeOperator.LE
        elif(tok.getTokenType()==TokenType.GT_TOK):
            op=BooleanExpression.RelativeOperator.GT
        elif(tok.getTokenType()==TokenType.GE_TOK):
            op=BooleanExpression.RelativeOperator.GE
        elif(tok.getTokenType()==TokenType.EQ_TOK):
            op=BooleanExpression.RelativeOperator.EQ
        elif(tok.getTokenType()==TokenType.NE_TOK):
            op=BooleanExpression.RelativeOperator.NE
        else:
            raise ParserException("relational operator expected", tok.getRowNum(), tok.getColumnNum())
        return op

    def getExpression(self):
        tok= self.lex.getLookaheadToken()
        if (tok.getTokenType() == TokenType.ID_TOK):
            expr=self.getID()
        elif (tok.getTokenType() == TokenType.LIT_INT_TOK):
            expr= self.getLiteralInteger()
        else:
            op = self.getArithmeticOperator()
            expr1 = self.getExpression()
            expr2 = self.getExpression()
            expr = BinaryExpression (op, expr1, expr2)
        return expr

    def getArithmeticOperator(self):
        tok= self.lex.getNextToken()
        if tok.getTokenType()==TokenType.ADD_TOK:
            op=BinaryExpression.ArithmeticOperator.ADD_OP
        elif tok.getTokenType()==TokenType.SUB_TOK:
            op=BinaryExpression.ArithmeticOperator.SUB_OP
        elif(tok.getTokenType()==TokenType.MUL_TOK):
            op=BinaryExpression.ArithmeticOperator.MUL_OP
        elif(tok.getTokenType()==TokenType.DIV_TOK):
            op=BinaryExpression.ArithmeticOperator.DIV_OP
        else:
            raise ParserException("arithmetic operator expected", tok.getRowNum(), tok.getColumnNum())
        return op



    def match(self, tok, expected):
        assert tok!= None
        if (tok.getTokenType() != expected):
            raise ParserException (str(expected) + "expected" , tok.getRowNum(), tok.getColumnNum())