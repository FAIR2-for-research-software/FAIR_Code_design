'''
This file codes the simulation object
'''


class Simulation:
    '''
    This class creates the simulation object

    Attributes
    ----------
    l    float
         the L number
    m	 float
         the M number
    h	 float
	     the H number 
    '''

    def __init__(self, l, m, h):
        '''
        Class initialisation

	    Parameters
	    ----------
        l	: float
                  the L number
        m	: float
                  the M number
        h	: float
	          the H number
        '''
        self.l = float(l)
        self.m = float(m)
        self.h = float(h)

    def get_total(self):
        '''
        This compute the sum L + M.
       
        Parameters
        ----------
        None

        Return
        ------
        None
        '''
        return self.l + self.m
        