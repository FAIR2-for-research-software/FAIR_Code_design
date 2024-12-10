'''
This is the main file of the program
'''


###Standard library
import sys


###local imports
import cli
import conf
import simulation

###Call the command line interface
options = cli.command_line()

###if the user does not give a configuration file we quit
if options.config is None:
    print('Please give a configuration file...exit')
    sys.exit()


###If we get there we have a configuration file
config = conf.read_conf(options.config)


###if a timestamp is provided, we change the configuration
if options.timestamp:
    config['time']['time_steps'] = options.timestamp


###instantiate the simulation
Simu = simulation.Simulation(config['Parameters']['l'], config['Parameters']['m'], config['Parameters']['h'])

###Ang get total L+M
print('Total L+M =', Simu.get_total())


###if the user wants to save the file we call the write conf
### function
if options.save:
    conf.write_conf(config, 'final_conf.ini')
