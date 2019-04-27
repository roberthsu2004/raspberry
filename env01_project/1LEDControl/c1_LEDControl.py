from tkinter import *
from gpiozero import LED as LightBolt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

buttonText = None
#lightBolt = LightBolt(4)

def displayWindow(w):
    global buttonText
    buttonText = StringVar()
    buttonText.set("OPEN")
    mainFrame = Frame(w,borderwidth=2,relief=GROOVE)    
    Button(mainFrame,textvariable=buttonText,font=("Helvetica", 18, "bold italic"),command=userClick).pack(expand=True,fill=BOTH,padx=40,pady=25);
    mainFrame.pack(expand=True,fill=BOTH,padx=10,pady=10)
    
def setupFirebaseDb():
    cred = credentials.Certificate('raspberryfirebase-firebase-adminsdk-q4ht6-7d3f9d2d5e.json')
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
    })
    ref = db.reference('raspberrypi/LCD')
    print(ref.get())

   
def userClick():    
    print("user click");
    if buttonText.get() == "OPEN":
        buttonText.set("CLOSE")
        #lightBolt.off();
    else:
        buttonText.set("OPEN")
        #lightBolt.on();

if __name__ == "__main__":
    
    window = Tk();
    window.title("LED Control")
    window.geometry("300x200")
    setupFirebaseDb()
    displayWindow(window);
   
    window.mainloop();
    
