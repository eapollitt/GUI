import tkinter
import tkinter.messagebox


class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.main_window.geometry('500x200')
        self.main_window.title("Label Demo")
        


        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

       
        self.radio_var = tkinter.IntVar()
    
        self.cb1_var = tkinter.IntVar()
        self.cb2_var = tkinter.IntVar()
        self.cb3_var = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.topframe,text='Option 1', variable=self.cb1_var)
        self.cb2 = tkinter.Checkbutton(self.topframe,text='Option 2', variable=self.cb2_var)
        self.cb3 = tkinter.Checkbutton(self.topframe,text='Option 3', variable=self.cb3_var)
   
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        #self.rb2.select() #selected as default when code starts to run 

        #self.cb1_var = tkinter.IntVar()
        #self.cb2_var = tkinter.IntVar()
        #self.cb3_var = tkinter.IntVar()

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
        message = "You have selected:\n"
        
        if self.cb1_var.get() ==1:
            message += "option 1\n"
        if self.cb2_var.get() ==1:
            message += "option 2\n"
        if self.cb3_var.get() ==1:
            message += "option 3\n"
        
        tkinter.messagebox.showinfo("Response",message)

    #get method gets the value of that variable and need to convert to the string because it is a message box
    #values are set 10,20,30



    
        #top bottom left and right or options and top is the default if you dont specify
        
         #sustains the window on a loop until the user closes it out
        #the rest of the code does not get executed until you're finished with that window

my_gui = myGUI()

print("I am done")

#text box shows up on top left of computer screen, and when you close it out, I am done prints in the terminal
