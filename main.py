import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from work import Gmail_sender
import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import threading
import pyrebase


class GmailAutomation:
    def __init__(self, root):
        self.root = root
        self.root.geometry("360x375+400+150")
        self.root.title("Gmail Automation")
        self.root.iconphoto(False, PhotoImage(file="images\icon.png"))
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)


          #   ========================  login frame ========================
        self.login_frame = LabelFrame(self.root, bg="#fff")
        self.login_frame.place(x=5, y=25, width=350, height=340)

        #   ========================  login label title========================
        loginLabel = Label(self.root, text="Log In",
                           fg="#57a1f8", bg="white",  font=("Ruda", 25, "bold"))
        loginLabel.place(x=130, y=0)

        #   ========================  Email entry and some design function ========================
        def on_enter_userName(e):
            name = self.email_entry.get()
            if name == "Email":
                self.email_entry.delete(0, "end")

        def on_leave_userName(e):
            name = self.email_entry.get()
            if name == "":
                self.email_entry.insert(0, "Email")
        self.email_entry = Entry(self.login_frame, bd=0, bg="white",
                                 fg="dimgray", font=("times new roman", 15))
        self.email_entry.place(x=40, y=70, width=270)
        self.email_entry.insert(0, "Email")
        self.email_entry.bind("<FocusIn>", on_enter_userName)
        self.email_entry.bind("<FocusOut>", on_leave_userName)

        entry_frame = Frame(self.login_frame, bg="dimgray")
        entry_frame.place(x=35, y=95, width=280, height=2)

         #   ========================  password entry========================
        def on_enter_password(e):
            name = self.password_entry.get()
            if name == "Password":
                self.password_entry.delete(0, "end")
                self.password_entry.config(show="*")

        def on_leave_password(e):
            name = self.password_entry.get()
            if name == "":
                self.password_entry.insert(0, "Password")
                self.password_entry.config(show="")
        self.password_entry = Entry(self.login_frame, bd=0, bg="white",
                                    fg="dimgray", font=("times new roman", 15))
        self.password_entry.place(x=40, y=150, width=270)
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", on_enter_password)
        self.password_entry.bind("<FocusOut>", on_leave_password)

        entry_frame = Frame(self.login_frame, bg="dimgray")
        entry_frame.place(x=35, y=175, width=280, height=2)

        #   =======================   log in button  ========================
        login_btn = Button(self.login_frame, text="Log In", bg="#57a1f8", fg="white", border=0, pady=2, font=(
            "Ruda", 15, "bold"), command=self.loginAuthentication)
        login_btn.place(x=35, y=210, width=280)
        
        #   =======================   log in button  ========================
        create_tatle = Label(self.root, text="© 2022 | CREATE BY ANIK SAHA", font=(
            "Ruda", 8), fg="#57a1f8", bg="white")
        create_tatle.place(x=90, y=352)

    #   =======================   log in button Authentication function  ========================
    def loginAuthentication(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)
        config = {
        "apiKey": "AIzaSyA_yuCRnppJRS77M1YmgcdieEo_xrG_GXQ",
        "authDomain": "outlook-auth-9791e.firebaseapp.com",
        "projectId": "outlook-auth-9791e",
        "storageBucket": "outlook-auth-9791e.appspot.com",
        "messagingSenderId": "271355744307",
        "databaseURL": "https://outlook-auth-9791e-default-rtdb.firebaseio.com",
        "appId": "1:271355744307:web:28a565dc3117b1993a5346",
        "measurementId": "G-D8VD59T2GZ"
        }
        firebase = pyrebase.initialize_app(config)
        # Get a reference to the auth service
        auth = firebase.auth()
       
        # Log the user in
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            Label(self.login_frame, text="Successfully Login", font=(
                "Ruda", 10), bg="white", fg="green").place(x=10, y=280, width=330)
            self.mainFunc()
        except Exception as ex:
            Label(self.login_frame, text="Wrong email and password", font=(
                "Ruda", 10), bg="white", fg="red").place(x=10, y=280, width=330)

    #   =======================   attachment  button function  ========================
    def textFileOpen(self, valueType):
        filename = filedialog.askopenfilename(
            initialdir="C:/", title="select a file")
        try:
            btn_name = filename.split("/")
                # print(btn_name)
            with open(filename, 'r') as file:
                read_file = file.read().split("\n")
            if valueType == 'sender':
                self.senderList = read_file
                self.sendFileBtn.config(text=btn_name[-1])
                self.total_sender_count.config(text=len(self.senderList))
                # print(self.senderList)
            elif valueType == 'traffic':
                self.trafficList = read_file
                self.toMail.config(text=btn_name[-1])
                self.total_to_count.config(text=len(self.trafficList))
        except:
            pass
            
    

    def mainFunc(self):   
        #================================= create mail write folder and txt file ==============================
        try:    
            os.mkdir('mail write')
        except:
            pass
        p = os.listdir("mail write")
        if "subject.txt" not in p:
            sub = open("mail write/subject.txt", "w")
        if "body.txt" not in p:
            body = open("mail write/body.txt", "w")
 
        #================================= page size setup ==============================
        self.root.geometry("500x335+400+150")
        self.root.title("Gmail Automation")

        #================================= some variables ==============================
        self.senderList = []
        self.trafficList = []

        #================================= main frame ==============================
        main_frame = Frame(self.root, bg="#fff")
        main_frame.place(x=0, y=0, width=500, height=375)

        #================================= top lable ==============================
        top_lbl = Label(self.root, text="Gmail Automation", bg="#E83F31", fg="#FFFFFF", font=("Ruda", 15, "bold"))
        top_lbl.place(x=0, y=0, width=500)


        #================================= send mail and password frame ==============================
        mail_pass = LabelFrame(self.root, text="Gmail & Password", bg="#fff", bd=1, font=("Ruda", 9, "bold"))
        mail_pass.place(x=5, y=40, width=240, height=50)

         #================================= send mail and password button ==============================
        self.sendFileBtn = Button(mail_pass, text="Select Text File", font=("Ruda", 12, "bold"), bd=1, bg="#3FA9F5", fg="#FFFFFF", command=lambda:self.textFileOpen("sender"))
        self.sendFileBtn.place(x=0, y=0, width=240, height=30)

        # #================================= To mail frame ==============================
        toMailList = LabelFrame(self.root, text="Traffic Mail", bg="#fff", bd=1, font=("Ruda", 9, "bold"))
        toMailList.place(x=5, y=100, width=240, height=50)

        self.toMail = Button(toMailList, text="Select Text File", font=("Ruda", 12, "bold"), bd=1, bg="#3FA9F5", fg="#FFFFFF", command=lambda:self.textFileOpen("traffic"))
        self.toMail.place(x=0, y=0, width=240, height=30)


        # #================================= set attachment ==============================
        toMailList = LabelFrame(self.root, text="Attachment", bg="#fff", bd=1, font=("Ruda", 9, "bold"))
        toMailList.place(x=5, y=160, width=240, height=50)

        toMail = Button(toMailList, text="Select Text File", font=("Ruda", 12, "bold"), bd=1, bg="#3FA9F5", fg="#FFFFFF")
        toMail.place(x=0, y=0, width=240, height=30)

        # #================================= To mail limit label ==============================
        toMailLimit = Label(self.root, text="Per Send To Limit :", bg="#3FA9F5", fg="#fff", font=("Ruda", 12, "bold"))
        toMailLimit.place(x=5, y=225, width=155, height=30)
        def update_par_send_limit(event):
            self.par_send_limit_count.config(text=self.to_mail_send_limit.get())
        self.to_mail_send_limit = ttk.Spinbox(
            self.root, from_=0, to=490, font=("Ruda", 13, "bold"))
        self.to_mail_send_limit.place(x=165, y=225, width=80, height=30)
        self.to_mail_send_limit.insert(0, "0")
        self.to_mail_send_limit.bind("<FocusOut>", update_par_send_limit)

        # #================================= Mail Send Limit ==============================
        toMailLimit = Label(self.root, text="Mail Send Limit :", bg="#3FA9F5", fg="#fff", font=("Ruda", 12, "bold"))
        toMailLimit.place(x=260, y=225, width=145, height=30)

        def update_mail_send_limit(event):
            self.mail_send_limit_count .config(text=self.mail_send_limit.get())
        self.mail_send_limit = ttk.Spinbox(
            self.root, from_=0, to=490, font=("Ruda", 13, "bold"))
        self.mail_send_limit.place(x=410, y=225, width=80, height=30)
        self.mail_send_limit.insert(0, "0")
        self.mail_send_limit.bind("<FocusOut>", update_mail_send_limit)

        # #================================= sending result ==============================
        sending_result = LabelFrame(self.root, text="Result", bg="#fff", bd=1, font=("Ruda", 11, "bold"))
        sending_result.place(x=260, y=40, width=230, height=170)

        # #================================= Total sender label ==============================
        total_sender = Label(sending_result, text="Total Sender : ", font=("Ruda", 10, "bold"), bg="#fff")
        total_sender.place(x=2, y=10, width=135)
        self.total_sender_count = Label(sending_result, font=("Ruda", 10, "bold"), bg="#e6e6ea", bd=0)
        self.total_sender_count.place(x=140, y=10, width=80)
        self.total_sender_count.config(text="0")

        # #================================= Total To label ==============================
        total_to = Label(sending_result, text="Total Traffic : ", font=("Ruda", 10, "bold"), bg="#fff")
        total_to.place(x=2, y=40, width=135)
        self.total_to_count = Label(sending_result, font=("Ruda", 10, "bold"), bg="#e6e6ea", bd=0)
        self.total_to_count.place(x=140, y=40, width=80)
        self.total_to_count.config(text="0")
        
        # #================================= Per Send To Limit label ==============================
        par_send_limit = Label(sending_result, text="Send To Limit :", font=("Ruda", 9, "bold"), bg="#fff")
        par_send_limit.place(x=2, y=70, width=135)
        self.par_send_limit_count = Label(sending_result, font=("Ruda", 10, "bold"), bg="#e6e6ea", bd=0)
        self.par_send_limit_count.place(x=140, y=70, width=80)
        self.par_send_limit_count.config(text="0")

        # #================================= Mail Send Limit label ==============================
        mail_send_limit = Label(sending_result, text="Mail Send Limit :", font=("Ruda", 9, "bold"), bg="#fff")
        mail_send_limit.place(x=2, y=100, width=135)
        self.mail_send_limit_count = Label(sending_result, font=("Ruda", 10, "bold"), bg="#e6e6ea", bd=0)
        self.mail_send_limit_count.place(x=140, y=100, width=80)
        self.mail_send_limit_count.config(text="0")

        #============================== send and reset buttom ==============================
        button_frame = Frame(self.root,  bg="#fff")
        button_frame.place(x=10, y=275, width=480, height=50)

        # ====================== send button  ===============
        send_button = Button(button_frame, text="Send", font=(
            "Ruda", 20, "bold"), bg="#198754", fg="#fff", bd=2, command=self.send_btn)
        send_button.place(x=0, y=0, width=240, height=50)

        # ====================== reset button  ===============
        Reset_button = Button(button_frame, text="Reset", font=(
            "Ruda", 20, "bold"), bg="#E35D6A", fg="#fff", bd=2, command=self.reset_btn)
        Reset_button.place(x=250, y=0, width=240, height=50)
    
    #============================== send function ==============================
    def send_btn(self):
        with open("mail write/subject.txt", "r") as sub_file:
            subject = sub_file.read()
        with open("mail write/body.txt", "r") as body_file:
            body = body_file.read()
        to_mail_send_limit_value = int(self.to_mail_send_limit.get())
        mail_send_limit_value = int(self.mail_send_limit.get())
        if len(self.senderList) == 0:
            messagebox.showerror("Error", "Please, Provide the Gmail & Password txt file!", parent=self.root)
        elif len(self.trafficList) == 0:
            messagebox.showerror("Error", "Please, Provide the Traffic Mail txt file!", parent=self.root)
        elif to_mail_send_limit_value == 0:
            messagebox.showerror("Error", "Provide the \"Per Send To Limit\"!", parent=self.root)
        elif to_mail_send_limit_value > 490:
            messagebox.showerror("Error", "Please, \"Per Send To Limit\" Provide less than or equal 490 !", parent=self.root)
        elif mail_send_limit_value == 0:
            messagebox.showerror("Error", "Provide the \"Mail Send Limit\"!", parent=self.root)
        elif mail_send_limit_value > 20:
            messagebox.showerror("Error", "Please,\"Mail Send Limit\" Provide less than or equal 20 !", parent=self.root)
        elif len(subject) == 0:
            messagebox.showerror("Error", "Please, Provide the mail Subject!", parent=self.root)
        elif len(body) == 0:
            messagebox.showerror("Error", "Please, Provide the mail Body!", parent=self.root)
        else:
            askResult = messagebox.askquestion("All Information", f"From Mail : {len(self.senderList)}\nTo Mail : {len(self.trafficList)}\nPer Send To Limit : {to_mail_send_limit_value}\nMail Send Limit : {mail_send_limit_value}")
            if askResult == "yes":
                print("send")
                self.gamil_send_new_win =  Toplevel(self.root)
                self.gamil_send_call_app = Gmail_sender(self.gamil_send_new_win, self.senderList, self.trafficList, to_mail_send_limit_value, mail_send_limit_value, subject, body)
                self.reset_btn()
    #============================== reset function ==============================
    def reset_btn(self):
        try:
            self.senderList = []
            self.trafficList = []
            self.sendFileBtn.config(text="Select Text File")
            self.total_sender_count.config(text=len(self.senderList))
            self.toMail.config(text="Select Text File")
            self.total_to_count.config(text=len(self.trafficList))
            self.mail_send_limit.delete(0, END)
            self.to_mail_send_limit.delete(0, END)
            self.to_mail_send_limit.insert(0, "0")
            self.mail_send_limit.insert(0, "0")
            self.par_send_limit_count.config(text="0")
            self.mail_send_limit_count.config(text="0")
        except:
            pass

if __name__ == '__main__':
    root = Tk()
    obj = GmailAutomation(root)
    root.mainloop()