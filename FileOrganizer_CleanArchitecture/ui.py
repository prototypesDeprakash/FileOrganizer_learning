import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("Dark")

GREEN = "#00ff66"
BG = "#050505"
FRAME = "#111111"

app = ctk.CTk()
app.title("FILEZ v2.1")
app.geometry("760x600")
app.configure(fg_color=BG)
app.resizable(False, False)

# ============================
# Title
# ============================

title = ctk.CTkLabel(
    app,
    text="""==========================================
        FILEZ v2.1 TERMINAL
==========================================""",
    font=("Consolas",18,"bold"),
    text_color=GREEN,
    justify="left"
)
title.pack(anchor="w", padx=30, pady=(20,25))


# ============================
# Target Directory
# ============================

def browse_folder():
    global selected_directory

    folder = filedialog.askdirectory(
        title="Select Target Directory"
    )

    if folder:
        selected_directory = folder

        directory.configure(state="normal")
        directory.delete("1.0", "end")
        directory.insert("1.0", f"> {folder}")
        directory.configure(state="disabled")


# ============================
# Target Directory
# ============================

label = ctk.CTkLabel(
    app,
    text="TARGET DIRECTORY",
    font=("Consolas", 16, "bold"),
    text_color=GREEN
)
label.pack(anchor="w", padx=30)

directory = ctk.CTkTextbox(
    app,
    height=35,
    width=680,
    fg_color=FRAME,
    border_width=1,
    border_color=GREEN,
    text_color=GREEN,
    font=("Consolas", 15)
)
directory.pack(padx=30, pady=(8, 18))

# Default text
directory.insert("1.0", "> No directory selected")
directory.configure(state="disabled")

browse = ctk.CTkButton(
    app,
    text="[ BROWSE ]",
    width=200,
    height=38,
    fg_color=FRAME,
    hover_color="#1a1a1a",
    border_width=1,
    border_color=GREEN,
    text_color=GREEN,
    corner_radius=0,
    font=("Consolas", 15, "bold"),
    command=browse_folder
)
browse.pack(anchor="w", padx=30)
# ============================
# Divider
# ============================

divider1 = ctk.CTkLabel(
    app,
    text="",
    font=("Consolas",16),
    text_color=GREEN
)
divider1.pack(anchor="w", padx=15, pady=10)

# ============================
# Ready
# ============================

ready = ctk.CTkLabel(
    app,
    text="READY",
    font=("Consolas",17,"bold"),
    text_color=GREEN
)
ready.pack(anchor="w", padx=30)

start = ctk.CTkButton(
    app,
    text="[ INITIALIZE ORGANIZATION ]",
    width=330,
    height=40,
    fg_color=FRAME,
    hover_color="#1a1a1a",
    border_width=1,
    border_color=GREEN,
    text_color=GREEN,
    corner_radius=0,
    font=("Consolas",15,"bold")
)
start.pack(anchor="w", padx=30, pady=(15,20))



# ============================
# Status
# ============================

status_label = ctk.CTkLabel(
    app,
    text="STATUS",
    font=("Consolas",16,"bold"),
    text_color=GREEN
)
status_label.pack(anchor="w", padx=30, pady=(18,10))

status = ctk.CTkTextbox(
    app,
    width=680,
    height=170,
    fg_color=FRAME,
    border_width=1,
    border_color=GREEN,
    text_color=GREEN,
    font=("Consolas",15)
)
status.pack(padx=30)

status.insert("end","> Scanning...\n")
status.insert("end","> 152 Files Detected\n")
status.insert("end","> 18 Categories Created\n")
status.insert("end","> Moving Files...\n")
status.insert("end","> Complete.")
for i in range(50):
    status.insert("end", f"> Status Message {i+1}\n")
status.configure(state="disabled")

app.mainloop()