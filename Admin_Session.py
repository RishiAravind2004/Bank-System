import tkinter as tk
from tkinter import ttk, Button, messagebox, Scrollbar
from tkcalendar import Calendar
from datetime import datetime
from Verify_OTP import Verify
from DataBase_Op import Check_for_matches,Add_Remove_Admin,Insert_Customer_Data,Check_admin_user
from Operations import destroy_current_session_content,generate_number
from Mail import Send_Mail

def Admin_Session(window):
    ttk.Label(window, text="Admin Session", font=("Helvetica", 12, "bold")).pack()  
    # Create Panedwindow  
    panedwindow = ttk.Panedwindow(window, orient=tk.HORIZONTAL)  
    panedwindow.pack(fill=tk.BOTH, expand=True)  
    
    # Create Frames  
    left_frame = ttk.Frame(panedwindow, width=100, height=300, relief=tk.SUNKEN)  
    mid_frame = ttk.Frame(panedwindow, width=400, height=400, relief=tk.SUNKEN)
    right_frame = ttk.Frame(panedwindow, width=100, height=300, relief=tk.SUNKEN)  
    
    panedwindow.add(left_frame, weight=1)  
    panedwindow.add(mid_frame, weight=4)
    panedwindow.add(right_frame, weight=2) 

    # Adding buttons to left frame
    Back_Button = tk.Button(left_frame, text="Back To Menu", command=lambda: Back_To_Main_Menu(window))
    Back_Button.pack(pady=10)

    Open_Button = tk.Button(left_frame, text="Opening Account", command=lambda: Opening_Account(mid_frame))
    Open_Button.pack(pady=15)
    Update_Button = tk.Button(left_frame, text="Update & Info Account", command=lambda: Update_and_Information(mid_frame))
    Update_Button.pack(pady=10)
    Close_Button = tk.Button(left_frame, text="Closing Account", command=lambda: Back_To_Main_Menu(window))
    Close_Button.pack(pady=10)
    Withdraw_Button = tk.Button(left_frame, text="Withdrawal Money", command=lambda: Back_To_Main_Menu(window))
    Withdraw_Button.pack(pady=10)
    Deposit_Button = tk.Button(left_frame, text="Deposit Money", command=lambda: Back_To_Main_Menu(window))
    Deposit_Button.pack(pady=10)
    List_Button = tk.Button(left_frame, text="List Accounts", command=lambda: Back_To_Main_Menu(window))
    List_Button.pack(pady=10)




"""

        Opening New Account

"""

def Opening_Account(mid_frame):
    destroy_current_session_content(mid_frame)
    # Title
    ttk.Label(mid_frame, text="Opening New Account", font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=4, pady=20, padx=20)
    

    # Label and Entry
    # Name
    ttk.Label(mid_frame, text="Name:").grid(row=1, column=1, sticky="e")
    name_entry = tk.Entry(mid_frame)
    name_entry.grid(row=1, column=2, pady=20, padx=20)

    # Initial
    ttk.Label(mid_frame, text="Initial: ").grid(row=1, column=3, sticky="e")
    initial_entry = tk.Entry(mid_frame, width=5)
    initial_entry.grid(row=1, column=4, pady=20, padx=20)

    # DOB
    ttk.Label(mid_frame, text="DoB: ").grid(row=2, column=1, sticky="e")
    # Add Calendar
    cal = Calendar(mid_frame, selectmode='day',
                   year=2004, month=5,
                   day=2)
    cal.grid(row=2, column=4, pady=20)
    # Label to display selected date
    Dob = tk.Label(mid_frame, text="", font=("Helvetica", 10, "bold"))
    Dob.grid(row=2, column=2, pady=20, padx=20)
    # Button to get date
    Button(mid_frame, text="Get Date", command=lambda: get_date(cal, Dob)).grid(row=3, column=4, pady=20, padx=20, sticky="s")

    # Mobile No
    global Mob_entry
    ttk.Label(mid_frame, text="Mobile No:").grid(row=3, column=1, sticky="e")
    Mob_entry = tk.Entry(mid_frame)
    Mob_entry.grid(row=3, column=2, pady=20, padx=20)
    Mob_entry.bind("<Key>",Get_Mob_No)

    # Email 
    ttk.Label(mid_frame, text="Email:").grid(row=4, column=1, sticky="e")
    email_entry = tk.Entry(mid_frame, width=30)
    email_entry.grid(row=4, column=2, pady=20, padx=20)

    # Email Verification

    verify_button_panel = Button(mid_frame, text="Verify", command=lambda: Verify_Btn(email_entry,Mob_entry, verify_button_panel, Customer_Name=name_entry.get(), Recipient_Email=email_entry.get(), Content="Opening New Account"))

    verify_button_panel.grid(row=4, column=3, pady=20, padx=20, sticky="s")

    # Address
    ttk.Label(mid_frame, text="Address:").grid(row=5, column=1, sticky="e")
    address_entry = tk.Text(mid_frame, height=4, width=30)
    address_entry.grid(row=5, column=2, pady=20, padx=20)

    submit_button = Button(mid_frame, text="Submit and continue", command=lambda: check_textboxs(mid_frame,name_entry.get(), initial_entry.get(), address_entry.get("1.0", "end-1c"), Dob.cget("text"), Mob_entry['state']=='disabled', email_entry['state']=='disabled', Mob_entry.get(), email_entry.get()))

    submit_button.grid(row=6, column=4, pady=20, padx=20, sticky="s")



