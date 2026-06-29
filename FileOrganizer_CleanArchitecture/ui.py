from customtkinter import *
from tkinter import filedialog
app =  CTk()
app.geometry("800x600")
app.title("FIlz")
set_appearance_mode("System")
app.resizable(width=True,height=True)

#theme Design

BG = "#F8F7FF"
FRAME = "#FFFFFF"
CARD = "#FCFBFF"
HEADER = "#FFFFFF"

ACCENT = "#8B5CF6"

TEXT = "#1F2937"
SUBTEXT = "#6B7280"

BUTTON = "#8B5CF6"
BUTTON_HOVER = "#7C3AED"

BORDER = "#E9D5FF"
app.configure(fg_color=BG)

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
frame4 = CTkFrame(app, fg_color=FRAME, border_color=ACCENT)
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
        directory_entry.delete(0, END)
        directory_entry.insert(0, folder)
        
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



app.mainloop()

'''
ui idea
frame1 -> title 
frame2 -> browse with a button
frame3 -> organize button
frame4 -> textbox_summary
'''