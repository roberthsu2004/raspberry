from tkinter import *
from gpiozero import LED as LightBolt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

buttonText = None
lightBolt = LightBolt(25)

def displayWindow(w):
    global buttonText
    buttonText = StringVar()
    buttonText.set("OPEN")
    mainFrame = Frame(w,borderwidth=2,relief=GROOVE)    
    Button(mainFrame,textvariable=buttonText,font=("Helvetica", 18, "bold italic"),command=userClick).pack(expand=True,fill=BOTH,padx=40,pady=25);
    mainFrame.pack(expand=True,fill=BOTH,padx=10,pady=10)
    
def setupFirebaseDb():
    global led25Ref
    cred = credentials.Certificate('raspberryfirebase-firebase-adminsdk-q4ht6-7d3f9d2d5e.json')
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
    })
    print("abc")
    led25Ref = db.reference('raspberrypi/LED_Control/LED25')
    
    led25Ref.listen(firebaseContentChange)

def firebaseContentChange(event):
    print("content change")
    print("Event type:{},Event path:{}".format(event.data,event.path));
    if event.data == "CLOSE":
        lightBolt.off();
    else:
        lightBolt.on();
        

   
def userClick():    
    print("user click");
    if buttonText.get() == "OPEN":
        buttonText.set("CLOSE")
        #lightBolt.off();
        led25Ref.set("CLOSE")
        
    else:
        buttonText.set("OPEN")
        #lightBolt.on();
        led25Ref.set("OPEN")

if __name__ == "__main__":
    led25Ref = None
    window = Tk();
    window.title("LED Control")
    window.geometry("300x200")
    setupFirebaseDb()
    displayWindow(window);
   
    window.mainloop();
    
