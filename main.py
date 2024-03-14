from script import main
import customtkinter as tk

def script_gui():

    tk.set_appearance_mode('dark')
    tk.set_default_color_theme('dark-blue')
    root = tk.CTk()

    root.resizable(0,0)

    root.title('[Discord: dz6k]')

    root.geometry('250x100')
    tk.set_widget_scaling(1.1)

    frame = tk.CTkFrame(master=root)
    frame.pack(pady=10,padx=10,fill='both',expand=True)
    

    button_stealth_farm = tk.CTkButton(master=frame,text='Start', command=main)
    button_stealth_farm.pack(padx=12,pady=10)

    
    texto = tk.CTkLabel(frame,
                        text='!!! Press "CTRL+E" for stop script !!!',
                        font=('unispace',13),
                        text_color='#abd11f').pack(padx=2,pady=1)
    root.mainloop()


if __name__ == '__main__':
    script_gui()