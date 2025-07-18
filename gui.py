import customtkinter as ctk
from PIL import Image

#Window settings
window = ctk.CTk()
window.geometry("144x144")
window.title("COMLOCK UI")
window.resizable(0,0)
#End of window settings


#Background
background_image_path = "images/comlock.png"
background_image = Image.open(background_image_path)
ctk_background_image = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(144, 144))
#End of background


#Buttons
#def go_home():
    

def start_call():
    call_btn.place_forget()
    go_home_btn.place(relx=0.5, rely=0.88, anchor="center")
#End of buttons


#Display background
image_label = ctk.CTkLabel(window, image=ctk_background_image, text ="")
image_label.place(relx=0, rely=0)
#End of display background

#Home button
go_home_btn = ctk.CTkButton(window, text="HOME", border_width=3, border_color="black", 
                            corner_radius=20, bg_color="transparent",  width=20,height=20)
go_home_btn.place(relx=0.7, rely=0.88, anchor="center")
#End of home button

#Call button
call_btn = ctk.CTkButton(window, text="CALL", border_width=3, border_color="black", 
                         corner_radius=20, bg_color="transparent", width=20,height=20,
                         command=start_call)
call_btn.place(relx=0.3, rely=0.88, anchor="center")
#Call of home button




window.mainloop()