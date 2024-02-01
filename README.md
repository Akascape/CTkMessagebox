<h1 align="center">CTkMessagebox</h1>

<h3 align="center">A modern and fully customizable messagebox for CustomTkinter, A must-have extension pack!</h3>

<div align="center">
    
  <a href="https://creativecommons.org/publicdomain/zero/1.0/">![License](https://img.shields.io/badge/License-CC0_1.0-blue)</a>
  <a href="https://github.com/Akascape/CTkMessagebox/archive/refs/heads/main.zip">![Download](https://img.shields.io/badge/Source_Code-Download-blue)</a>
  [![PyPI](https://img.shields.io/pypi/v/CTkMessagebox?style=flat)](https://pypi.org/project/CTkMessagebox)
  [![Downloads](https://static.pepy.tech/badge/ctkmessagebox)](https://pepy.tech/project/ctkmessagebox)
  ![Platform](https://img.shields.io/powershellgallery/p/Pester?color=blue)
</div>


<div align="center">

![3d](https://github.com/Akascape/CTkMessagebox/assets/89206401/cce577fc-6426-4c09-96f9-ede88caf7784)

</div>

<br>

<h2 align="center"> Features </h2>

- Customize all elements inside the messagebox
- Add custom icons or images
- Add multiple options according to your wish
- No ugly looking header or borders
- Comes with **5 default icons**
- Spawns at center of the screen/app
- Draggable window
- Fade-in/Fade-out window effect

<br>

<h2 align="center"> Installation </h2>

<div align="center">

```
pip install CTkMessagebox
```

[<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Akascape/CTkMessagebox?&color=green&label=Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="300">](https://github.com/Akascape/CTkMessagebox/archive/refs/heads/main.zip)


</div>

<p align="center"> 
    
<br>

<h2 align="center"> How it looks? </h2>

<div align="center">

![Screenshot](https://user-images.githubusercontent.com/89206401/221258593-75058878-b598-40c3-828a-1d44a6cefb73.jpg)

</div>

<br>

<h2 align="center"> Example </h2>

```python
from CTkMessagebox import CTkMessagebox
import customtkinter

def show_info():
    # Default messagebox for showing some information
    CTkMessagebox(title="Info", message="This is a CTkMessagebox!")

def show_checkmark():
    # Show some positive message with the checkmark icon
    CTkMessagebox(message="CTkMessagebox is successfully installed.",
                  icon="check", option_1="Thanks")
    
def show_error():
    # Show some error message
    CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
    
def show_warning():
    # Show some retry/cancel warnings
    msg = CTkMessagebox(title="Warning Message!", message="Unable to connect!",
                  icon="warning", option_1="Cancel", option_2="Retry")
    
    if msg.get()=="Retry":
        show_warning()
        
def ask_question():
    # get yes/no answers
    msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
    response = msg.get()
    
    if response=="Yes":
        app.destroy()       
    else:
        print("Click 'Yes' to exit!")
              
app = customtkinter.CTk()
app.rowconfigure((0,1,2,3,4,5), weight=1)
app.columnconfigure(0, weight=1)
app.minsize(200,250)

customtkinter.CTkLabel(app, text="CTk Messagebox Examples").grid(padx=20)
customtkinter.CTkButton(app, text="Check CTkMessagebox", command=show_checkmark).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Info", command=show_info).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Error", command=show_error).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Warning", command=show_warning).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Ask Question", command=ask_question).grid(padx=20, pady=(10,20), sticky="news")

app.mainloop()

```

<br>

<h2 align="center"> OPTIONS </h2>

<div align="center">

  | Parameters  | Description |
  | -------- | ----------- |
  | _master_ | set parent window (optional), the box will spawn at center of the parent window |
  | _width_ | width of the window in px (optional) |
  | _height_ | height of the window in px (optional) |
  | _fg_color_ | forground color of the messagebox [middle portion] |
  | _bg_color_  | background color of the messagebox |
  | **_title_** | title of the messagebox |
  | **_message_** | main message of the messagebox which will be shown at the center |
  | **_option_1_** | the text on the first button [Default is 'OK'] |
  | **_option_2_** | the text on the second button |
  | **_option_3_** | the text on the last button |
  | _options_ | directly pass a list containing the options in order |
  | _button_color_ | color of the buttons |
  | _text_color_ | color of the message-text |
  | _title_color_ | color of the title-text |
  | _button_text_color_ | color of the button-text |
  | _button_hover_color_ | hover color of the buttons |
  | _button_width_ | width of the buttons in px |
  | _button_height_ | height of the buttons in px |
  | _border_width_ | width of the border around the main frame [Default is 1] |
  | _border_color_ | color of the frame border |
  | _cancel_button_ | define the cancel button type: **circle, cross or None** |
  | _cancel_button_color_ | color of the **close** button, **set it to 'transparent' if you want to hide it** |
  | **_icon_** | icon that will be shown in the messagebox [Default is the 'info' icon] |
  | _icon_size_ | define the size of the icon image manually (tuple) |
  | _corner_radius_ | corner roundness of the messagebox window [**not applicable in linux**] |
  | _font_ | font of the messagebox text (tuple) |
  | _header_ | add the original header back if you don't like **overrideredirect** (bool) |
  | _topmost_ | disable the topmost window outside the app (bool) |
  | _sound_ | enable the system bell sound when the window popups (bool) |
  | _justify_ | position the buttons to center/right/left |
  | _option_focus_ | select an option by default when `Enter` key is pressed |
  | **_fade_in_duration_** | enable a fade-in and fade-out animation (int, default is 0)  |
  

</div>

<br>

<h2 align="center"> Icons </h2>

<div align="center">

**Default icons:**

![icons](https://user-images.githubusercontent.com/89206401/221258403-aafea575-856e-4f4e-b3af-f995785c9879.png)

(*These icons are created using Paint.NET, free to use!*)

**For custom images, just use `icon="image_path.png"`**

## That's all, hope it will help in UI development! 

</div>
