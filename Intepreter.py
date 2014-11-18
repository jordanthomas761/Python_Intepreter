__author__ = 'Jordan Thomas'
"""
Class: CS 4150
Date: October 30, 2014
"""

from Parser import Parser
from LexException import LexException
from ParserException import ParserException
if __name__ == '__main__':
    try:
        f= Parser("test4.e.txt")
        feat = f.parse()
        feat.execute()
    except LexException as e:
        print(str(e))
    except ParserException as e:
        print(str(e))
    except Exception as e:
        print(str(e))