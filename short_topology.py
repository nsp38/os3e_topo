
"""
Mininet topology from OS3E data, shortened so learning switches can be used
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import Node
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

import math


class OS3ETopo(Topo):
    
    def __init__(self, **opts):

        Topo.__init__(self, **opts)

        # Nodes (10)
        Sunnyvale = self.addSwitch('s0')
        Chicago = self.addSwitch('s1')
        Vancouver = self.addSwitch('s2')
        Los_Angeles = self.addSwitch('s3')
        Missoula = self.addSwitch('s4')
        Tucson = self.addSwitch('s5')
        Minneapolis = self.addSwitch('s6')
        Salt_Lake_City = self.addSwitch('s7')
        Portland = self.addSwitch('s8')
        Seattle = self.addSwitch('s9')

        # Single host for each node
        Sunnyvale_host = self.addHost('h0')
        Chicago_host = self.addHost('h1')
        Vancouver_host = self.addHost('h2')
        Los_Angeles_host = self.addHost('h3')
        Missoula_host = self.addHost('h4')
        Tucson_host = self.addHost('h5')
        Minneapolis_host = self.addHost('h6')
        Salt_Lake_City_host = self.addHost('h7')
        Portland_host = self.addHost('h8')
        Seattle_host = self.addHost('h9')

        # Connect Nodes/Hosts
        self.addLink(Sunnyvale, Sunnyvale_host)
        self.addLink(Chicago, Chicago_host)
        self.addLink(Vancouver, Vancouver_host)
        self.addLink(Los_Angeles, Los_Angeles_host)
        self.addLink(Missoula, Missoula_host)
        self.addLink(Tucson, Tucson_host)
        self.addLink(Minneapolis, Minneapolis_host)
        self.addLink(Salt_Lake_City, Salt_Lake_City_host)
        self.addLink(Portland, Portland_host)
        self.addLink(Seattle, Seattle_host)

        # Edges
        self.addLink(Vancouver, Seattle, bw=1, delay=getDelay(49.260440, -123.114034, 47.603560, -122.329439))
        self.addLink(Seattle, Missoula, bw=1, delay=getDelay(47.603560, -122.329439, 46.872780, -113.996234))
        self.addLink(Missoula, Minneapolis, bw=1, delay=getDelay(46.872780, -113.996234, 44.979035, -93.264929))
        self.addLink(Minneapolis, Chicago, bw=1, delay=getDelay(44.979035, -93.264929, 41.884150, -87.632409))
        self.addLink(Seattle, Salt_Lake_City, bw=1, delay=getDelay(47.603560, -122.329439, 40.759505, -111.888229))
        self.addLink(Seattle, Portland, bw=1, delay=getDelay(47.603560, -122.329439, 45.511795, -122.675629))
        self.addLink(Portland, Sunnyvale, bw=1, delay=getDelay(45.511795, -122.675629, 37.371612, -122.038258))
        self.addLink(Sunnyvale, Los_Angeles, bw=1, delay=getDelay(37.371612, -122.038258, 34.053490, -118.245319))
        self.addLink(Los_Angeles, Tucson, bw=1, delay=getDelay(34.053490, -118.245319, 32.221553, -110.969754))

topos = { 'generated': ( lambda: OS3ETopo() ) }

# Calculates and returns delay (latency due to geographical distance) for an edge. Equation is from Assessing-Mininet project/paper.
# Inputs: (latitude of first node, longitude of first node, latitude of second node, longitude of second node)
def getDelay(la1, lo1, la2, lo2):
    first_product = math.sin(float(la1)) * math.sin(float(la2))
    second_product_first_part = math.cos(float(la1)) * math.cos(float(la2))
    second_product_second_part = math.cos((float(lo2)) - (float(lo1)))
    distance = math.radians(math.acos(first_product + (second_product_first_part * second_product_second_part))) * 6378.137
    delay = "'" + (str((distance * 1000) / 197000)) + "ms'"
    return delay

def setupNetwork(controller_ip):
    "Create network and run simple performance test"
    # check if remote controller's ip was set
    # else set it to localhost
    topo = OS3ETopo()
    if controller_ip == '':
        #controller_ip = '10.0.2.2';
        controller_ip = '127.0.0.1';
    net = Mininet(topo=topo, controller=lambda a: RemoteController( a, ip='127.0.0.1', port=6633 ), host=CPULimitedHost, link=TCLink)
    return net

def connectToRootNS( network, switch, ip, prefixLen, routes ):
    "Connect hosts to root namespace via switch. Starts network."
    "network: Mininet() network object"
    "switch: switch to connect to root namespace"
    "ip: IP address for root namespace node"
    "prefixLen: IP address prefix length (e.g. 8, 16, 24)"
    "routes: host networks to route to"
    # Create a node in root namespace and link to switch 0
    root = Node( 'root', inNamespace=False )
    intf = TCLink( root, switch ).intf1
    root.setIP( ip, prefixLen, intf )
    # Start network that now includes link to root namespace
    network.start()
    # Add routes from root ns to hosts
    for route in routes:
        root.cmd( 'route add -net ' + route + ' dev ' + str( intf ) )

def sshd( network, cmd='/usr/sbin/sshd', opts='-D' ):
    "Start a network, connect it to root ns, and run sshd on all hosts."
    switch = network.switches[ 0 ]  # switch to use
    ip = '10.123.123.1'  # our IP address on host network
    routes = [ '10.0.0.0/8' ]  # host networks to route to
    connectToRootNS( network, switch, ip, 8, routes )
    for host in network.hosts:
        host.cmd( cmd + ' ' + opts + '&' )

    # DEBUGGING INFO
    print
    print "Dumping host connections"
    dumpNodeConnections(network.hosts)
    print
    print "*** Hosts are running sshd at the following addresses:"
    print
    for host in network.hosts:
        print host.name, host.IP()
    print
    print "*** Type 'exit' or control-D to shut down network"
    print
    print "*** For testing network connectivity among the hosts, wait a bit for the controller to create all the routes, then do 'pingall' on the mininet console."
    print

    CLI( network )
    for host in network.hosts:
        host.cmd( 'kill %' + cmd )
    network.stop()


if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    sshd( setupNetwork('127.0.0.1') )
