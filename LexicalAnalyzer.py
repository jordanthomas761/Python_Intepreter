__author__ = 'BIWMac'

from LexException import LexException
from Token import Token
from TokenType import TokenType

class LexicalAnalyzer(object):
    '''
    classdocs
    '''

    def __init__(self, fileNeme):
        '''
        Constructor
        '''
        if (fileNeme == None):
            raise ValueError("null file name argument")
        inputFile = open(fileNeme, "r")
        lineNum = 1
        self.tokenList = list()
        sent=inputFile.readline()
        while(sent !=""):
            self.processLine(sent, lineNum)
            lineNum+=1
            sent=inputFile.readline()
        self.tokenList.append(Token("EOS", lineNum, 1, TokenType.EOS_TOK))
        inputFile.close()


    def processLine(self, line, lineNum):
        assert line != None
        index = 0
        index = self.skip_white_space(line, index)
        if("\n" in line):
            length=len(line)-1
        else:
            length=len(line)
        while(index < length):
            lexeme = self.getLexeme(line, index, lineNum)
            tokType = self.getTokenType (lexeme, lineNum, index + 1)
            self.tokenList.append(Token (lexeme, lineNum, index + 1, tokType))
            index+=len(lexeme)
            index = self.skip_white_space(line, index)

    def getTokenType(self, lexeme, lineNum, columnNum):
        assert lexeme != None
        assert len(lexeme) > 0
        assert lineNum >= 1
        assert columnNum >= 1
        tokType = TokenType.EOS_TOK
        lexeme = lexeme.lower()
        if(lexeme[0:1].isalpha()):
            if(len(lexeme)==1):
                tokType = TokenType.ID_TOK
            else:
                if(lexeme=="feature"):
                    tokType = TokenType.FEATURE_TOK
                elif(lexeme=="end"):
                    tokType = TokenType.END_TOK
                elif(lexeme=="if"):
                    tokType = TokenType.IF_TOK
                elif(lexeme=="print"):
                    tokType = TokenType.PRINT_TOK
                elif(lexeme=="loop"):
                    tokType = TokenType.LOOP_TOK
                elif(lexeme=="until"):
                    tokType = TokenType.UNTIL_TOK
                elif(lexeme=="from"):
                    tokType = TokenType.FROM_TOK
                elif(lexeme=="is"):
                    tokType = TokenType.IS_TOK
                elif(lexeme=="do"):
                    tokType = TokenType.DO_TOK
                elif(lexeme=="else"):
                    tokType = TokenType.ELSE_TOK
                elif(lexeme=="then"):
                    tokType = TokenType.THEN_TOK
                else:
                    raise LexException("invalid lexeme at ", lineNum, columnNum)
        elif(lexeme[0:1].isdigit()):
            i=0
            while(i<len(lexeme) and lexeme[0:1].isdigit()):
                i+=1
            if(i == len(lexeme)):
                tokType = TokenType.LIT_INT_TOK
            else:
                raise LexException("invalid integer constant", lineNum, columnNum)
        else:
                if(lexeme=="("):
                    tokType = TokenType.LEFT_PAREN_TOK
                elif(lexeme==")"):
                    tokType = TokenType.RIGHT_PAREN_TOK
                elif(lexeme==":="):
                    tokType = TokenType.ASSIGN_TOK
                elif(lexeme=="<="):
                    tokType = TokenType.LE_TOK
                elif(lexeme=="<"):
                    tokType = TokenType.LE_TOK
                elif(lexeme==">="):
                    tokType = TokenType.GE_TOK
                elif(lexeme==">"):
                    tokType = TokenType.GT_TOK
                elif(lexeme=="="):
                    tokType = TokenType.EQ_TOK
                elif(lexeme=="/="):
                    tokType = TokenType.NE_TOK
                elif(lexeme=="+"):
                    tokType = TokenType.ADD_TOK
                elif(lexeme=="-"):
                    tokType = TokenType.SUB_TOK
                elif(lexeme=="*"):
                    tokType = TokenType.MUL_TOK
                elif(lexeme=="/"):
                    tokType = TokenType.DIV_TOK
                else:
                    print(lexeme)
                    raise LexException("invalid lexeme", lineNum, columnNum)
        return tokType

    def getLexeme(self, line, index, lineNum):
        assert line != None
        assert index >= 0
        assert lineNum > 0
        i = index
        if("\n" in line):
            length=len(line)-1
        else:
            length=len(line)
        while(i< length and  " "!= line[i:i+1]):
            i=i+1
        return line[index:i]


    def skip_white_space(self, line, index):
        assert line !=None
        assert index >= 0
        while(index< len(line) and  line[index:index+1].isspace()):
            index=index+1
        return index

    def getNextToken(self):
        if(len(self.tokenList)==0):
            raise RuntimeError("no more tokens")
        return self.tokenList.pop(0)

    def getLookaheadToken(self):
        if(len(self.tokenList)==0):
            raise RuntimeError("no more tokens")
        return self.tokenList[0]


