import tkinter
import tkinter.messagebox


class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.main_window.geometry('500x200')
        self.main_window.title("Label Demo")
        


        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.topframe, text='John')
        self.label2 = tkinter.Label(self.topframe, text='Jim')
        self.label3 = tkinter.Label(self.topframe, text='Jerry')


    
    #packit controls what part of the screen these elements will show on 
     #default is top


        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')

        self.label4 = tkinter.Label(self.bottomframe, text='Jill')
        self.label5 = tkinter.Label(self.bottomframe, text='Jen')
        self.label6 = tkinter.Label(self.bottomframe, text='Jessica')

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.topframe.pack()
        self.bottomframe.pack()
        

        self.mybutton = tkinter.Button(self.main_window, text='Click Me!',command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
    
        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')
    #packit controls what part of the screen these elements will show on 
     #default is top
    
        tkinter.mainloop()

          #sustains the window on a loop until the user closes it out
        #the rest of the code does not get executed until you're finished with that window

    def do_something(self):
        tkinter.messagebox.showinfo("Response", "Thanks for clicking me!")
    
        #top bottom left and right or options and top is the default if you dont specify
        
         #sustains the window on a loop until the user closes it out
        #the rest of the code does not get executed until you're finished with that window

my_gui = myGUI()

print("I am done")

#text box shows up on top left of computer screen, and when you close it out, I am done prints in the terminal
