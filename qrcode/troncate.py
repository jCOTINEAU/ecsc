
from PIL import Image
from PIL import ImageOps
import re
from pyzbar.pyzbar import decode
img = Image.open("my_recovered_log_file")
rg = re.compile('.*b\'()\'.*')
t=0
for i in range (0,2320,290):
    for z in range (0,2320,290):
        area=(i,z,i+290,z+290)
        cropped_img = img.crop(area)
        data = decode(cropped_img)
        t+=(int(data[0][0]))
print(t)
