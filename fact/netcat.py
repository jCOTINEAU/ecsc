import socket
import base64
import re
import math
class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = b''
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 1024):

        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)
 
    def read_until(self, data):

        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)
 
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
 
        return rval
 
    def write(self, data):

        self.socket.send(data)
    
    def close(self):
        self.socket.close()


p = re.compile('.* ([0-9]+)!.*')
nextR = re.compile('.*zeros.*')
nextR2 = re.compile('.*What are.*')
nextI = re.compile('.*the(.*)last.*')
dCap = re.compile(' (\d+) ')
deleteZ = re.compile('(.*[1-9])0+$')
foundDig = re.compile('.* (\d+)!')
nc = Netcat('challenges.ecsc-teamfrance.fr', 3000)
output = nc.read_until(b">>")
print(output)

# start a new note
nc.write(b"720" + b'\n')
qr=nc.read_until(b">>")
print(qr)
nc.write(b"4" + b'\n')

while 1<2:
    print('entering loop')
    dem = nc.read(3)
    print(dem)

    cap = nc.read_until(b">>")
    print(cap)
    sCap = str(cap,"utf-8")
    if nextR.match(sCap) or nextR2.match(sCap):
        print("entering next step")
        splited = sCap.splitlines()
        toSearch = splited[-2]
        m = nextI.match(toSearch)
        print("has been splited"+toSearch)
        i=-1
        if len(m.group(1))==1:
            i = 1
        else:
            m = dCap.match(m.group(1))
            i=int(m.group(1))
        print("last"+str(i))
        m = foundDig.match(toSearch)
        fac = int(m.group(1))
        print("calculating fact of "+str(fac))
        r = 1
        for i in range (1,fac+1):
            r=(r*i)%1000000
        #r = math.factorial(fac)
        strr=str(r)
        m = deleteZ.match(strr)
        if len(m.groups())>=2:
            strr=m.group(1)
        else:
            print("no empty 0")
        strr = strr[-i:]
        print("rez is "+strr)
        nc.write(bytes(strr,"utf-8")+b'\n')
    else:    
        m = p.match(cap.decode("utf-8"))
        print(m.groups())
        i =int(m.group(1))
        r = math.factorial(i)
        strr = str(r)
        strr = strr[-1:]
        print("strtruncated"+strr)
        nc.write(bytes(strr,"utf-8")+b'\n')

    


