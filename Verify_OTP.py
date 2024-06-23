import tkinter as tk
from tkinter import ttk, messagebox
import math, random
from Mail import Send_Mail
global OTP # Declare OTP as a global variable

def verify_check(email_entry,Mob_entry,verify_button_panel, otp):
    if otp == OTP:
        from Admin_Session import Opening_Account
        messagebox.showinfo("Verification Successful", "OTP Verified Successfully!")
        verify_win.destroy()

        email_entry.configure(state="disabled")
        Mob_entry.configure(state="disabled")
        verify_button_panel.config(state="disabled")
    else:
        messagebox.showerror("Verification Failed", "Incorrect OTP. Please try again.")

def resend_otp():
    OTP = generate_otp() 
    messagebox.showinfo("Resend OTP", "OTP Resent Successfully!")

def Verify(email_entry,Mob_entry, verify_button_panel, Customer_Name, Recipient_Email, Content):
    global verify_win
    
    OTP = generate_otp()
    Send_OTP(Customer_Name, Recipient_Email, Content)
    
    verify_win = tk.Tk()
    verify_win.title("Verification System")
    verify_win.geometry("300x150")
    
    ttk.Label(verify_win, text="OTP Verification", font=("Helvetica", 12, "bold")).pack(pady=5)
    ttk.Label(verify_win, text="An OTP verification code has been sent to your verifying email!").pack(pady=5)
    
    entry_var = tk.StringVar()
    entry_box = ttk.Entry(verify_win, textvariable=entry_var)
    entry_box.pack(pady=5)
    
    verify_button = tk.Button(verify_win, text="Verify", command=lambda: verify_check(email_entry,Mob_entry, verify_button_panel, otp=entry_box.get()))
    verify_button.pack(side=tk.BOTTOM, padx=5, pady=5)

    resend_button = tk.Button(verify_win, text="Resend OTP", command=resend_otp)
    resend_button.pack(side=tk.BOTTOM, padx=5, pady=5)
    
    verify_win.mainloop()

def Send_OTP(Customer_Name, Recipient_Email, Content):
    global OTP
    
    Subject="Bank System 🏦"

    if Content == "Opening New Account":
        Content=f'''\t\t Bank Verification System🛡 !️

Dear {Customer_Name}🫣,
    Thank you for opening your new account in our bank. Your One-Time Password (OTP) for verification is:

            {OTP}

    This OTP is valid till verification popup closes. Please do not share this OTP with anyone🤫, including bank staffs. If you did not initiate this opening new account, please contact our customer support immediately at 👉 copycat.developerz@gmail.com.
        
Thank you,
CopyCat Team😼,
Bank System'''
    Send_Mail(Recipient_Email, Subject, Content)

def generate_otp():
    global OTP
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6) :
        OTP += string[math.floor(random.random() * length)]
    return OTP

if __name__ == "__main__":
    Verify("John Doe", "rishikesh1878@gmail.com", "Opening New Account")
