import tkinter as tk
import socket
import time
import random
from tkinter import messagebox
from DataBase_Op import Check_for_matches
def destroy_current_session_content(window):
    for widget in window.winfo_children():
        widget.destroy()
    return



def Back_To_Main_Menu(window):
    from Main import Main_Menu
    
    # Recreate Main
    return Main_Menu(window)


def generate_number(length):
    if length == 11:
        account_number = ''.join(random.choices('0123456789', k=length))
        Search_Query={"Bank Details.Account No": account_number}
        if Check_for_matches(Search_Query,"CustomerDB"):
            generate_number(length)
        else:
            return account_number

    if length == 6:
        card_number = ''.join(random.choices('0123456789', k=length))
        Search_Query={"ATM.Card No": card_number}
        if Check_for_matches(Search_Query,"CustomerDB"):
            generate_number(length)
        else:
            return card_number
        
    if length == 4:
        pin = ''.join(random.choices('0123456789', k=length))
        return pin
