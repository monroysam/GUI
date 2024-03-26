import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #---CREATE TITLE TEXT----
        self.main_window.geometry("500x350")
        self.main_window.title("Registration Form")    

        title_font = ("Arial", 20, "bold")
        register_font = ("Arial", 15, "bold")

        self.label1 = tkinter.Label(self.main_window, text = "Responsive Registration", font = title_font)
        self.label2 = tkinter.Label(self.main_window, text = "Form", font = title_font)    

        self.label1.pack()
        self.label2.pack()


        #---EMAIL TEXT BOX---
        self.email_frame = tkinter.Frame(self.main_window)
        self.email_label = tkinter.Label(self.email_frame, text = "Email")        
        self.email_entry = tkinter.Entry(self.email_frame, width = 25)

        self.email_label.pack(side = "left", padx = (42, 55))
        self.email_entry.pack(side = "left")

        self.email_frame.pack()

        #---PASSWORD TEXT BOX---
        self.pass_frame = tkinter.Frame(self.main_window)
        self.pass_label = tkinter.Label(self.pass_frame, text = "Password")        
        self.pass_entry = tkinter.Entry(self.pass_frame, width = 25, show = "*")

        self.pass_label.pack(side = "left", padx = (30, 40))
        self.pass_entry.pack(side = "left")

        self.pass_frame.pack()

        #---CONFIRM PASSWORD TEXT BOX---
        self.confm_pass_frame = tkinter.Frame(self.main_window)
        self.confm_pass_label = tkinter.Label(self.confm_pass_frame, text = "Confirm Password")        
        self.confm_pass_entry = tkinter.Entry(self.confm_pass_frame, width = 25, show = "*")

        self.confm_pass_label.pack(side = "left", padx = (0, 19))
        self.confm_pass_entry.pack(side = "left")

        self.confm_pass_frame.pack()


        #---NAMES TEXT BOX---
        self.name_title_frame = tkinter.Frame(self.main_window)
        self.name_title_label1 = tkinter.Label(self.name_title_frame, text = "First Name")        
        self.name_title_label2 = tkinter.Label(self.name_title_frame, text = "Last Name") 

        self.name_title_label1.pack(side = "left", padx = (0, 60))
        self.name_title_label2.pack(side = "left")

        self.name_title_frame.pack()


        #---NAMES INPUT BOX---
        self.name_input_frame = tkinter.Frame(self.main_window)        
        self.fn_entry = tkinter.Entry(self.name_input_frame, width = 15)
        self.ln_entry = tkinter.Entry(self.name_input_frame, width = 15)

        self.fn_entry.pack(side = "left")
        self.ln_entry.pack(side = "left")

        self.name_input_frame.pack()       

        #---M/F SELECTION---
        self.mf_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.mf_frame, text = "Male", variable = self.radio_var, value = 1)
        self.rb2 = tkinter.Radiobutton(self.mf_frame, text = "Female", variable = self.radio_var, value = 2)

        self.rb1.pack(side = "left")
        self.rb2.pack(side = "left")

        self.mf_frame.pack()

        #---TERMS AND CONDITION + MAIL SUB---
        self.term_frame = tkinter.Frame(self.main_window)
        self.sub_frame = tkinter.Frame(self.main_window)

        self.term_var = tkinter.IntVar()
        self.sub_var = tkinter.IntVar()

        self.terms = tkinter.Checkbutton(self.term_frame, text = "I agree with the terms and conditions", variable = self.term_var)
        self.subs = tkinter.Checkbutton(self.sub_frame, text = "I want to recive the news letter", variable = self.sub_var)

        self.terms.pack()
        self.subs.pack()

        self.term_frame.pack(padx = (0, 22))
        self.sub_frame.pack(padx = (0, 60))


        #---REGISTER BUTTON---
        self.button_frame = tkinter.Frame(self.main_window)

        self.register_button = tkinter.Button(self.button_frame, text = "Register", command = self.register,
                                               font = register_font, background = "blue", fg = "black", width = 30)

        self.register_button.pack()
        self.button_frame.pack()


        tkinter.mainloop()

    def register(self):
        regg = True
        message1 = "Please select a gender\n"
        message2 = f"Please agree with terms and" f"\n Subscribe to the newsletter\n"
        message3 = "Passwords do not match\n"
        message4 = "First name cannnot be blank\n"
        message5 = "Last name cannot be blank\n"
        message6 = "Email cannot be blank\n"
        message7 = f"You have been successfully" f"\n registered\n"
        final_message = ""
        email =  self.email_entry.get()
        pass1 = self.pass_entry.get()
        pass2 = self.confm_pass_entry.get()
        first_name = self.fn_entry.get()
        last_name = self.ln_entry.get()

        if self.radio_var.get() == 0:
            final_message += message1
            regg = False

        if self.term_var.get() == 0 or self.sub_var.get() == 0:
            final_message += message2
            regg = False

        if pass1 != pass2:
            final_message += message3
            regg = False

        if first_name == '':
            final_message += message4
            regg = False

        if last_name == '':
            final_message += message5
            regg = False

        if email == '':
            final_message += message6
            regg = False


        if regg:
            self.email_entry.delete(0, tkinter.END)
            self.pass_entry.delete(0, tkinter.END)
            self.confm_pass_entry.delete(0, tkinter.END)
            self.fn_entry.delete(0, tkinter.END)
            self.ln_entry.delete(0, tkinter.END)
            self.radio_var.set(None)
            self.term_var.set(0)
            self.sub_var.set(0)
            tkinter.messagebox.showinfo("Selection", message7)
        else:
            tkinter.messagebox.showinfo("Selection", final_message)

regform = GUI()