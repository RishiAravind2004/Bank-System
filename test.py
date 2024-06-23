import tkinter as tk

def show_selected():
    selected_option = radio_var.get()
    selection_label.config(text=f"Selected option: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Radio Buttons")

# Create a variable to hold the selected option
radio_var = tk.StringVar(value="Option 1")  # Set default value to "Option 1"

# Create radio buttons
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio_button1.pack(side="left")

radio_button2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio_button2.pack(side="left")

radio_button3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value="Option 3")
radio_button3.pack(side="left")

# Create a button to show the selected option
show_button = tk.Button(root, text="Show Selected", command=show_selected)
show_button.pack()

# Create a label to display the selected option
selection_label = tk.Label(root, text="")
selection_label.pack()

# Run the Tkinter event loop
root.mainloop()
