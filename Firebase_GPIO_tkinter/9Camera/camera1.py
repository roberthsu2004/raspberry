# pip3 install Pillow

from tkinter import *
from PIL import ImageTk, Image
from time import sleep
from picamera import PiCamera

camera = PiCamera();

def takePicture():
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(path);
    openImage = Image.open(path);
    img = ImageTk.PhotoImage(openImage);
    panel.configure(image=img)
    panel.image = img;
    

 

#This creates the main window of an application
window = Tk()
window.title("Join")
window.geometry("1024x810")
window.configure(background='blue')
path = "foo.jpg"
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
openImage = Image.open(path);

img = ImageTk.PhotoImage(openImage)

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
mainFrame = Frame(window);

panel = Label(mainFrame, image = img);
panel.image = img;
panel.pack(fill = BOTH, expand = YES);

button = Button(mainFrame,text="picture",command=takePicture).pack();

        #The Pack geometry manager packs widgets in rows or columns.
        
mainFrame.pack(fill=BOTH,expand=YES);
#Start the GUI
window.mainloop()

