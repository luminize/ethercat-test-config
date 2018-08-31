from machinekit import rtapi as rt
from machinekit import hal
import os
import time


def instantiate_threads(arguments):
    print('instantiating thread(s)')
    cycletime = arguments.cycle
    rt.newthread('veryfast', 50000)
    rt.newthread('st', int(cycletime), fp=True)


def setup_lcec(configfile=None):
    # load ethercat config parser
    print('lcec_conf %s' % configfile)
    hal.loadusr('lcec_conf %s' % configfile, wait=True)
    # load ethercat realtime module
    rt.loadrt('lcec')


def instantiate_components(arguments):
    configfile = arguments.config
    # name of the servothread
    st = 'st'
    print('instantiating components')
    setup_lcec(configfile)
    # write lcec-read-all first
    hal.addf('lcec.0.read', st)
    # write lcec-write-all last
    hal.addf('lcec.0.write', st)
    # start threads for executing functions
    hal.start_threads()
