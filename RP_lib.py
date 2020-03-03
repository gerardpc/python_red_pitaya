"""
RS 232 COMMUNICATION WITH TUNABLE LASER

Created on Mon Mar 18 11:52:15 2019
"""
"""
###############################################################################
# FUNCTIONS DEFINITIONS PROVIDED BY COMPANY
###############################################################################
"""
import serial
import time
import struct
import threading
import numpy
import paramiko
import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')


###############################################################################
###############################################################################
# Gerard new functions
# Red Pitaya functions


# Establish connection
def RP_connect(ip, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port, username, password)
    return client

# Terminate connection
def RP_disconnect(client):
    client.close()

# Get register value
def RP_get_intensity(client):
    cmd_1 = '/root/read_register.o' # command that RP will execute
    stdin, stdout, stderr = client.exec_command(cmd_1)
    # Return register value
    outlines = stdout.readlines()
    register = ''.join(outlines)
    return float(register)

# Get 2 register values
def RP_get_2intensity(client):
    cmd_1 = '/root/read_register.o' # command that RP will execute
    stdin, stdout, stderr = client.exec_command(cmd_1)
    # Return register value
    outlines = stdout.readlines()
    return [float(outlines[0]), float(outlines[1])]














