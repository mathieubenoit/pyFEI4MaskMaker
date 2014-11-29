from PIL import Image
import numpy as np



def DoImage(file,bits) : 

    im = Image.open(file)
    p = np.array(im)

    x=0
    y=60

    for i in range(len(p)):
        for j in range(len(p[0])) :
            print p[i][j]
            if p[i][j]==0 :
                bits[x+j][y+i]=1
                
            else :
                bits[x+j][y+i]=0


            
def WriteBits(bits,f) :

    for row in range(336):
        line =""
        line+= "%i "%(row+1)
        for col in range(8) :
            for i in range(10) : 
                line+="%i"%bits[col*10+i][row]
                if i==4:
                 line+="-"   
            line+=" "
        line+="\n"  
        f.write(line)

def MakeRectangle(xmin,ymin,xmax,ymax,bits) :

    for i in range(xmin,xmax):
        for j in range(ymin,ymax) :
            bits[i][j]=0



f = open("ATLASITkMask.dat","w")


x=5
y=-20

bits = [[1 for j in range(336)] for i in range(80)]

#I
MakeRectangle(12-x,10-y,18-x,30-y,bits)

#T
MakeRectangle(34-x,10-y,40-x,30-y,bits)

MakeRectangle(25-x,10-y,49-x,13-y,bits)

#K
MakeRectangle(55-x,14-y,61-x,30-y,bits)

MakeRectangle(60-x,22-y,65-x,24-y,bits)
MakeRectangle(65-x,24-y,70-x,26-y,bits)
MakeRectangle(70-x,26-y,75-x,28-y,bits)
MakeRectangle(75-x,28-y,80-x,30-y,bits)

MakeRectangle(60-x,20-y,65-x,22-y,bits)
MakeRectangle(65-x,18-y,70-x,20-y,bits)
MakeRectangle(70-x,16-y,75-x,18-y,bits)
MakeRectangle(75-x,14-y,80-x,16-y,bits)



DoImage("msu_atlas_logo.gif",bits)
#DoImage("homer.gif",bits)

WriteBits(bits,f)
       

        
