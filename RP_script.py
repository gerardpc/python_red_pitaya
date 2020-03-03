"""
###############################################################################
COMMUNICATION WITH Red Pitaya

CONTACT: 
gerardpc@gmail.com, irene.alda@icfo.eu
###############################################################################
UPDATE HISTORY:
    
Created on 18.3.2019 by Gerard Planes Conangla & Irene Alda Ferrero
Last update: 3.4.2019 by Gerard Planes Conangla
###############################################################################
"""
# Import modules
import time # for sleep() 
import RP_lib # custom laser library

###############################################################################
# STARTING ROUTINES
print "#############################################################"
print "Starting routine.\n"

# CONNECT TO RED PITAYA
# Photodiode intensity (i.e. feedback signal) is connected to RP input 2. 
# Connect to Red pitaya through ssh and get value of IN2 voltage register 

# Connection parameters
ip = '192.168.1.3' # this value depends on RP I.P. of course
port = 22 # default ssh port
username = 'root' # RP user
password = 'root' # RP password

# Establish connection
RP_client = laser_lib.RP_connect(ip, port, username, password)

################################################################################
## Main part
################################################################################
# Do some stuff. For instance:

int_1 = RP_lib.RP_get_intensity(RP_client)
    
# End of the main part
################################################################################
# ENDING ROUTINES

# Terminate connections
# Disconnect RP
RP_lib.RP_disconnect(RP_client)



















