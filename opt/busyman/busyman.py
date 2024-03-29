#!/usr/bin/env python3
# copyrights Visaroy
# usage: busy <action> [--option="argument"]
#
from __future__ import print_function
import pyautogui, time, sys, math, random, os, getopt, numpy, imutils, cv2, inspect, yaml
from time import sleep
from busymanConfig import *
#global verbose

def options(argv):
    verbose = 'true'
    place = ''
    destination = ''
    privacy = ''
    recipient = ''
    try:
        opts, args = getopt.getopt(argv,"hv:p:d:P:r:",["help","verbose=","place=","destination=","privacy=","recipient="])
    except getopt.GetoptError:
        print (error, 'usage: busy <action> [--option="argument"]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (info, '--help: usage: busy <action> [--option="argument"]')
            sys.exit()
        elif opt in ("-V", "--verbose"):
            verbose = arg
        elif opt in ("-p", "--place"):
            place = arg
        elif opt in ("-d", "--destination"):
            destination = arg
        elif opt in ("-P", "--privacy"):
            privacy = arg
        elif opt in ("-r", "--recipient"):
            recipient = arg
    if verbose == "true":
        print (info, "read options...")
    return verbose, place, destination, privacy, recipient

verbose, place, destination, privacy, recipient = options(sys.argv[1:])
print ("\t options: verbose=",verbose)

if verbose == None:
    verbose = "false"

def default():
    print ("\t",func_name, (inspect.currentframe().f_code.co_name))

def status():
    bashCommand = "screen -ls"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

try:
#https://stackoverflow.com/questions/2831597/processing-command-line-arguments-in-prefix-notation-in-python
#    default()
    for x in sys.argv:
        print ("Argument: ", x)
    if verbose == "true":
        print ("verbose=",verbose)
        print (success, "done:\n",func_name, (inspect.currentframe().f_code.co_name))
#    sys.stdout.write("\n")
    sys.exit(0)
except KeyboardInterrupt:
    print('\n')
