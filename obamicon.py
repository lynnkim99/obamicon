from Myro import*
pic = makePicture("rainbow.png")
show(pic)

Obama_DarkBlue = makeColor(0,51,76)
Obama_Red = makeColor(217, 26, 33)
Obama_Blue = makeColor(112,150,158)
Obama_Yellow = makeColor(252, 227, 166)

pixels = getPixels(pic)
#use like math functions to get gray value

def changeColor():
    for px in pixels:
        red=getRed(px)*0.299
        green=getGreen(px)*0.587
        blue=getBlue(px)*0.114
        gray=red+green+blue
        
        if gray>180:
            setColor(px, Obama_Yellow)
            #repaint(pic)
        if gray>120 and gray<=180:
            setColor(px, Obama_Blue)
            #repaint(pic)
        if gray>60 and gray<=120:
            setColor(px, Obama_Red)
            #repaint(pic)
        else:
            setColor(px, Obama_DarkBlue)
            #repaint(pic)
    show(pic)

changeColor()