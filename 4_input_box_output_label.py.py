import tkinter
import tkinter.messagebox

class KiloConverter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")
        self.main_window.title("Frames and buttons")


        # creates two frames, one top and one bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter a distance in kilometers")

        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)

        self.prompt_label.pack(side = "left")
        self.kilo_entry.pack(side = "left")

        self.discr_label = tkinter.Label(self.mid_frame, text = "Converted to miles: ")

        # We need a StringVar object/variable to associate with and output label.
        # Use the objects set meathod to store a string of blank characters
        self.miles_label_var = tkinter.StringVar()

        # Create a label and associate it with the StringVar object. Any value stored in the
        # StringVar object will automotically be sicplayed in the label

        self.miles_label = tkinter.Label(self.mid_frame, textvariable = self.miles_label_var)


        self.calc_button = tkinter.Button(self.bottom_frame, text = "Convert", command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)

        self.calc_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        self.miles_label.pack(side = "left")
        self.discr_label.pack(side = "left")

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop() 

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round(kilo * 0.6214, 2)

        #tkinter.messagebox.showinfo("Result", str(kilo) + " kilometers is equal to " + str(miles) + " miles.")

        self.miles_label_var.set(miles)

kconv = KiloConverter()

print("Moving on...") 