def Opening_Account_Page_2(mid_frame,Customer_details):
    destroy_current_session_content(mid_frame)

    # Title
    ttk.Label(mid_frame, text="Opening New Account", font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=20, padx=20)
    

    # Label and Entry
    # Username
    ttk.Label(mid_frame, text="Username: ").grid(row=1, column=1, sticky="e")
    username_entry = tk.Entry(mid_frame)
    username_entry.grid(row=1, column=2, pady=20, padx=20)

    # password
    ttk.Label(mid_frame, text="Password: ").grid(row=2, column=1, sticky="e")
    userpass_entry = tk.Entry(mid_frame)
    userpass_entry.grid(row=2, column=2, pady=20, padx=20)

    

    # Account Type
    ttk.Label(mid_frame, text="Account Type: ").grid(row=3, column=1, sticky="e")
    # Create a variable to hold the selected option
    acc_type_var = tk.StringVar(value="Savings")
    # Create radio buttons
    radio_button1 = tk.Radiobutton(mid_frame, text="Savings Account", variable=acc_type_var, value="Savings")
    radio_button1.grid(row=3, column=2, pady=20, padx=10)

    radio_button2 = tk.Radiobutton(mid_frame, text="Current Account", variable=acc_type_var, value="Current")
    radio_button2.grid(row=3, column=3, pady=20, padx=10)

    # Initial amount
    ttk.Label(mid_frame, text="Initial Balance: ").grid(row=4, column=1, sticky="e")
    InitialAmt_entry = tk.Entry(mid_frame)
    InitialAmt_entry.grid(row=4, column=2, pady=20, padx=20)

    # Is Admin?
    ttk.Label(mid_frame, text="Is Admin?: ").grid(row=5, column=1, sticky="e")
    # Create a variable to hold the selected option
    isadmin = tk.StringVar(value="No")
    # Create radio buttons
    admin_no = tk.Radiobutton(mid_frame, text="No", variable=isadmin, value="No")
    admin_no.grid(row=5, column=2, pady=20, padx=10)

    admin_yes = tk.Radiobutton(mid_frame, text="Yes", variable=isadmin, value="Yes")
    admin_yes.grid(row=5, column=3, pady=20, padx=10)


    # Security Question
    ttk.Label(mid_frame, text="Security Question:").grid(row=6, column=1, sticky="e")
    SQ_entry = tk.Text(mid_frame, height=4, width=30)
    SQ_entry.grid(row=6, column=2, pady=20, padx=20)

    # Security Question
    ttk.Label(mid_frame, text="Security Answer:").grid(row=7, column=1, sticky="e")
    SAns_entry = tk.Text(mid_frame, height=4, width=30)
    SAns_entry.grid(row=7, column=2, pady=20, padx=20)


    submit_confirm_button = Button(mid_frame, text="Submit to open account", command=lambda: check_textboxs_2(mid_frame ,username_entry.get(), userpass_entry.get(), acc_type_var.get(), InitialAmt_entry.get(),isadmin.get() ,SQ_entry.get("1.0", "end-1c"), SAns_entry.get("1.0", "end-1c"),Customer_details))
    submit_confirm_button.grid(row=8, column=1, pady=20, padx=20, sticky="s")

def check_textboxs(mid_frame,Name,Initial,Address,Dob,Mobile_Check,Email_Check,Mobile,Email):
    Error=False
    if len(Name)==0:
        Error=True
    if len(Initial)==0:
        Error=True
    if len(str(Dob))==0:
        Error=True
    if len(Address)==0:
        Error=True
    if Mobile_Check is False:
        Error=True
    if Email_Check is False:
        Error=True

    if Error is True:
        messagebox.showerror("Error!", "Please check whether you have fill every informations and verfied!")
    else:
        name= Name.upper()+" "+Initial.upper()
        Customer_details={
            "Name": name,
            "Dob": Dob,
            "MobileNo": Mobile,
            "Email": Email,
            "Address": Address.upper()
        }
        print(Customer_details)
        Opening_Account_Page_2(mid_frame,Customer_details)

        
