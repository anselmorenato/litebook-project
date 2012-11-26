#-------------------------------------------------------------------------------
# Name:        UPNP Client of miranda
# Purpose:
#
# Author:      Administrator
#
# Created:     30/04/2012
# Copyright:   (c) Administrator 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import miranda
import socket
import platform
MYOS = platform.system()
if MYOS != "Darwin":
    import netifaces
else:
    import netifaces_osx


def insubnet(ip1,mask1,ip2):
    """
    return True if ip2 is in ip1's subnet
    """
    bs1 = socket.inet_aton(ip1)
    bs2 = socket.inet_aton(ip2)
    mask = socket.inet_aton(mask1)
    subnet1=''
    for n in range(4):
        subnet1+=chr(ord(bs1[n]) & ord(mask[n]))
    subnet2=''
    for n in range(4):
        subnet2+=chr(ord(bs2[n]) & ord(mask[n]))
    if subnet1 == subnet2:
        return True
    else:
        return False

def getDRIntIP(gwip):
    """
    return the 1st interface ip that in the the same subnet of gwip
    """
    for ifname in netifaces.interfaces(): #return addr of 1st network interface
        if 2 in netifaces.ifaddresses(ifname):
            if_addr = netifaces.ifaddresses(ifname)[2][0]['addr']
            if if_addr != '127.0.0.1' and if_addr != None and if_addr != '':
                if_mask = netifaces.ifaddresses(ifname)[2][0]['netmask']
                if insubnet(if_addr,if_mask,gwip) == True:
                    return if_addr
    return False

def addUPNPPortMapping(map_list):
    """
    map_list ia a list of following dict:
        {'proto':,'port':}
    """
    #Table of valid commands - all primary commands must have an associated function
    appCommands = {
    		'help' : {
    			'help' : None
    			},
    		'quit' : {
    			'help' : None
    			},
    		'exit' : {
    			'help' : None
    			},
    		'save' : {
    			'data' : None,
    			'info' : None,
    			'help' : None
    			},
    		'load' : {
    			'help' : None
    			},
    		'seti' : {
    			'uniq' : None,
    			'socket' : None,
    			'show' : None,
    			'iface' : None,
    			'debug' : None,
    			'version' : None,
    			'verbose' : None,
    			'help' : None
    			},
    		'head' : {
    			'set' : None,
    			'show' : None,
    			'del' : None,
    			'help': None
    			},
    		'host' : {
    			'list' : None,
    			'info' : None,
    			'get'  : None,
    			'details' : None,
    			'send' : None,
    			'summary' : None,
    			'help' : None
    			},
    		'pcap' : {
    			'help' : None
    			},
    		'msearch' : {
    			'device' : None,
    			'service' : None,
    			'help' : None
    			},
    		'log'  : {
    			'help' : None
    			},
    		'debug': {
    			'command' : None,
    			'help'    : None
    			}
    }

    ##	#The load command should auto complete on the contents of the current directory
    ##        for file in os.listdir(os.getcwd()):
    ##                appCommands['load'][file] = None

    #Initialize upnp class
    hp = miranda.upnp(False,False,None,appCommands);

    ##	#Set up tab completion and command history
    ##	readline.parse_and_bind("tab: complete")
    ##	readline.set_completer(hp.completer.complete)

    #Set some default values
    hp.UNIQ = True
    hp.VERBOSE = False
##    action = False
##    funPtr = False
    #search for host
    try:
        miranda.msearch(2,['service','WANIPConnection'],hp)#return 1st router with portmapping action
    except:
        return False
    found = False
    for index,hostInfo in hp.ENUM_HOSTS.iteritems():
        gwip=hostInfo['name'].split(':')[0]
        found = True
        break
    if found == False: return False
    miranda.host(3,['host','get','0'],hp)#this is needed
    #miranda.host(6,['host', 'send', '0', 'WANConnectionDevice', 'WANIPConnection', 'GetExternalIPAddress'],hp) #get external ip
    try:
        for mapping in map_list:
            miranda.addPortMapping(hp,0,"TestFromScript",getDRIntIP(gwip),mapping['port'],mapping['port'],mapping['proto'])
    except:
        return False
    return True
    #miranda.delPortMapping(hp,0,portnum,proto) #remove the mapping

if __name__ == '__main__':
    addUPNPPortMapping([{'proto':'UDP','port':50200}])
