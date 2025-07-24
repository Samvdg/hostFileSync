import tkinter as tk
from sysfunctions import *

def create_gui():
   # 1) Main window
    app = tk.Tk()
    app.geometry("800x600")
    
    # State variable for radio buttons

    # Top-right frame
    top_frame = tk.Frame(app, bg="#3a3a3a")
    top_frame.pack(side="top", anchor="ne", padx=10, pady=10)

    platform_var = tk.StringVar(value="Windows")  # default selection
    # Platform toggle buttons
    for option in ["Windows", "WSL", "Linux"]:
        rb = tk.Radiobutton(
            top_frame,
            text=option,
            value=option,
            variable=platform_var,
            command=lambda opt=option: switchSystem(opt),
            indicatoron=0,  # make it look like a button
            width=8,
            bg="#444",
            fg="white",
            selectcolor="#666",
            font=("Segoe UI", 10),
            relief="raised",
            activebackground="#666"
        )
        # if platform_var.get() == option: rb.state(['selected'])
        rb.pack(side="left", padx=2)

    platform_var.set(platform_var.get())

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
    hosts = Hosts()
    for entry in hosts.entries:
        print(entry) 
    # print(hosts)
    # hosts.import_url(DEFAULT_SYNC_SOURCE)
    # print("TRUE")
    return True

def switchSystem(sys):
    print(sys)

def open_gui():
    g = create_gui()
    loadHostFileInGui(g)
    g.mainloop()