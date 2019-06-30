import struct
import random

def char(c):
	return struct.pack("=c",c.encode('ascii'))
def word(c):
	return struct.pack("=h",c)
def dword(c):
	return struct.pack("=l",c)
def color(r,g,b):
	return bytes([b,g,r])

class Bitmap(object):
            
    def __init__(self, width,height):
	    self.width = width
	    self.height = height
	    self.framebuffer = []
	    self.clear()

    def clear(self):
	    self.framebuffer = [
	    [
		    color(0,0,0) 
			    for x in range(self.width)
		    ]
		
		    for y in range(self.height)
	    ]
        
    def write(self, filename):
	    f = open(filename, 'wb')

	    #file header
	    f.write(char('B'))
	    f.write(char('M'))
	    f.write(dword(14 + 40 + self.width * self.height *3))
	    f.write(dword(0))
	    f.write(dword(14+40))

	    #image header 40
	    f.write(dword(40))
	    f.write(dword(self.width))
	    f.write(dword(self.height))
	    f.write(word(1))
	    f.write(word(24))
	    f.write(dword(0))
	    f.write(dword(self.width * self.height *3))	
	    f.write(dword(0))
	    f.write(dword(0))
	    f.write(dword(0))
	    f.write(dword(0))

	    for x in range(self.height):
		    for y in range(self.width):
			    f.write(self.framebuffer[x][y])

	    f.close()
    def point(self,x,y,color):
        self.framebuffer[y][x] = color

    def line(self,x0,x1,y0,y1,color):
        m = (y1-y0)/(x1-x0)
        m = int(m)
        print(m)
        b = y1 - m*x1
        for x in range(x0,x1):
            for y in range(y0,y1):
                yc = m*x + b
                self.framebuffer[yc][x] = color
                
	
        

		      
            
       

     
  
def inciso1():
        
        r = Bitmap(800,600)
        r.point(300,200, color(255, 255, 255))
        r.write("inciso1.bmp")
def inciso2():
    r = Bitmap(800,600)
    r.point(799,599,color(255,255,255))
    r.point(2,2,color(255,255,255))
    r.point(799,2,color(255,255,255))
    r.point(2,599,color(255,255,255))
    r.write("inciso2.bmp")
def inciso3():
    r = Bitmap(800,600)
    #cuadrado
    for x in range(350,450):
        x = x + 1
        r.point(x,100, color(255,255,255))
        r.point(x,200, color(255,255,255))
    for y in range(100,200):
        r.point(350,y, color(255,255,255))
        r.point(450,y, color(255,255,255))
    #cuadrado 2
    for x in range(400,500):
        x = x + 1
        r.point(x,150, color(255,255,255))
        r.point(x,250, color(255,255,255))
    for y in range(150,250):
        r.point(400,y, color(255,255,255))
        r.point(500,y, color(255,255,255))
    #diagonal
    r.line(350,400,200,250,color(255,255,255))    
    r.line(450,500,200,250,color(255,255,255))
    r.line(350,400,100,150,color(255,255,255))
    r.line(450,500,100,150,color(255,255,255))
    r.write("inciso3.bmp")

def inciso4():
    r = Bitmap(800,600)
    for x in range(1,800):
        r.point(x,1, color(255,255,255))
        r.point(x,599, color(255,255,255))
    for y in range(1,600):
        r.point(1,y, color(255,255,255))
        r.point(799,y, color(255,255,255))
    
    r.write("inciso4.bmp")
def inciso5():
    r = Bitmap(1000,1000)
    r.line(20,1000,20,1000,color(255,255,255))
    r.write("inciso5.bmp")
def inciso6():
    r = Bitmap(1000,1000)
    for x in range(1,1000):
        for y in range(1,1000):
            col = random.randint(1,100)
            if(col > 50):
                w = 255
            else:
                w = 0
            r.point(x,y,color(w,w,w))
    r.write("inciso6.bmp")
def inciso7():
    r = Bitmap(1000,1000)
    for x in range(1,1000):
        for y in range(1,1000):
            t = random.randint(1,255)
            g = random.randint(1,255)
            b = random.randint(1,255)
            r.point(x,y,color(t,g,b))
    r.write("inciso7.bmp")
def inciso8():
    r = Bitmap(1000,1000)
    for x in range(1,1000):
        for y in range(1,1000):
            col = random.randint(1,1000)
            if(col > 999):
                w = 255
            else:
                w = 0
            r.point(x,y,color(w,w,w))
    r.write("inciso8.bmp")
    
    
inciso1()
inciso2()
inciso3()
inciso4()
inciso5()
inciso6()
inciso7()
inciso8()
