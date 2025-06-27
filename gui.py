import customtkinter as ctk

def create_gui():
    ctk.set_appearance_mode("dark")  # or "light" or "system"
    ctk.set_default_color_theme("blue")  # themes: blue, dark-blue, green

    g = ctk.CTk()
    g.overrideredirect(True)
    ctk.CTkFrame(g, corner_radius=15, fg_color="#2b2b2b")
    g.geometry("400x400")

    create_btns(g)
    return g;

def create_btns(gui):
    frame = ctk.CTkFrame(gui)
    frame.pack(side='bottom', pady=20)

    sync_btn = ctk.CTkButton(frame, text="start", command=gui.destroy, width=10, height=1)
    stop_btn = ctk.CTkButton(frame, text="Finish", command=gui.destroy, width=10, height=1)

    sync_btn.pack(side="left", padx=5)
    stop_btn.pack(side="left", padx=5)
    

def open_gui():
    g = create_gui()
    g.mainloop()