import tkinter as tk
from sysfunctions import *

class tkinterGui:
    
    fields = []
    
    def __init__(self):
        g = self.create_gui()
        self.loadHostFileInGui(g)
        self.loadButtons(g)
        g.mainloop()

    def create_gui(self):
    # 1) Main window
        app = tk.Tk()
        app.geometry("800x600")
        app.configure(bg="#3a3a3a")
        
        app.grid_rowconfigure(1, weight=1)     # allow center frame to grow
        app.grid_columnconfigure(0, weight=1)  # allow center frame to stretch
        
        # State variable for radio buttons

        # Top-right frame
        top_frame = tk.Frame(app, bg="#3a3a3a")
        top_frame.grid(row=0, column=0, sticky="ne", padx=10, pady=10)

        platform_var = tk.StringVar(value=detect_platform())  # default selection
        # Platform toggle buttons
        for idx, option in enumerate(["Windows", "WSL", "Linux"]):
            rb = tk.Radiobutton(
                top_frame,
                text=option,
                value=option,
                variable=platform_var,
                command=lambda opt=option: self.switchSystem(opt),
                indicatoron=0,  # make it look like a button
                width=8,
                bg="#444",
                fg="white",
                selectcolor="#666",
                font=("Segoe UI", 10),
                relief="raised",
                activebackground="#666"
            )
            rb.grid(row=0, column=idx, padx=2)

        return app

    def switchSystem(self, sys):
        print(sys)

    def loadHostFileInGui(self, g):
        #create frame for fields
        frame = tk.Frame(g, bg="#3a3a3a")
        frame.grid(row=1, column=0)
        
        #Load variables
        hosts = Hosts()
        types = ["ipv4", "ipv6", "comment", "blank"]
        
        #TODO add all these fields below to the new fields array
        
        for idx, entry in enumerate(hosts.entries):
            print(idx)
            # 1. Create dropdown menu
            type_var = tk.StringVar(value=entry.entry_type)
            type_menu = tk.OptionMenu(
                frame, type_var, *["ipv4", "ipv6", "comment", "blank"]
            )
            type_menu.config(width=7)
            type_menu.grid(row=idx, column=0, padx=5, pady=2)
            
            # 2. IP Address Entry (disabled for comment/blank)
            ip_var = tk.StringVar(value=entry.address if hasattr(entry, 'address') else "")
            ip_entry = tk.Entry(frame, textvariable=ip_var, width=15)
            ip_entry.grid(row=idx, column=1, padx=5)

            # 3. Names Entry (joined by space)
            names_var = tk.StringVar(value = " ".join(entry.names) if hasattr(entry, 'names') and entry.names is not None else "")
            names_entry = tk.Entry(frame, textvariable=names_var, width=30)
            names_entry.grid(row=idx, column=2, padx=5)

            # Comment Entry
            comment_var = tk.StringVar(value=entry.comment if hasattr(entry, 'comment') else "")
            comment_entry = tk.Entry(frame, textvariable=comment_var, width=30)
            comment_entry.grid(row=idx, column=3, padx=5)
            
            self.fields.insert(idx, {
                "type": type_var,
                "ip": ip_entry,
                'names': names_entry,
                "comment": comment_entry
            })
            type_var.trace_add("write", lambda *args, i=idx: self.on_type_change(i))
            self.on_type_change(idx)


        # print(hosts)
        # hosts.import_url(DEFAULT_SYNC_SOURCE)
        # print("TRUE")
        return True

    def on_type_change(self, idx):
        fields = self.fields[idx]
        print(fields["type"].get())
        if fields["type"].get() == "comment":
            fields["ip"].grid_forget()
            fields["names"].grid_forget()
            fields["comment"].grid(row=idx, column=1, columnspan=3, sticky="ew", padx=5)
            fields["comment"].config(state='normal')
        elif fields["type"].get() == "blank":
            fields["ip"].grid_forget()
            fields["names"].grid_forget()
            fields["comment"].grid(row=idx, column=1, columnspan=3, sticky="ew", padx=5)
            fields["comment"].config(state='disabled')
        else:
            fields["ip"].grid(row=idx, column=1, padx=5)
            fields["names"].grid(row=idx, column=2, padx=5)
            fields["comment"].grid(row=idx, column=3, padx=5)
            fields["comment"].config(state='normal')

    def loadButtons(self, g):
        #Bottom frame (no fill/expand so it shrinks to fit its children)
        frame = tk.Frame(g, bg="#3a3a3a")
        frame.grid(row=99, sticky="s", pady=20) 
        
        btn_frame = tk.Frame(frame, bg="#3a3a3a")
        btn_frame.grid(row=0, sticky="nsew", pady=20)  

        #Two buttons, packed left-to-right
        sync_btn = tk.Button(btn_frame, text="Sync",  command=g.destroy, width=10, height=1)
        stop_btn = tk.Button(btn_frame, text="Exit", command=g.destroy, width=10, height=1)

        sync_btn.grid(row=0, column=0, padx=5)
        stop_btn.grid(row=0, column=1, padx=5)        