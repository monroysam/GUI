import tkinter
import tkinter.messagebox

class GIU:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")
        self.main_window.title("Frames and buttons")


        # creates two frames, one top and one bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        #set the intVar variable to 1
        self.cb_var1.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text = "option 1", variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text = "option 2", variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text = "option 3", variable = self.cb_var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text = "OK", command = self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)

        self.ok_button.pack(side = "left")
        self.quit_button.pack(side = "left")


        self.top_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop() 

    def show_choice(self):
        message = "You have selected: \n"

        if self.cb_var1.get() == 1:
            message += '1\n'
        if self.cb_var2.get() == 1:
            message += '2\n'
        if self.cb_var3.get() == 1:
            message += '3\n'

        tkinter.messagebox.showinfo("Selection", message)

kconv = GIU()

print("Moving on...") 