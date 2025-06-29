import tkinter as tk
from sysfunctions import *

def create_gui():
   # 1) Main window
    app = tk.Tk()
    app.geometry("800x600")

    # 2) Bottom frame (no fill/expand so it shrinks to fit its children)
    frame = tk.Frame(app, bg="#3a3a3a")
    frame.pack(expand=True, fill="both", pady=20)  

    btn_frame = tk.Frame(frame, bg="#3a3a3a")
    btn_frame.pack(side='bottom', pady=20)  

    # 3) Two buttons, packed left-to-right
    sync_btn = tk.Button(btn_frame, text="Start",  command=app.destroy, width=10, height=1)
    stop_btn = tk.Button(btn_frame, text="Finish", command=app.destroy, width=10, height=1)

    sync_btn.pack(side="left", padx=5)
    stop_btn.pack(side="left", padx=5)

    return app

def open_gui():
    g = create_gui()
    config = get_config()
    print(config)
    # g.mainloop()