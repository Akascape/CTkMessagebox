"""
CustomTkinter Messagebox
Author: Akash Bora
Version: 2.5
"""

import customtkinter
from PIL import Image, ImageTk
import os
import sys
import time
from typing import Literal

class CTkMessagebox(customtkinter.CTkToplevel):
    ICONS = {
        "check": None,
        "cancel": None,
        "info": None,
        "question": None,
        "warning": None
    }
    ICON_BITMAP = {}
    def __init__(self,
                 master: any = None,
                 width: int = 400,
                 height: int = 200,
                 title: str = "CTkMessagebox",
                 message: str = "This is a CTkMessagebox!",
                 option_1: str = "OK",
                 option_2: str = None,
                 option_3: str = None,
                 options: list = [],
                 border_width: int = 1,
                 border_color: str = "default",
                 button_color: str = "default",
                 bg_color: str = "default",
                 fg_color: str = "default",
                 text_color: str = "default",
                 title_color: str = "default",
                 button_text_color: str = "default",
                 button_width: int = None,
                 button_height: int = None,
                 cancel_button_color: str = None,
                 cancel_button: str = None, # types: circle, cross or none
                 button_hover_color: str = "default",
                 icon: str = "info",
                 icon_size: tuple = None,
                 corner_radius: int = 15,
                 justify: str = "right",
                 font: tuple = None,
                 header: bool = False,
                 topmost: bool = True,
                 fade_in_duration: int = 0,
                 sound: bool = False,
                 option_focus: Literal[1, 2, 3] = None):
        
        super().__init__()
        
        
        self.master_window = master
     
        self.width = 250 if width<250 else width
        self.height = 150 if height<150 else  height
            
        if self.master_window is None:
            self.spawn_x = int((self.winfo_screenwidth()-self.width)/2)
            self.spawn_y = int((self.winfo_screenheight()-self.height)/2)
        else:
            self.spawn_x = int(self.master_window.winfo_width() * .5 + self.master_window.winfo_x() - .5 * self.width + 7)
            self.spawn_y = int(self.master_window.winfo_height() * .5 + self.master_window.winfo_y() - .5 * self.height + 20)
            
        self.after(10)
        self.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")
        self.title(title)
        self.resizable(width=False, height=False)
        self.fade = fade_in_duration
        
        if self.fade:
            self.fade = 20 if self.fade<20 else self.fade
            self.attributes("-alpha", 0)
        
        if not header:
            self.overrideredirect(1)
            
        if topmost:
            self.attributes("-topmost", True)
        else:
            self.transient(self.master_window)
    
        if sys.platform.startswith("win"):
            self.transparent_color = self._apply_appearance_mode(self.cget("fg_color"))
            self.attributes("-transparentcolor", self.transparent_color)
            default_cancel_button = "cross"
        elif sys.platform.startswith("darwin"):
            self.transparent_color = 'systemTransparent'
            self.attributes("-transparent", True)
            default_cancel_button = "circle"
        else:
            self.transparent_color = '#000001'
            corner_radius = 0
            default_cancel_button = "cross"

        self.lift()
        
        self.config(background=self.transparent_color)
        self.protocol("WM_DELETE_WINDOW", self.button_event)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)    
        self.x = self.winfo_x()
        self.y = self.winfo_y()
        self._title = title
        self.message = message
        self.font = font
        self.justify = justify
        self.sound = sound
        self.cancel_button = cancel_button if cancel_button else default_cancel_button      
        self.round_corners = corner_radius if corner_radius<=30 else 30
        self.button_width = button_width if button_width else self.width/4
        self.button_height = button_height if button_height else 28
  
        if self.fade: self.attributes("-alpha", 0)
        
        if self.button_height>self.height/4: self.button_height = self.height/4 -20
        self.dot_color = cancel_button_color
        self.border_width = border_width if border_width<6 else 5
        
        if type(options) is list and len(options)>0:
            try:
                option_1 = options[-1]
                option_2 = options[-2]
                option_3 = options[-3]
            except IndexError: None
            
        if bg_color=="default":
            self.bg_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        else:
            self.bg_color = bg_color

        if fg_color=="default":
            self.fg_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"])
        else:
            self.fg_color = fg_color
            
        default_button_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])

        if sys.platform.startswith("win"):
            if self.bg_color==self.transparent_color or self.fg_color==self.transparent_color:
                self.configure(fg_color="#000001")
                self.transparent_color = "#000001"
                self.attributes("-transparentcolor", self.transparent_color)

        if button_color=="default":
            self.button_color = (default_button_color, default_button_color, default_button_color)
        else:
            if type(button_color) is tuple:
                if len(button_color)==2:                
                    self.button_color = (button_color[0], button_color[1], default_button_color)
                elif len(button_color)==1:
                    self.button_color = (button_color[0], default_button_color, default_button_color)
                else:
                    self.button_color = button_color
            else:
                self.button_color = (button_color, button_color, button_color)

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

        if button_hover_color=="default":
            self.bt_hv_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["hover_color"])
        else:
            self.bt_hv_color = button_hover_color
            
        if border_color=="default":
            self.border_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["border_color"])
        else:
            self.border_color = border_color
            
        if icon_size:
            self.size_height = icon_size[1] if icon_size[1]<=self.height-100 else self.height-100
            self.size = (icon_size[0], self.size_height)
        else:
            self.size = (self.height/4, self.height/4)
        
        self.icon = self.load_icon(icon, icon_size) if icon else None
        
        self.frame_top = customtkinter.CTkFrame(self, corner_radius=self.round_corners, width=self.width, border_width=self.border_width,
                                                bg_color=self.transparent_color, fg_color=self.bg_color, border_color=self.border_color)
        self.frame_top.grid(sticky="nswe")

        if button_width:
            self.frame_top.grid_columnconfigure(0, weight=1)
        else:
            self.frame_top.grid_columnconfigure((1,2,3), weight=1)

        if button_height:
            self.frame_top.grid_rowconfigure((0,1,3), weight=1)
        else:
            self.frame_top.grid_rowconfigure((0,1,2), weight=1)
            
        self.frame_top.bind("<B1-Motion>", self.move_window)
        self.frame_top.bind("<ButtonPress-1>", self.oldxyset)

        if self.cancel_button=="cross":
            self.button_close = customtkinter.CTkButton(self.frame_top, corner_radius=10, width=0, height=0, hover=False, border_width=0,
                                                        text_color=self.dot_color if self.dot_color else self.title_color,
                                                      text="✕", fg_color="transparent", command=self.button_event)
            self.button_close.grid(row=0, column=5, sticky="ne", padx=5+self.border_width, pady=5+self.border_width)
        elif self.cancel_button=="circle":
            self.button_close = customtkinter.CTkButton(self.frame_top, corner_radius=10, width=10, height=10, hover=False, border_width=0,
                                                        text="", fg_color=self.dot_color if self.dot_color else "#c42b1c", command=self.button_event)     
            self.button_close.grid(row=0, column=5, sticky="ne", padx=10, pady=10)       
            
        self.title_label = customtkinter.CTkLabel(self.frame_top, width=1, text=self._title, text_color=self.title_color, font=self.font)
        self.title_label.grid(row=0, column=0, columnspan=6, sticky="nw", padx=(15,30), pady=5)
        self.title_label.bind("<B1-Motion>", self.move_window)
        self.title_label.bind("<ButtonPress-1>", self.oldxyset)
        
        self.info = customtkinter.CTkButton(self.frame_top,  width=1, height=self.height/2, corner_radius=0, text=self.message, font=self.font,
                                            fg_color=self.fg_color, hover=False, text_color=self.text_color, image=self.icon)
        self.info._text_label.configure(wraplength=self.width/2, justify="left")
        self.info.grid(row=1, column=0, columnspan=6, sticky="nwes", padx=self.border_width)
        
        if self.info._text_label.winfo_reqheight()>self.height/2:
            height_offset = int((self.info._text_label.winfo_reqheight())-(self.height/2) + self.height)
            self.geometry(f"{self.width}x{height_offset}")


        self.option_text_1 = option_1
        
        self.button_1 = customtkinter.CTkButton(self.frame_top, text=self.option_text_1, fg_color=self.button_color[0],
                                                width=self.button_width, font=self.font, text_color=self.bt_text_color,
                                                hover_color=self.bt_hv_color, height=self.button_height,
                                                command=lambda: self.button_event(self.option_text_1))
        

        self.option_text_2 = option_2 
        if option_2:     
            self.button_2 = customtkinter.CTkButton(self.frame_top, text=self.option_text_2, fg_color=self.button_color[1],
                                                    width=self.button_width, font=self.font, text_color=self.bt_text_color,
                                                    hover_color=self.bt_hv_color, height=self.button_height,
                                                    command=lambda: self.button_event(self.option_text_2))

        self.option_text_3 = option_3
        if option_3:
            self.button_3 = customtkinter.CTkButton(self.frame_top, text=self.option_text_3, fg_color=self.button_color[2],
                                                    width=self.button_width, font=self.font, text_color=self.bt_text_color,
                                                    hover_color=self.bt_hv_color, height=self.button_height,
                                                    command=lambda: self.button_event(self.option_text_3))
            
        if self.justify=="center":
            if button_width:
                columns = [4,3,2]
                span = 1
            else:
                columns = [4,2,0]
                span = 2
            if option_3:
                self.frame_top.columnconfigure((0,1,2,3,4,5), weight=1)
                self.button_1.grid(row=2, column=columns[0], columnspan=span, sticky="news", padx=(0,10), pady=10) 
                self.button_2.grid(row=2, column=columns[1], columnspan=span, sticky="news", padx=10, pady=10)
                self.button_3.grid(row=2, column=columns[2], columnspan=span, sticky="news", padx=(10,0), pady=10)
            elif option_2:
                self.frame_top.columnconfigure((0,5), weight=1)
                columns = [2,3]
                self.button_1.grid(row=2, column=columns[0], sticky="news", padx=(0,5), pady=10)
                self.button_2.grid(row=2, column=columns[1], sticky="news", padx=(5,0), pady=10)
            else:
                if button_width:
                    self.frame_top.columnconfigure((0,1,2,3,4,5), weight=1)
                else:
                    self.frame_top.columnconfigure((0,2,4), weight=2)
                self.button_1.grid(row=2, column=columns[1], columnspan=span, sticky="news", padx=(0,10), pady=10)   
        elif self.justify=="left":
            self.frame_top.columnconfigure((0,1,2,3,4,5), weight=1)
            if button_width:
                columns = [0,1,2]
                span = 1
            else:        
                columns = [0,2,4]
                span = 2
            if option_3:
                self.button_1.grid(row=2, column=columns[2], columnspan=span, sticky="news", padx=(0,10), pady=10)
                self.button_2.grid(row=2, column=columns[1], columnspan=span, sticky="news", padx=10, pady=10)
                self.button_3.grid(row=2, column=columns[0], columnspan=span, sticky="news", padx=(10,0), pady=10)
            elif option_2:
                self.button_1.grid(row=2, column=columns[1], columnspan=span, sticky="news", padx=10, pady=10)
                self.button_2.grid(row=2, column=columns[0], columnspan=span, sticky="news", padx=(10,0), pady=10)
            else:
                self.button_1.grid(row=2, column=columns[0], columnspan=span, sticky="news", padx=(10,0), pady=10)
        else:
            self.frame_top.columnconfigure((0,1,2,3,4,5), weight=1)
            if button_width:
                columns = [5,4,3]
                span = 1
            else:
                columns = [4,2,0]
                span = 2
            self.button_1.grid(row=2, column=columns[0], columnspan=span, sticky="news", padx=(0,10), pady=10)
            if option_2:  
                self.button_2.grid(row=2, column=columns[1], columnspan=span, sticky="news", padx=10, pady=10)
            if option_3:
                self.button_3.grid(row=2, column=columns[2], columnspan=span, sticky="news", padx=(10,0), pady=10)
                        
        if header:
            self.title_label.configure(text="")
            self.title_label.grid_configure(pady=0)
            self.button_close.configure(text_color=self.bg_color)
            self.frame_top.configure(corner_radius=0)

        if self.winfo_exists():
            self.grab_set()

        if self.sound:
            self.bell()
            
        if self.fade:
            self.fade_in()
            
        if option_focus:
            self.option_focus = option_focus
            self.focus_button(self.option_focus)
        else:
            if not self.option_text_2 and not self.option_text_3:
                self.button_1.focus()
                self.button_1.bind("<Return>", lambda event: self.button_event(self.option_text_1))
 
        self.bind("<Escape>", lambda e: self.button_event())
        
    def focus_button(self, option_focus):
        try:
            self.selected_button = getattr(self, "button_"+str(option_focus))
            self.selected_button.focus()
            self.selected_button.configure(border_color=self.bt_hv_color, border_width=3)
            self.selected_option = getattr(self, "option_text_"+str(option_focus))
            self.selected_button.bind("<Return>", lambda event: self.button_event(self.selected_option))
        except AttributeError:
            return
        
        self.bind("<Left>", lambda e: self.change_left())
        self.bind("<Right>", lambda e: self.change_right())
        
    def change_left(self):
        if self.option_focus==3:
            return
        
        self.selected_button.unbind("<Return>")
        self.selected_button.configure(border_width=0)
    
        if self.option_focus==1:
            if self.option_text_2:
                self.option_focus = 2
        
        elif self.option_focus==2:
            if self.option_text_3:
                self.option_focus = 3
  
        self.focus_button(self.option_focus)
        
    def change_right(self):
        if self.option_focus==1:
            return
        
        self.selected_button.unbind("<Return>")
        self.selected_button.configure(border_width=0)

        if self.option_focus==2:
            self.option_focus = 1

        elif self.option_focus==3:
            self.option_focus = 2
                
        self.focus_button(self.option_focus)
    
    def load_icon(self, icon, icon_size):
        if icon not in self.ICONS or self.ICONS[icon] is None:
            if icon in ["check", "cancel", "info", "question", "warning"]:
                image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons', icon + '.png')
            else:
                image_path = icon
            if icon_size:
                size_height = icon_size[1] if icon_size[1] <= self.height - 100 else self.height - 100
                size = (icon_size[0], size_height)
            else:
                size = (self.height / 4, self.height / 4)
            self.ICONS[icon] = customtkinter.CTkImage(Image.open(image_path), size=size)
            self.ICON_BITMAP[icon] = ImageTk.PhotoImage(file=image_path)
        self.after(200, lambda: self.iconphoto(False, self.ICON_BITMAP[icon]))
        return self.ICONS[icon]
        
    def fade_in(self):
        for i in range(0,110,10):
            if not self.winfo_exists():
                break
            self.attributes("-alpha", i/100)
            self.update()
            time.sleep(1/self.fade)
            
    def fade_out(self):
        for i in range(100,0,-10):
            if not self.winfo_exists():
                break
            self.attributes("-alpha", i/100)
            self.update()
            time.sleep(1/self.fade)

    def get(self):
        if self.winfo_exists():
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
        try:
            self.button_1.configure(state="disabled")
            self.button_2.configure(state="disabled")
            self.button_3.configure(state="disabled")
        except AttributeError:
            pass

        if self.fade:
            self.fade_out()
        self.grab_release()
        self.destroy()
        self.event = event  
        
if __name__ == "__main__":
    app = CTkMessagebox()
    app.mainloop()
