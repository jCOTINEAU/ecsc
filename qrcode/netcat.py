import socket
import base64
import zlib, sys
from PIL import ImageOps
from PIL import Image
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
print(output)

# start a new note
nc.write(b'Y' + b'\n')
qr=nc.read_until(b"=")
print(qr)
decoded=base64.b64decode(qr)
dzlib = zlib.decompress(decoded)
f = open('qr', 'wb')
f.write(dzlib)
f.close()



# image handling 

#img = Image.open("my_recovered_log_file")

#border = (0, 30, 0, 30) # left, up, right, bottom
#resImg = ImageOps.crop(img, border)
#f = open ('croped','wb')
#f.write(resImg)
#f.close()










end = nc.read_until(b">>")
print(end)



