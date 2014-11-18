__author__ = 'Jordan Thomas'

import abc

class Statement(object):
    '''
    classdocs
    '''

    @abc.abstractmethod
    def __init__(self):
        '''
        Constructor
        '''

    @abc.abstractmethod
    def execute(self):
        return