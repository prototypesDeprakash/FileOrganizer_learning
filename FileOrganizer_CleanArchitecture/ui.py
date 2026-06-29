from customtkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter
from tkinter import StringVar
from organizer import FileOrganizer

def start_ui():
    app =  CTk()
    app.geometry("800x600")
    app.title("FIlz")
    set_appearance_mode("System")
    app.resizable(width=False,height=True)






    #theme Design
    BG = "#121212"          # Window background
    FRAME = "#1B1B1B"       # Panels
    CARD = "#242424"        # Cards
    HEADER = "#181818"      # Header
    ACCENT = "#E53935"      # Fire red
    TEXT = "#F5F5F5"
    SUBTEXT = "#A8A8A8"
    BUTTON = "#E53935"
    BUTTON_HOVER = "#C62828"
    BORDER = "#8B1E1E"
    GREY='#222222'
    app.configure(fg_color=BG)


    #Global variables
    directory_path = StringVar()

    #layout design
    #frame1 = CTkFrame(master=app,fg_color=FRAME,height=50)
    frame1 = CTkFrame(app, fg_color=HEADER, border_color=ACCENT, border_width=1)
    frame1.pack(fill="x",padx=20, pady=10)

    #frame2 = CTkFrame(master=app,fg_color=CARD,height=250)
    frame2 = CTkFrame(app, fg_color=FRAME, border_color=ACCENT)
    frame2.pack(fill="x",padx=20, pady=10)

    #frame3 = CTkFrame(master=app,fg_color=CARD,height=150)
    frame3 = CTkFrame(app, fg_color=FRAME, border_color=ACCENT)
    frame3.pack(fill="x")

    #frame4 = CTkFrame(master=app,fg_color=FRAME,height=200)
    frame4 = CTkFrame(app, fg_color=GREY, border_color=ACCENT,height=250)
    frame4.pack(fill="both",expand=True)



    #title ->frame1
    title = CTkLabel(
        frame1,
        text="TidyDir v1.0.0",
        font=("Consolas", 22, "bold"),
        text_color=ACCENT
    )
    title.pack(expand=True)

    #fileBrowser ->frame2

    # Heading
    heading = CTkLabel(
        frame2,
        text="Target Directory",
        font=("Consolas", 18, "bold"),
        text_color=ACCENT
    )
    heading.pack(anchor="center", pady=(10, 5))

    # Entry + Button
    path_frame = CTkFrame(frame2, fg_color="transparent")
    path_frame.pack(fill="x")

    directory_entry = CTkEntry(
        path_frame,
        textvariable=directory_path,
        placeholder_text="Select a folder...",
        height=40,
        fg_color=FRAME,
        border_color=ACCENT,
        border_width=1,
        text_color=ACCENT,
        placeholder_text_color="#4D4D4D",
        font=("Consolas", 14)
    )

    directory_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
    def browse_folder():
        folder = filedialog.askdirectory()
        if folder:
            directory_path.set(folder)
            
    browse_button = CTkButton(
        path_frame,
        text="BROWSE",
        command=browse_folder,
        width=120,
        fg_color=ACCENT,
        hover_color=BUTTON_HOVER,
        text_color="#000000",    # Black text
        font=("Consolas", 14, "bold")
    )
    browse_button.pack(side="right")

    #start organize button and callback

    org = FileOrganizer()
    def start_organizer():
        selected_folder = directory_path.get()
       # print(selected_folder)
        org.run(selected_folder)
        display_summary(org.summary_list)
        

    start_button = CTkButton(
        frame3,
        text="START",
        command=start_organizer,
        width=200,
        height=45,
        fg_color=BUTTON,
        hover_color=BUTTON_HOVER,
        text_color="white",
        font=("Consolas", 16, "bold"),
        corner_radius=8
    )

    start_button.pack(pady=20)

    #Summary text box
    summary_box = CTkTextbox(
        frame4,
        fg_color=GREY,
        border_color=ACCENT,
        border_width=1,
        text_color="#1aff00",
        font=("Consolas", 13),
        wrap="none",
        
    )
  

    summary_box.pack(fill="both", expand=True, padx=15, pady=15)
    def display_summary(summary_list):
        summary_box.configure(state="normal")
        summary_box.delete("1.0", END)
        for line in summary_list:
            summary_box.insert(END, line + "\n")
        summary_box.configure(state="disabled")
    
    app.mainloop()

    '''
    ui idea
    frame1 -> title 
    frame2 -> browse with a button
    frame3 -> organize button
    frame4 -> textbox_summary
    '''