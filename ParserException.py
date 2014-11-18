__author__ = 'Jordan Thomas'

class ParserException(Exception):
    '''
    classdocs
    '''


    def __init__(self, message, rowNum, columnNum):
        '''
        Constructor
        '''
        if(message == None):
            raise ValueError("null message argument")
        self.message = message
        if(rowNum<=0):
            raise ValueError("invalid row number argument")
        self.rowNum = rowNum
        if(columnNum<=0):
            raise ValueError("invalid column number argument")
        self.columnNum = columnNum

    def __str__(self):
        return self.message + " at row " + str(self.rowNum) + " column " + str(self.columnNum)