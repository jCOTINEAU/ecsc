import socket
import base64
import re
import math
import numpy as np
from math import log
import bisect
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

def factGood(n,primes,detail):
    #primes = prime_range(n=n+1)
    prime_count = n // primes
    for j in range(len(primes)):
        for i in range(2,int(log(n,primes[j]))+1):
            prime_count[j] += n // (primes[j]**i)
    prime_count[0] -= prime_count[2]
    prime_count[2] = 0

    ans = 1
    #print(prime_count)
    for p1, p2 in zip(primes,prime_count):
        ans = (ans * pow(int(p1),int(p2), base**detail)) % (base**detail)
    return ans

base = 10

def custF(n):
    t = 1
    for i in range(1,n+1):
        t = (i*t)%10
    return t
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

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i:
        return a[:i]
    raise ValueError



primes = prime_range(n=90000000)

p = re.compile('.* ([0-9]+)!.*')
nextR = re.compile('.*zeros.*')
nextR2 = re.compile('.*t are.*')
nextI = re.compile('.*the(.*)last.*')
dCap = re.compile(' (\d+) ')
foundDig = re.compile('.* (\d+)!')

i=4
fac=11
pp = find_le(primes,fac+1)
r = factGood(fac,pp,2)
strr=str(r)
print(strr)



def pp(k):
    a=[6,2,4,8]
    if k<1:
        return 1
    return a[k%4]

def ll(n):
    a =[1,1,2,6,4]
    if n<5:
        return a[n]
    return(pp(n//5)*ll(n//5)*ll(n%5))%10

print(ll(fac))    

    


