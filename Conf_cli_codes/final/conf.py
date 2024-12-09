'''
This code the configuration file handling

It implements a function that reads a configuration file
And another one that writes a configuration file
'''

###Standard library
import configparser

def read_conf(file):
    '''
    This function reads the configuration file and
    extract the complete configuration


    Parameters
    ----------
    file		str
		        path to configuration file

    return
    ------
    configuration	dict
                        complete configuration
    '''
    #Create the parser object
    parser = configparser.ConfigParser()

    ##Read the configuration file
    parser.read(file)

    ###convert all the documentation to a dictionary
    configuration = {}
    for section in parser.sections():
        configuration[section] = dict(parser[section])

    return configuration


def write_conf(configuration, filename):
    '''
    This function writes the configuration as an INI file
    in a file

    Parameters
    ----------
    configuration 	dict
			2-level Nested dictionary with a configuration to write
     			first level: section name
                        second level: content of the section


    filename		str
			path to the file we want to save the configuration into


    Return
    ------
    None
    '''


    #Create the parser object
    parser = configparser.ConfigParser()


    ###Put the configuration dictionary in the configuration object
    for section in configuration:
        parser[section] = configuration[section]


    ###save into file
    with open(filename, 'w') as writefile:
        parser.write(writefile)
