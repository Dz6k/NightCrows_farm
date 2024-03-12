from script import main
import customtkinter as tk



import customtkinter as ctk
from customtkinter import CTkImage
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = ctk.CTk()
win.resizable(0,0)
# Define the geometry of the window
win.geometry("300x300")
win.title('Donate pix')
frame = ctk.CTkFrame(win, width=300, height=300)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = Image.open("pix.png")
img = CTkImage(light_image=Image.open("pix.png"),
               dark_image=Image.open("pix.png"),
               size=(295, 295))

# Create a Label Widget to display the text or Image
label = ctk.CTkLabel(frame, text=None, image=img)
label.pack()

win.mainloop()


def script_gui():
    # visual
    tk.set_appearance_mode('dark')
    tk.set_default_color_theme('dark-blue')
    # definindo variavel
    root = tk.CTk()
    # remove opcao "maximizar" do windows
    root.resizable(0,0)
    # titulo da janela 
    root.title('[Discord: dz6k]')
    # dimensao
    root.geometry('250x100')
    tk.set_widget_scaling(1.1)

    frame = tk.CTkFrame(master=root)
    frame.pack(pady=10,padx=10,fill='both',expand=True)
    
    # modos
    button_stealth_farm = tk.CTkButton(master=frame,text='Start', command=main)
    button_stealth_farm.pack(padx=12,pady=10)

    
    texto = tk.CTkLabel(frame,
                        text='!!! Press "CTRL+E" for stop script !!!',
                        font=('unispace',13),
                        text_color='#abd11f').pack(padx=2,pady=1)
    root.mainloop()


if __name__ == '__main__':
    script_gui()