"""
CustomTkinter Messagebox
Author: Akash Bora
Version: 1.3
"""

import customtkinter
from PIL import Image
import os, sys

class CTkMessagebox(customtkinter.CTkToplevel):
    
    def __init__(self,
                 width: int = 400,
                 height: int = 200,
                 title: str = "CTkMessagebox",
                 message: str = "This is a CTkMessagebox!",
                 option_1: str = "OK",
                 option_2: str = None,
                 option_3: str = None,
                 border_width: int = 0,
                 border_color: str = "default",
                 button_color: str = "default",
                 bg_color: str = "default",
                 fg_color: str = "default",
                 text_color: str = "default",
                 title_color: str = "default",
                 button_text_color: str = "default",
                 button_width: int = None,
                 cancel_button_color: str = "#c42b1c",
                 icon: str = "info",
                 icon_size: tuple = None,
                 corner_radius: int = 15,
                 font: tuple = None):
        
        super().__init__()

        self.width = 250 if width<250 else width
        self.height = 180 if height<180 else  height
        self.spawn_x = int((self.winfo_screenwidth()-self.width)/2)
        self.spawn_y = int((self.winfo_screenheight()-self.height)/2)
        self.after(10)
        self.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")
        self.title(title)
        self.resizable(width=False, height=False)
        self.overrideredirect(1)
        self.attributes("-topmost", True)
        
        if sys.platform.startswith("win"):
            self.transparent_color = '#000001'
            self.attributes("-transparentcolor", self.transparent_color)
        elif sys.platform.startswith("darwin"):
            self.transparent_color = 'systemTransparent'
            self.attributes("-transparent", True)
        else:
            self.transparent_color = '#000001'
            corner_radius = 0
            
        self.config(background=self.transparent_color)
        self.protocol("WM_DELETE_WINDOW", self.button_event)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)    
        self.lift()
        
        self.x = self.winfo_x()
        self.y = self.winfo_y()
        self._title = title
        self.message = message
        self.font = font
        self.round_corners = corner_radius if corner_radius<=30 else 30
        self.button_width = button_width if button_width else self.width/4
        self.dot_color = cancel_button_color
        self.border_width = border_width if border_width<6 else 5
        
        if bg_color=="default":
            self.bg_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        else:
            self.bg_color = bg_color

        if fg_color=="default":
            self.fg_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"])
        else:
            self.fg_color = fg_color

        if button_color=="default":
            self.button_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])
        else:
            self.button_color = button_color

        if text_color=="default":
            self.text_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
        else:
            self.text_color = text_color

        if title_color=="default":
            self.title_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
        else:
            self.title_color = title_color
            
        if button_text_color=="default":
            self.bt_text_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["text_color"])
        else:
            self.bt_text_color = button_text_color
            
        if border_color=="default":
            self.border_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["border_color"])
        else:
            self.border_color = border_color
            
        if icon_size:
            self.size_height = icon_size[1] if icon_size[1]<=self.height-100 else self.height-100
            self.size = (icon_size[0], self.size_height)
        else:
            self.size = (self.height/4, self.height/4)
        
        if icon in ["check", "cancel", "info", "question", "warning"]:
            self.icon = customtkinter.CTkImage(Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons', icon+'.png')),
                                               size=self.size)
        else:
            self.icon = customtkinter.CTkImage(Image.open(icon), size=self.size) if icon else None

        self.frame_top = customtkinter.CTkFrame(self, corner_radius=self.round_corners, width=self.width, border_width=self.border_width,
                                                bg_color=self.transparent_color, fg_color=self.bg_color, border_color=self.border_color)
        self.frame_top.grid(sticky="nswe")
        self.frame_top.grid_columnconfigure((0,1,2), weight=1)
        self.frame_top.grid_rowconfigure((0,1,2), weight=1)
        self.frame_top.bind("<B1-Motion>", self.move_window)
        self.frame_top.bind("<ButtonPress-1>", self.oldxyset)
        
        self.button_close = customtkinter.CTkButton(self.frame_top, corner_radius=10, width=10, height=10, hover=False,
                                           text="", fg_color=self.dot_color, command=self.button_event)
        self.button_close.configure(cursor="arrow")        
        self.button_close.grid(row=0, column=2, sticky="ne", padx=10, pady=10)

        self.title_label = customtkinter.CTkLabel(self.frame_top, width=1, text=self._title, text_color=self.title_color, font=self.font)
        self.title_label.grid(row=0, column=0, columnspan=3, sticky="nw", padx=(15,30), pady=5)
        self.title_label.bind("<B1-Motion>", self.move_window)
        self.title_label.bind("<ButtonPress-1>", self.oldxyset)
        
        self.info = customtkinter.CTkButton(self.frame_top,  width=1, height=100, corner_radius=0, text=self.message, font=self.font,
                                            fg_color=self.fg_color, hover=False, text_color=self.text_color, image=self.icon)
        self.info._text_label.configure(wraplength=self.width/2, justify="left")
        self.info.grid(row=1, column=0, columnspan=3, sticky="nwes", padx=self.border_width)
        
        self.option_text_1 = option_1
        self.button_1 = customtkinter.CTkButton(self.frame_top, text=self.option_text_1, fg_color=self.button_color,
                                                width=self.button_width, font=self.font, text_color=self.bt_text_color,
                                                command=lambda: self.button_event(self.option_text_1))
        self.button_1.grid(row=2, column=2, sticky="news", padx=(0,10), pady=10)

        if option_2:
            self.option_text_2 = option_2      
            self.button_2 = customtkinter.CTkButton(self.frame_top, text=self.option_text_2, fg_color=self.button_color,
                                                    width=self.button_width, font=self.font, text_color=self.bt_text_color,
                                                    command=lambda: self.button_event(self.option_text_2))
            self.button_2.grid(row=2, column=1, sticky="news", padx=10, pady=10)
            
        if option_3:
            self.option_text_3 = option_3
            self.button_3 = customtkinter.CTkButton(self.frame_top, text=self.option_text_3, fg_color=self.button_color,
                                                    width=self.button_width, font=self.font, text_color=self.bt_text_color,
                                                    command=lambda: self.button_event(self.option_text_3))
            self.button_3.grid(row=2, column=0, sticky="news", padx=(10,0), pady=10)
            
        self.grab_set()
        
    def get(self):
        self.master.wait_window(self)
        return self.event
        
    def oldxyset(self, event):
        self.oldx = event.x
        self.oldy = event.y
    
    def move_window(self, event):
        self.y = event.y_root - self.oldy
        self.x = event.x_root - self.oldx
        self.geometry(f'+{self.x}+{self.y}')
        
    def button_event(self, event=None):
        self.grab_release()
        self.destroy()
        self.event = event
    
if __name__ == "__main__":
    app = CTkMessagebox()
    app.mainloop()