def check_textboxs_2(mid_frame, Username ,Password ,Account_type,InitialAmt ,Isadmin ,Security_Qn ,Security_Ans ,Customer_details):
    Error=False
    if len(InitialAmt)==0:
        Error=True
    if len(Username)==0:
        Error=True
    if len(Password)==0:
        Error=True
    if len(Security_Qn)==0:
        Error=True
    if len(Security_Ans)==0:
        Error=True

    if Error is True:
        messagebox.showerror("Error!", "Please check whether you have fill every informations!")
    else:
        if Isadmin == "Yes":
            email=Customer_details["Email"]
            Add_Remove_Admin(email,"add")
        AccNo=generate_number(11)
        CardNo=generate_number(6)
        Pin=generate_number(4)

        Customer_Info = {
            "Name": Customer_details["Name"],
            "Dob": Customer_details["Dob"],
            "MobileNo": int(Customer_details["MobileNo"]),
            "Email": Customer_details["Email"],
            "Address": Customer_details["Address"],
            "Bank Details": {
                "Account No": int(AccNo),
                "Ac Type": Account_type,
                "Balance": int(InitialAmt)
            },
            "Credentials": {
                "UserID": Username,
                "Password": Password,
                "Security Qn": Security_Qn,
                "Security Ans": Security_Ans
            },
            "ATM": {
                "Card No": int(CardNo),
                "PIN": int(Pin)
            },
            "Transactions": []
        }
            
        print(Customer_Info)
        Insert_Customer_Data(Customer_Info)
        messagebox.showinfo("Successful", "Creating new account completed!")

        # sending copy to mail

        EMAIL=str(Customer_details["Email"])

        Content=f'''\t\t Bank Verification System🛡 !️

Dear {Customer_details["Name"]}🫣,
    Thank you for opening your new account in our bank. You have successfully created an account!

\t\t Customer Information!

            Name: {Customer_details["Name"]}
            Dob: {Customer_details["Dob"]}
            Mobile No: {Customer_details["MobileNo"]}
            Email: {EMAIL}
            Address: {Customer_details["Address"]}

\t\t Customer Bank Information!

            Account No: {AccNo}
            Account type: {Account_type}
            Balance: {InitialAmt}
            
\t\t Customer Security Information!

            User ID: {Username}
            Password: {Password}
            Security Question: {Security_Qn}
            Security Answer: {Security_Ans}

\t\t Customer ATM Information!

            Card No: {CardNo}
            PIN: {Pin}

    Please do not share your information with anyone🤫, including bank staffs. If you did not initiate this opening new account, please contact our customer support immediately at 👉 copycat.developerz@gmail.com.
        
Thank you,
CopyCat Team😼,
Bank System'''

        Send_Mail(EMAIL, "Bank System 🏦", Content)

        destroy_current_session_content(mid_frame)


        ttk.Label(mid_frame, text="Customer Account Informations", font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=20, padx=20)
    
        ttk.Label(mid_frame, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Customer_details["Name"]).grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="Dob:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Customer_details["Dob"]).grid(row=2, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="MobileNo:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Customer_details["MobileNo"]).grid(row=3, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="Email:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Customer_details["Email"]).grid(row=4, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="Address:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Customer_details["Address"]).grid(row=5, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="Bank Account No:").grid(row=6, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=AccNo).grid(row=6, column=1, sticky="w", padx=5, pady=5)
    
        ttk.Label(mid_frame, text="Account Type:").grid(row=7, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Account_type).grid(row=7, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="Is Admin:").grid(row=8, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Isadmin).grid(row=8, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="User ID:").grid(row=9, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Username).grid(row=9, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="Password:").grid(row=10, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Password).grid(row=10, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="Security Question:").grid(row=11, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Security_Qn).grid(row=11, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="Security Answer:").grid(row=12, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Security_Ans).grid(row=12, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="ATM Card No:").grid(row=13, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=CardNo).grid(row=13, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(mid_frame, text="ATM PIN:").grid(row=14, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text=Pin).grid(row=14, column=1, sticky="w", padx=5, pady=5)


        ttk.Label(mid_frame, text="Note", font=("Helvetica", 9, "bold")).grid(row=16, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(mid_frame, text="A copy of these information are sent to your email!").grid(row=16, column=1, sticky="w", padx=5, pady=5)

        okay_button = Button(mid_frame, text="Okay!", command=lambda: destroy_current_session_content(mid_frame))
        okay_button.grid(row=17, column=1, pady=20, padx=20, sticky="s")

    
def Verify_Btn(email_entry, Mob_entry, verify_button_panel, Customer_Name, Recipient_Email, Content):

    email_value = email_entry.get()
    mob_value = Mob_entry.get()
    
    search_query_email = {"Email": email_value}
    email_result = Check_for_matches(search_query_email, DbName='CustomerDB')

    search_query_mob = {"MobileNo": int(mob_value)}
    mob_result = Check_for_matches(search_query_mob, DbName='CustomerDB')

    if email_result and mob_result:
        messagebox.showerror("Database Error", "Both Email and Mobile Number already exist.Please try another!")
    elif email_result:
        messagebox.showerror("Database Error", "Email already exists.Please try another!")
    elif mob_result:
        messagebox.showerror("Database Error", "Mobile Number already exists.Please try another!")
    else:
        Verify(email_entry,Mob_entry, verify_button_panel, Customer_Name, Recipient_Email, Content)

def get_date(cal, Dob):
    selected_date = cal.get_date()
    # Convert the selected date string to datetime object
    datetime_object = datetime.strptime(selected_date, '%m/%d/%y')
    # Format the datetime object to 'DD-MM-YYYY' format
    formatted_date = datetime_object.strftime('%d-%m-%Y')
    Dob.config(text=" " + formatted_date)

def Get_Mob_No(event):
    global Mob_entry
    if event.char.isdigit() or event.keysym == "BackSpace":
        if len(Mob_entry.get()) >= 10 and event.keysym != "BackSpace":
            return 'break'
    else:
        return 'break'


"""

        Updating Information of Account

"""




def Update_and_Information(mid_frame):
    destroy_current_session_content(mid_frame)


    ttk.Label(mid_frame, text="Updating and Information of Account", font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=4, pady=20, padx=20)

    ttk.Label(mid_frame, text="Enter the account number for which account details you want to update and view inforamtion of teh account!").grid(row=1, column=0, columnspan=4, pady=20, padx=20)
    
    global AccNo_entry
    ttk.Label(mid_frame, text="Account No: ").grid(row=2, column=1, sticky="e")
    AccNo_entry = tk.Entry(mid_frame)
    AccNo_entry.grid(row=2, column=2, pady=20, padx=20)
    AccNo_entry.bind("<Key>",Get_Acc_No)

    Update_Info_button = Button(mid_frame, text="Update Information", command=lambda: InfoAndUpdates(mid_frame,"update-user"))
    Update_Info_button.grid(row=4, column=1, pady=10, padx=20)

    RemoveAdmin_button = Button(mid_frame, text="Remove From Admin", command=lambda: InfoAndUpdates(mid_frame,"add-user"))
    RemoveAdmin_button.grid(row=4, column=2, pady=10, padx=20)

    AddAdmin_button = Button(mid_frame, text="Add to Admin", command=lambda: InfoAndUpdates(mid_frame,"remove-user"))
    AddAdmin_button.grid(row=4, column=3, pady=10, padx=20)

    InfoView_button = Button(mid_frame, text="View Information", command=lambda: InfoAndUpdates(mid_frame,"info-user"))
    InfoView_button.grid(row=4, column=4, pady=10, padx=20)

def Get_Acc_No(event):
    # Allow digits and Backspace
    if event.char.isdigit() or event.keysym == "BackSpace":
        if len(AccNo_entry.get()) >= 11 and event.keysym != "BackSpace":
            return 'break'
    # Allow Ctrl+V (paste)
    elif event.state & 0x0004 and event.keysym == 'v':  # Check if Ctrl is pressed
        return
    else:
        return 'break'
def InfoAndUpdates(mid_frame,work):
    AccNo=int(AccNo_entry.get())
    search_query_email = {"Bank Details.Account No": AccNo}
    AccNo_result = Check_for_matches(search_query_email, DbName='CustomerDB')
    if AccNo_result:
        if work=="add-user":
            res=Check_admin_user(AccNo_result.get("Email"))
            if res:
                messagebox.showerror("Admin Status Error", "This User is already an Admin!")
            else:
                email=AccNo_result.get("Email")
                Add_Remove_Admin(email, "add")
                messagebox.showerror("Admin Status Error", "The user with email '{email}' has been successfully added as an admin!")
        elif work=="remove":
            res=Check_admin_user(AccNo_result.get("Email"))
            if res:
                email=AccNo_result.get("Email")
                Add_Remove_Admin(email, "remove")
                messagebox.showerror("Admin Status Error", "The user with email '{email}' has been successfully removed from admin!")
            else:
                messagebox.showerror("Admin Status Error", "This User is not an Admin!")
    else:
        messagebox.showerror("Failed", " Please check \"Account No\" is valid!")
if __name__ == "__main__":
    window = tk.Tk()
    Admin_Session(window)
    window.mainloop()
