from SimpleCV import *
display = Display()
cam = Camera()
topi = Image("topi.jpg")
mask = topi.hueDistance(color=Color.GREEN)

result = (mask.invert() - topi)


face_cascade = HaarCascade("face.xml")

while True:
     image = cam.getImage().flipHorizontal()
     faces = image.findHaarFeatures(face_cascade)
     if faces:
         faces = faces.sortArea()
         face = faces[-1]
         myFace = face.crop()
         xf=face.x-((face.width()/2)-20)
         yf=2*(face.y-((face.width()/2)+120))
         
         print yf
         image=image.blit(topi,pos=(xf,yf),mask=mask.invert())
         image.show()
