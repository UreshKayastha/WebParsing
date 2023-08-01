import tkinter as tk

window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(3, minsize=10, weight=1)
window.columnconfigure(3, minsize=10, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=3)
btn_open = tk.Button(frm_buttons, text="Open")
btn_save = tk.Button(frm_buttons, text="Save As...")
btn_open.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=1, column=0, sticky="ns")
txt_edit.grid(row=0, column=0, sticky="nsew")

window.mainloop()