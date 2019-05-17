import socket
import base64
import zlib, sys
import io
from PIL import ImageOps
from PIL import Image
import re
from pyzbar.pyzbar import decode

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


nc = Netcat('challenges.ecsc-teamfrance.fr', 3001)
output = nc.read_until(b">>")

# start a new note
nc.write(b'Y' + b'\n')
print(output)
qr=nc.read_until(b"==")
decoded=base64.b64decode(qr)
dzlib = zlib.decompress(decoded)
end = nc.read_until(b">>")
print("answer"+str(end))
img = Image.open(io.BytesIO(dzlib))
t=0
for i in range (0,2320,290):
    for z in range (0,2320,290):
        area=(i,z,i+290,z+290)
        cropped_img = img.crop(area)
        data = decode(cropped_img)
        t+=(int(data[0][0]))

strr = str(t)
nc.write(bytes(strr,"utf-8")+b"\n")
end = nc.read(4000)
print(end)



