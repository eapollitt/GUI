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
    
        self.rb1 = tkinter.Radiobutton(self.topframe,text='Option 1', variable=self.radio_var,value=10)
        self.rb2 = tkinter.Radiobutton(self.topframe,text='Option 2', variable=self.radio_var,value=20)
        self.rb3 = tkinter.Radiobutton(self.topframe,text='Option 3', variable=self.radio_var,value=30)
   
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.rb2.select() #selected as default when code starts to run 


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
        tkinter.messagebox.showinfo("Selection", "The value is " + str(self.radio_var.get()))

    #get method gets the value of that variable and need to convert to the string because it is a message box
    #values are set 10,20,30



    
        #top bottom left and right or options and top is the default if you dont specify
        
         #sustains the window on a loop until the user closes it out
        #the rest of the code does not get executed until you're finished with that window

my_gui = myGUI()

print("I am done")

#text box shows up on top left of computer screen, and when you close it out, I am done prints in the terminal
