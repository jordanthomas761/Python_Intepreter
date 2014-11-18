__author__ = 'Jordan Thomas'

from Compound import Compound

class Feature(object):
    '''
    classdocs
    '''


    def __init__(self, comp):
        '''
        Constructor
        '''
        if(comp == None):
            raise ValueError("null statement list argument")
        self.comp=comp

    def execute(self):
        self.comp.execute()