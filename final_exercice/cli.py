'''
This codes the command line interface
'''

###Standard library
import argparse


def command_line():
    '''
    This function codes the command line interface of the program.

    Parameters
    ----------
    None

    Return
    ------
    args	NameSpace
		with argument analysis

    '''
    ###Create the parser object
    parser = argparse.ArgumentParser(description='This program is an example of command line',
 				                     epilog='Author: R. Thomas, 2024, UoS')

    ###Add argument
    parser.add_argument('--config', type=str, help='Takes a configuration file as value')
    parser.add_argument('--save', action='store_true', help='To save the configuration on disk')
    parser.add_argument('--timestamp', type=float,
                                       help='Delta time of the simulation (override the conf file)')

    args = parser.parse_args()
    return args
