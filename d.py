
"""
Mininet topology for OS3E 
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
        El_Paso = self.addSwitch('s0')
        Denver = self.addSwitch('s1')
        Vancouver = self.addSwitch('s2')
        Baton_Rouge = self.addSwitch('s3')
        Albuquerque = self.addSwitch('s4')
        Jacksonville = self.addSwitch('s5')
        Miami = self.addSwitch('s6')
        Houston = self.addSwitch('s7')
        Salt_Lake_City = self.addSwitch('s8')
        Seattle = self.addSwitch('s9')
		
        # Single host for each node
        El_Paso_host = self.addHost('h0', ip='0.0.0.0')
        Denver_host = self.addHost('h1', ip='0.0.0.0')
        Vancouver_host = self.addHost('h2', ip='0.0.0.0')
        Baton_Rouge_host = self.addHost('h3', ip='0.0.0.0')
        Albuquerque_host = self.addHost('h4', ip='0.0.0.0')
        Jacksonville_host = self.addHost('h5', ip='0.0.0.0')
        Miami_host = self.addHost('h6', ip='0.0.0.0')
        Houston_host = self.addHost('h7', ip='0.0.0.0')
        Salt_Lake_City_host = self.addHost('h8', ip='0.0.0.0')
        Seattle_host = self.addHost('h9', ip='0.0.0.0')

        # Connect Nodes/Hosts
        self.addLink(El_Paso, El_Paso_host)
        self.addLink(Denver, Denver_host)
        self.addLink(Vancouver, Vancouver_host)
        self.addLink(Baton_Rouge, Baton_Rouge_host)
        self.addLink(Albuquerque, Albuquerque_host)
        self.addLink(Jacksonville, Jacksonville_host)
        self.addLink(Miami, Miami_host)
        self.addLink(Houston, Houston_host)
        self.addLink(Salt_Lake_City, Salt_Lake_City_host)
        self.addLink(Seattle, Seattle_host)
		
        # Edges
        self.addLink(Vancouver, Seattle, bw=1, delay=getDelay(49.260440, -123.114034, 47.603560, -122.329439))
        self.addLink(Seattle, Salt_Lake_City, bw=1, delay=getDelay(47.603560, -122.329439, 40.759505, -111.888229))
        self.addLink(Salt_Lake_City, Denver, bw=1, delay=getDelay(40.759505, -111.888229, 39.740010, -104.992259))
        self.addLink(Denver, Albuquerque, bw=1, delay=getDelay(39.740010, -104.992259, 35.084180, -106.648639))
        self.addLink(Albuquerque, El_Paso, bw=1, delay=getDelay(35.084180, -106.648639, 31.759165, -106.487494))
        self.addLink(El_Paso, Houston, bw=1, delay=getDelay(31.759165, -106.487494, 29.760450, -95.369784))
        self.addLink(Houston, Baton_Rouge, bw=1, delay=getDelay(29.760450, -95.369784, 30.443335, -91.186994))
        self.addLink(Baton_Rouge, Jacksonville, bw=1, delay=getDelay(30.443335, -91.186994, 30.331380, -81.655799))
        self.addLink(Jacksonville, Miami, bw=1, delay=getDelay(30.331380, -81.655799, 25.728985, -80.237419))
		
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
