__author__ = 'BIWMac'

class LexException(Exception):
    def __init__(self, message, lineNum, columnNum):
        '''
        Constructor
        '''
        if(message == None):
            raise ValueError("null string argument")
        self.message = message
        if(lineNum<=0):
            raise ValueError("invalid line number argument")
        self.lineNum = lineNum
        if(columnNum<=0):
            raise ValueError("invalid column number argument")
        self.columnNum = columnNum

    def __str__(self):
        return self.message + " Line: " + str(self.lineNum) + " Row:" + str(self.lineNum)
