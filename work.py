import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import messagebox
import threading





class Gmail_sender:
    def __init__(self, root, senderMailPass, toMailList, parSendLimit, senderLimit, subject, body):
        self.root = root
        self.root.title("SMTP MAIL SENDER")
        self.root.geometry("240x275+300+150")
        self.root.iconphoto(False, PhotoImage(file="images\icon.png"))
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)
        self.senderMailPass = senderMailPass
        self.toMailList = toMailList
        self.parSendLimit = parSendLimit
        self.senderLimit = senderLimit
        self.subject = subject
        self.body = body
     # #================================= count variables ==============================
        self.SuccessSend = 0
        self.SuccessTraffic = 0
        self.errorSend = 0
        self.errorTraffic = 0
         # #================================= sending result ==============================
        sending_result = LabelFrame(self.root, text="Result", bg="#fff", bd=1, font=("Ruda", 11, "bold"))
        sending_result.place(x=5, y=5, width=230, height=265)

        # #================================= Total sender label ==============================
        total_sender = Label(sending_result, text="Total Sender : ", font=("Ruda", 10, "bold"), bg="#fff")
        total_sender.place(x=2, y=10, width=135)
        self.total_sender_count = Label(sending_result, text=len(self.senderMailPass), font=("Ruda", 10, "bold"), bg="#e6e6ea", bd=0)
        self.total_sender_count.place(x=140, y=10, width=80)

        # #================================= Total To label ==============================
        total_to = Label(sending_result, text="Total Traffic : ", font=("Ruda", 10, "bold"), bg="#fff")
        total_to.place(x=2, y=40, width=135)
        self.total_to_count = Label(sending_result, text=len(self.toMailList), font=("Ruda", 10, "bold"), bg="#e6e6ea", bd=0)
        self.total_to_count.place(x=140, y=40, width=80)
        
        
        # #================================= Per Send To Limit label ==============================
        par_send_limit = Label(sending_result, text="Send To Limit :", font=("Ruda", 9, "bold"), bg="#fff")
        par_send_limit.place(x=2, y=70, width=135)
        self.par_send_limit_count = Label(sending_result, text=self.parSendLimit,  font=("Ruda", 10, "bold"), bg="#e6e6ea", bd=0)
        self.par_send_limit_count.place(x=140, y=70, width=80)
       

        # #================================= Mail Send Limit label ==============================
        mail_send_limit = Label(sending_result, text="Mail Send Limit :", font=("Ruda", 9, "bold"), bg="#fff")
        mail_send_limit.place(x=2, y=100, width=135)
        self.mail_send_limit_count = Label(sending_result, text=self.senderLimit, font=("Ruda", 10, "bold"), bg="#e6e6ea", bd=0)
        self.mail_send_limit_count.place(x=140, y=100, width=80)
  

        # #================================= Successfully Sender label ==============================
        succes_sender = Label(sending_result, text="Successfully Send :", font=("Ruda", 9, "bold"), bg="#fff", fg="#7bc043")
        succes_sender.place(x=2, y=130, width=135)
        self.succes_sender_count = Label(sending_result, font=("Ruda", 10, "bold"), bg="#7bc043", bd=0)
        self.succes_sender_count.place(x=140, y=130, width=80)
        self.succes_sender_count.config(text="0")

        # #================================= Successfully Traffic label ==============================
        succes_to = Label(sending_result, text="Successfully Traffic :", font=("Ruda", 9, "bold"), bg="#fff", fg="#7bc043")
        succes_to.place(x=2, y=160, width=135)
        self.succes_to_count = Label(sending_result, font=("Ruda", 10, "bold"), bg="#7bc043", bd=0)
        self.succes_to_count.place(x=140, y=160, width=80)
        self.succes_to_count.config(text="0")

        # #================================= error Sender label ==============================
        error_sender = Label(sending_result, text="Error Send :", font=("Ruda", 9, "bold"), bg="#fff", fg="#ee4035")
        error_sender.place(x=2, y=190, width=135)
        self.error_sender_count = Label(sending_result, font=("Ruda", 10, "bold"), bg="#ee4035", bd=0)
        self.error_sender_count.place(x=140, y=190, width=80)
        self.error_sender_count.config(text="0")
        #============================== error Sender label ==============================
        error_to = Label(sending_result, text="Error Traffic :", font=("Ruda", 9, "bold"), bg="#fff", fg="#ee4035")
        error_to.place(x=2, y=220, width=135)
        self.error_to_count = Label(sending_result, font=("Ruda", 10, "bold"), bg="#ee4035", bd=0)
        self.error_to_count.place(x=140, y=220, width=80)
        self.error_to_count.config(text="0")
        threading.Thread(target=self.send_start).start()
    
    def send_start(self):
        for i in self.senderMailPass:
            driver = uc.Chrome()
            mail_pass = i.split(":")
            to_mail = ", ".join(self.toMailList[0:self.parSendLimit])
            del self.toMailList[0:self.parSendLimit]
            try:
                driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
                            'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
                            '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
                sleep(3)
                mail_box = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
                mail_box.send_keys(mail_pass[0])
                mail_box_next = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
                mail_box_next.click()
                sleep(3)
                pass_box = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
                pass_box.send_keys(mail_pass[1])
                pass_box_next = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
                pass_box_next.click()
                sleep(20)
                for j in range(self.senderLimit):
                    try:
                        compose_btn = driver.find_element(By.XPATH, "//div[@class='aic']/div/div")
                        compose_btn.click()
                        sleep(3)
                        to_box = driver.find_element(By.CLASS_NAME, "vO")
                        to_box.send_keys(to_mail)
                        sleep(1)
                        sub_box = driver.find_element(By.CLASS_NAME, "aoT")
                        sub_box.send_keys(self.subject)
                        sleep(1)
                        body_box = driver.find_element(By.XPATH, "//div[@aria-label='Message Body']")
                        body_box.send_keys(self.body)
                        sleep(1)
                        send_btn = driver.find_element(By.XPATH, "//div[text()='Send']")
                        send_btn.click()
                        sleep(3)
                        self.SuccessSend += 1
                        self.SuccessTraffic += self.parSendLimit
                        self.succes_sender_count.config(text=self.SuccessSend)
                        self.succes_to_count.config(text=self.SuccessTraffic)
                    except :
                        self.errorSend += 1
                        self.errorTraffic += self.parSendLimit
                        self.error_sender_count.config(text= self.errorSend)
                        self.error_to_count.config(text= self.errorTraffic)
            except Exception as ex:
                messagebox.showerror("Error", f"Something is worng. \n {ex}", parent=self.root)    
            driver.close() 
        messagebox.showinfo("Good News", "successfully mail send complete.", parent=self.root)