import tkinter as tk
from Operations import destroy_current_session_content

def show_admin_session(window):
    destroy_current_session_content(window)
    from Admin_Session import Admin_Session
    Admin_Session(window)


def Main_Menu(window):
    destroy_current_session_content(window)
    window.title("Banking System (Online)")
    window.geometry("1200x600")
    # Create buttons for different sessions

    # Admin session button
    button_session1 = tk.Button(window, text="Admin Session", command=lambda: show_admin_session(window))
    button_session1.pack(pady=10)

    # Customer session button
    button_session2 = tk.Button(window, text="Customer Session", command=lambda: show_customer_session(window))
    button_session2.pack(pady=10)

    # ATM session button
    button_session3 = tk.Button(window, text="ATM Session", command=lambda: show_atm_session(window))
    button_session3.pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    Main_Menu(window)
