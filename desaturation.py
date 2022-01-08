from PIL import Image

def desaturation(pngName):
    image1 = Image.open(pngName)
    x, y = image1.size
    for xpixel in range (x):
        for ypixel in range (y) :
            r, g, b, sample = image1.getpixel((xpixel, ypixel))
            c=(127.5 > (r+g+b)/3)*255
            image1.putpixel((xpixel,ypixel),(c,c,c))    
        #print(xpixel/x*100, '%')
    newname = 'new' + pngName
    image1.save(newname)
    image1.close()

# 1.9193007946014404 seconds on a 731 Ko png
desaturation('wolf.png')
