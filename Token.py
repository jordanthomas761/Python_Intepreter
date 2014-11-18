__author__ = 'BIWMac'

class Token(object):
    '''
    classdocs
    '''


    def __init__(self, lexeme, rowNumber, columnNumber, tok):
        '''
        @param lexeme - cannot be null & cannot be empty
        @param rowNumber - must be >= 1
        @param columnNumber - must be >= 1
        '''
        if (lexeme == None or len(lexeme) == 0):
            raise ValueError("invalid lexeme")
        if (rowNumber <= 0):
            raise ValueError("invalid row number")
        if ( columnNumber <= 0):
            raise ValueError("invalid column number")
        self.lexeme = lexeme
        self.rowNum = rowNumber
        self.columnNum = columnNumber
        self.tok = tok


    def getLexeme(self):
        return self.lexeme

    def getRowNum(self):
        return self.rowNum

    def getColumnNum(self):
        return self.columnNum

    def getTokenType(self):
        return self.tok

    def __str__(self):
        return str(self.tok) + ": " + str(self.lexeme) + " row: " + str(self.lineNum) + " column: " + str(self.columnNum)
