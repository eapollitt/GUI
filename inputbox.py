import tkinter
import tkinter.messagebox


class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.main_window.geometry('500x200')
        self.main_window.title("Label Demo")
        


        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.promptlabel = tkinter.Label(self.topframe, text='Enter a distance in Kilometers')
        self.entry = tkinter.Entry(self.topframe, width=10)
       

    
    #packit controls what part of the screen these elements will show on 
     #default is top


        self.promptlabel.pack(side='left')
        self.entry.pack(side='left')
       

      

        self.topframe.pack()
        self.bottomframe.pack()
        

        self.mybutton = tkinter.Button(self.main_window, text='Convert',command=self.convert)
        self.quitbutton = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
    
        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')
    #packit controls what part of the screen these elements will show on 
     #default is top
    
        tkinter.mainloop()

          #sustains the window on a loop until the user closes it out
        #the rest of the code does not get executed until you're finished with that window

    def convert(self):
        kilo = float(self.entry.get()) #get is a built in function ; accessor method

        miles = round(kilo*0.6214,2)

        tkinter.messagebox.showinfo("Result", str(kilo)+' kilometers is equal to '+ str(miles)+ " miles")
    
        #top bottom left and right or options and top is the default if you dont specify
        
         #sustains the window on a loop until the user closes it out
        #the rest of the code does not get executed until you're finished with that window

my_gui = myGUI()

print("I am done")

#text box shows up on top left of computer screen, and when you close it out, I am done prints in the terminal
