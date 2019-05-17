import socket
import base64
import re
import math
import numpy as np
from math import log
def prime_range(a=1,n=1000):
    """ Return a list of the primes between a and n. """
    prime = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[p*p//3 :: 2*p] = False
            prime[p*(p - 2*(i&1) + 4)//3 :: 2*p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    i=0
    while result[i] < a:
        i += 1
    return np.r_[2, result[i:]]

def factGood(n):
    primes = prime_range(n=n+1)
    prime_count = n // primes
    for j in range(len(primes)):
        for i in range(2,int(log(n,primes[j]))+1):
            prime_count[j] += n // (primes[j]**i)
    prime_count[0] -= prime_count[2]
    prime_count[2] = 0

    ans = 1
    #print(prime_count)
    for p1, p2 in zip(primes,prime_count):
        ans = (ans * pow(int(p1),int(p2), base**5)) % (base**5)
    return ans

base = 10


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
nextR2 = re.compile('.*t are.*')
nextI = re.compile('.*the(.*)last.*')
dCap = re.compile(' (\d+) ')
foundDig = re.compile('.* (\d+)!')
nc = Netcat('challenges.ecsc-teamfrance.fr', 3000)
output = nc.read_until(b">>")
print(output)
def facc(n):
    if n==1:
        return n
    return n*facc(n-1)

# start a new note
nc.write(b"720" + b'\n')
qr=nc.read_until(b">>")
print(qr)
nc.write(b"4" + b'\n')

while 1<2:
    #print('entering loop')
    dem = nc.read(3)
    print(dem)

    cap = nc.read_until(b">>")
    #print(cap)
    sCap = str(cap,"utf-8")
    if nextR.match(sCap) or nextR2.match(sCap):
        #print("entering next step")
        splited = sCap.splitlines()
        toSearch = splited[-2]
        m = nextI.match(toSearch)
        #print("has been splited"+toSearch)
        i=-1
        if len(m.group(1))==1:
            i = 1
        else:
            m = dCap.match(m.group(1))
            i=int(m.group(1))
        #print("last"+str(i))
        m = foundDig.match(toSearch)
        fac = int(m.group(1))
        print("calculating fact of "+str(fac))
        r = factGood(fac)
        strr=str(r)
        #print("factorial is"+strr) 
        strr = strr[-i:]

        


        print("rez is "+strr)
        nc.write(bytes(strr,"utf-8")+b'\n')
    else:    
        m = p.match(cap.decode("utf-8"))
        #print(m.groups())
        i =int(m.group(1))
        r = math.factorial(i)
        strr = str(r)
        strr = strr[-1:]
        #print("strtruncated"+strr)
        nc.write(bytes(strr,"utf-8")+b'\n')

    


