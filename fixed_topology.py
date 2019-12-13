
"""
Custom topology for Mininet
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


class GeneratedTopo(Topo):

    def getDelay(la1, lo1, la2, lo2):
        first_product               = math.sin(float(la1)) * math.sin(float(la2))
        second_product_first_part   = math.cos(float(la1)) * math.cos(float(la2))
        second_product_second_part  = math.cos((float(lo2)) - (float(lo1)))
        distance = math.radians(math.acos(first_product + (second_product_first_part * second_product_second_part))) * 6378.137
        # t (in ms) = ( distance in km * 1000 (for meters) ) / ( speed of light / 1000 (for ms))
        # t         = ( distance       * 1000              ) / ( 1.97 * 10**8   / 1000         )
        delay = "'" + (str((distance * 1000) / 197000)) + "ms'"
        return delay
    
    def __init__(self, **opts):
        "Create a topology."

        # Initialize Topology
        Topo.__init__(self, **opts)

        # add nodes, switches first...
        Sunnyvale = self.addSwitch('s0')
        Nashville = self.addSwitch('s1')
        Raleigh = self.addSwitch('s2')
        Chicago = self.addSwitch('s3')
        El_Paso = self.addSwitch('s4')
        Denver = self.addSwitch('s5')
        Dallas = self.addSwitch('s6')
        Louisville = self.addSwitch('s7')
        Vancouver = self.addSwitch('s8')
        Washington_DC = self.addSwitch('s9')
        Indianapolis = self.addSwitch('s10')
        Pittsburgh = self.addSwitch('s11')
        Baton_Rouge = self.addSwitch('s12')
        Albuquerque = self.addSwitch('s13')
        Los_Angeles = self.addSwitch('s14')
        Atlanta = self.addSwitch('s15')
        Memphis = self.addSwitch('s16')
        Jacksonville = self.addSwitch('s17')
        Miami = self.addSwitch('s18')
        Kansas_City = self.addSwitch('s19')
        Missoula = self.addSwitch('s20')
        Philadelphia = self.addSwitch('s21')
        Tucson = self.addSwitch('s22')
        Buffalo = self.addSwitch('s23')
        Houston = self.addSwitch('s24')
        Boston = self.addSwitch('s25')
        Minneapolis = self.addSwitch('s26')
        New_York = self.addSwitch('s27')
        Salt_Lake_City = self.addSwitch('s28')
        Cleveland = self.addSwitch('s29')
        Jackson = self.addSwitch('s30')
        Portland = self.addSwitch('s31')
        Seattle = self.addSwitch('s32')
        Ashburn = self.addSwitch('s33')

        # ... and now hosts
        Sunnyvale_host = self.addHost('h0')
        Nashville_host = self.addHost('h1')
        Raleigh_host = self.addHost('h2')
        Chicago_host = self.addHost('h3')
        El_Paso_host = self.addHost('h4')
        Denver_host = self.addHost('h5')
        Dallas_host = self.addHost('h6')
        Louisville_host = self.addHost('h7')
        Vancouver_host = self.addHost('h8')
        Washington_DC_host = self.addHost('h9')
        Indianapolis_host = self.addHost('h10')
        Pittsburgh_host = self.addHost('h11')
        Baton_Rouge_host = self.addHost('h12')
        Albuquerque_host = self.addHost('h13')
        Los_Angeles_host = self.addHost('h14')
        Atlanta_host = self.addHost('h15')
        Memphis_host = self.addHost('h16')
        Jacksonville_host = self.addHost('h17')
        Miami_host = self.addHost('h18')
        Kansas_City_host = self.addHost('h19')
        Missoula_host = self.addHost('h20')
        Philadelphia_host = self.addHost('h21')
        Tucson_host = self.addHost('h22')
        Buffalo_host = self.addHost('h23')
        Houston_host = self.addHost('h24')
        Boston_host = self.addHost('h25')
        Minneapolis_host = self.addHost('h26')
        New_York_host = self.addHost('h27')
        Salt_Lake_City_host = self.addHost('h28')
        Cleveland_host = self.addHost('h29')
        Jackson_host = self.addHost('h30')
        Portland_host = self.addHost('h31')
        Seattle_host = self.addHost('h32')
        Ashburn_host = self.addHost('h33')

        # add edges between switch and corresponding host
        self.addLink(Sunnyvale, Sunnyvale_host)
        self.addLink(Nashville, Nashville_host)
        self.addLink(Raleigh, Raleigh_host)
        self.addLink(Chicago, Chicago_host)
        self.addLink(El_Paso, El_Paso_host)
        self.addLink(Denver, Denver_host)
        self.addLink(Dallas, Dallas_host)
        self.addLink(Louisville, Louisville_host)
        self.addLink(Vancouver, Vancouver_host)
        self.addLink(Washington_DC, Washington_DC_host)
        self.addLink(Indianapolis, Indianapolis_host)
        self.addLink(Pittsburgh, Pittsburgh_host)
        self.addLink(Baton_Rouge, Baton_Rouge_host)
        self.addLink(Albuquerque, Albuquerque_host)
        self.addLink(Los_Angeles, Los_Angeles_host)
        self.addLink(Atlanta, Atlanta_host)
        self.addLink(Memphis, Memphis_host)
        self.addLink(Jacksonville, Jacksonville_host)
        self.addLink(Miami, Miami_host)
        self.addLink(Kansas_City, Kansas_City_host)
        self.addLink(Missoula, Missoula_host)
        self.addLink(Philadelphia, Philadelphia_host)
        self.addLink(Tucson, Tucson_host)
        self.addLink(Buffalo, Buffalo_host)
        self.addLink(Houston, Houston_host)
        self.addLink(Boston, Boston_host)
        self.addLink(Minneapolis, Minneapolis_host)
        self.addLink(New_York, New_York_host)
        self.addLink(Salt_Lake_City, Salt_Lake_City_host)
        self.addLink(Cleveland, Cleveland_host)
        self.addLink(Jackson, Jackson_host)
        self.addLink(Portland, Portland_host)
        self.addLink(Seattle, Seattle_host)
        self.addLink(Ashburn, Ashburn_host)

        # add edges between switches
        self.addLink(Vancouver, Seattle, bw=1, delay=getDelay(49.260440, -123.114034, 47.603560, -122.329439))
        self.addLink(Seattle, Missoula, bw=1, delay=getDelay(47.603560, -122.329439, 46.872780, -113.996234))
        self.addLink(Missoula, Minneapolis, bw=1, delay=getDelay(46.872780, -113.996234, 44.979035, -93.264929))
        self.addLink(Minneapolis, Chicago, bw=1, delay=getDelay(44.979035, -93.264929, 41.884150, -87.632409))
        self.addLink(Seattle, Salt_Lake_City, bw=1, delay=getDelay(47.603560, -122.329439, 40.759505, -111.888229))
        self.addLink(Seattle, Portland, bw=1, delay=getDelay(47.603560, -122.329439, 45.511795, -122.675629))
        self.addLink(Portland, Sunnyvale, bw=1, delay=getDelay(45.511795, -122.675629, 37.371612, -122.038258))
        self.addLink(Sunnyvale, Salt_Lake_City, bw=1, delay=getDelay(37.371612, -122.038258, 40.759505, -111.888229))
        self.addLink(Sunnyvale, Los_Angeles, bw=1, delay=getDelay(37.371612, -122.038258, 34.053490, -118.245319))
        self.addLink(Los_Angeles, Salt_Lake_City, bw=1, delay=getDelay(34.053490, -118.245319, 40.759505, -111.888229))
        self.addLink(Los_Angeles, Tucson, bw=1, delay=getDelay(34.053490, -118.245319, 32.221553, -110.969754))
        self.addLink(Tucson, El_Paso, bw=1, delay=getDelay(32.221553, -110.969754, 31.759165, -106.487494))
        self.addLink(Salt_Lake_City, Denver, bw=1, delay=getDelay(40.759505, -111.888229, 39.740010, -104.992259))
        self.addLink(Denver, Albuquerque, bw=1, delay=getDelay(39.740010, -104.992259, 35.084180, -106.648639))
        self.addLink(Albuquerque, El_Paso, bw=1, delay=getDelay(35.084180, -106.648639, 31.759165, -106.487494))
        self.addLink(Denver, Kansas_City, bw=1, delay=getDelay(39.740010, -104.992259, 39.102960, -94.583062))
        self.addLink(Kansas_City, Chicago, bw=1, delay=getDelay(39.102960, -94.583062, 41.884150, -87.632409))
        self.addLink(Kansas_City, Dallas, bw=1, delay=getDelay(39.102960, -94.583062, 32.778155, -96.795404))
        self.addLink(Dallas, Houston, bw=1, delay=getDelay(32.778155, -96.795404, 29.760450, -95.369784))
        self.addLink(El_Paso, Houston, bw=1, delay=getDelay(31.759165, -106.487494, 29.760450, -95.369784))
        self.addLink(Houston, Jackson, bw=1, delay=getDelay(29.760450, -95.369784, 32.298690, -90.180489))
        self.addLink(Jackson, Memphis, bw=1, delay=getDelay(32.298690, -90.180489, 35.149680, -90.048929))
        self.addLink(Memphis, Nashville, bw=1, delay=getDelay(35.149680, -90.048929, 36.167783, -86.778365))
        self.addLink(Houston, Baton_Rouge, bw=1, delay=getDelay(29.760450, -95.369784, 30.443335, -91.186994))
        self.addLink(Baton_Rouge, Jacksonville, bw=1, delay=getDelay(30.443335, -91.186994, 30.331380, -81.655799))
        self.addLink(Chicago, Indianapolis, bw=1, delay=getDelay(41.884150, -87.632409, 39.766910, -86.149964))
        self.addLink(Indianapolis, Louisville, bw=1, delay=getDelay(39.766910, -86.149964, 38.254860, -85.766404))
        self.addLink(Louisville, Nashville, bw=1, delay=getDelay(38.254860, -85.766404, 36.167783, -86.778365))
        self.addLink(Nashville, Atlanta, bw=1, delay=getDelay(36.167783, -86.778365, 33.748315, -84.391109))
        self.addLink(Atlanta, Jacksonville, bw=1, delay=getDelay(33.748315, -84.391109, 30.331380, -81.655799))
        self.addLink(Jacksonville, Miami, bw=1, delay=getDelay(30.331380, -81.655799, 25.728985, -80.237419))
        self.addLink(Chicago, Cleveland, bw=1, delay=getDelay(41.884150, -87.632409, 41.504365, -81.690459))
        self.addLink(Cleveland, Buffalo, bw=1, delay=getDelay(41.504365, -81.690459, 42.885440, -78.878464))
        self.addLink(Buffalo, Boston, bw=1, delay=getDelay(42.885440, -78.878464, 42.358635, -71.056699))
        self.addLink(Boston, New_York, bw=1, delay=getDelay(42.358635, -71.056699, 40.714550, -74.007124))
        self.addLink(New_York, Philadelphia, bw=1, delay=getDelay(40.714550, -74.007124, 39.952270, -75.162369))
        self.addLink(Philadelphia, Washington_DC, bw=1, delay=getDelay(39.952270, -75.162369, 38.890370, -77.031959))
        self.addLink(Cleveland, Pittsburgh, bw=1, delay=getDelay(41.504365, -81.690459, 40.438335, -79.997459))
        self.addLink(Pittsburgh, Ashburn, bw=1, delay=getDelay(40.438335, -79.997459, 39.051631, -77.483151))
        self.addLink(Ashburn, Washington_DC, bw=1, delay=getDelay(39.051631, -77.483151, 38.890370, -77.031959))
        self.addLink(Washington_DC, Raleigh, bw=1, delay=getDelay(38.890370, -77.031959, 35.785510, -78.642669))
        self.addLink(Raleigh, Atlanta, bw=1, delay=getDelay(35.785510, -78.642669, 33.748315, -84.391109))

topos = { 'generated': ( lambda: GeneratedTopo() ) }

# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

# the following code produces an executable script working with a remote controller
# and providing ssh access to the the mininet hosts from within the ubuntu vm
controller_ip = '127.0.0.0'

#def getDelay(la1, lo1, la2, lo2):
#    first_product               = math.sin(float(la1)) * math.sin(float(la2))
#    second_product_first_part   = math.cos(float(la1)) * math.cos(float(la2))
#    second_product_second_part  = math.cos((float(lo2)) - (float(lo1)))
#    distance = math.radians(math.acos(first_product + (second_product_first_part * second_product_second_part))) * 6378.137
#    # t (in ms) = ( distance in km * 1000 (for meters) ) / ( speed of light / 1000 (for ms))
#    # t         = ( distance       * 1000              ) / ( 1.97 * 10**8   / 1000         )
#    delay = "'" + (str((distance * 1000) / 197000)) + "ms'"
#    return delay

def setupNetwork(controller_ip):
    "Create network and run simple performance test"
    # check if remote controller's ip was set
    # else set it to localhost
    topo = GeneratedTopo()
    if controller_ip == '':
        #controller_ip = '10.0.2.2';
        controller_ip = '127.0.0.1';
    net = Mininet(topo=topo, controller=lambda a: RemoteController( a, ip=controller_ip, port=6633 ), host=CPULimitedHost, link=TCLink)
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
    sshd( setupNetwork(controller_ip) )
