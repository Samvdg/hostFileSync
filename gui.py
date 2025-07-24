import tkinter as tk
from sysfunctions import *

def create_gui():
   # 1) Main window
    app = tk.Tk()
    app.geometry("800x600")
    
    # State variable for radio buttons
    platform_var = tk.StringVar(value="Windows")  # default selection

    # Top-right frame
    top_frame = tk.Frame(app, bg="#3a3a3a")
    top_frame.pack(side="top", anchor="ne", padx=10, pady=10)

    # Platform toggle buttons
    for option in ["Linux", "WSL", "Windows"]:
        rb = tk.Radiobutton(
            top_frame,
            text=option,
            variable=platform_var,
            value=option,
            indicatoron=0,  # make it look like a button
            width=8,
            relief="raised",
            bg="#444",
            fg="white",
            selectcolor="#666",
            font=("Segoe UI", 10),
            # activebackground="#666"
        )
        rb.pack(side="left", padx=2)

    # 3) Bottom frame (no fill/expand so it shrinks to fit its children)
    frame = tk.Frame(app, bg="#3a3a3a")
    frame.pack(expand=True, fill="both", pady=20) 
    
    btn_frame = tk.Frame(frame, bg="#3a3a3a")
    btn_frame.pack(side='bottom', pady=20)  

    # 3) Two buttons, packed left-to-right
    sync_btn = tk.Button(btn_frame, text="Sync",  command=app.destroy, width=10, height=1)
    stop_btn = tk.Button(btn_frame, text="Exit", command=app.destroy, width=10, height=1)

    sync_btn.pack(side="left", padx=5)
    stop_btn.pack(side="left", padx=5)

    return app

def loadHostFileInGui(g):
    

def open_gui():
    g = create_gui()
    loadHostFileInGui(g)
    g.mainloop()