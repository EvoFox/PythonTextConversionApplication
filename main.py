#Libraries
import tkinter as ui
from tkinter.constants import DISABLED, LEFT, NORMAL, RIGHT
from typing import Text
import owo, l337


#Functions


def convert():
    txt_output.configure(state=NORMAL)
    if selected.get() == option_list[0]:
        # L337
        txt_output.delete(1.0, "end")
        txt_output.insert(1.0, l337.hacker_speak(txt_input.get(1.0, 'end-1c')))
    elif selected.get() == option_list[1]:
        # RaNDom cApS
        txt_output.delete(1.0, "end")
        # txt_output.insert(1.0, owo.owoify(txt_input.get(1.0, 'end-1c')))
    else:
        # OwO Speak
        txt_output.delete(1.0, "end")
        txt_output.insert(1.0, owo.owoify(txt_input.get(1.0, 'end-1c')))
    txt_output.configure(state=DISABLED)
    # print(f"Option menu: {selected.get()}, Text: {txt_input.get(1.0, 'end-1c')}") 

#Create a window
root = ui.Tk()
root.title("Text Conversion Application")


root.geometry("1920x1000")
root.minsize(600,600)
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1, minsize=20)
root.columnconfigure(2, weight=3)


lbl_text = ui.Label(text="Text Conversion Application!")
lbl_text.configure(font=("Helvetica", 28, "bold"))
lbl_text.grid(row=0, column=0, columnspan=3)

lbl_input = ui.Label(height=1, text="Input your text here: ")
lbl_input.configure(font=("Helvetica", 12), anchor='e', justify=LEFT)
lbl_input.grid(row=1, column=0)

lbl_output = ui.Label(height=1, text="Your text will be output here: ")
lbl_output.configure(font=("Helvetica", 12), anchor='e', justify=LEFT)
lbl_output.grid(row=1, column=2)



txt_input = ui.Text(root)
txt_input.configure(wrap="word")
txt_input.grid(row=2, column=0)
txt_input.insert(1.0,
    """Enter the text you want converting here and then hit the button! If you want to change the type of conversion you're doing, click on that drop down box that's below this text box!

I hope you enjoy your time using this program! (Even if it is entirely cursed!)""")

txt_output = ui.Text()
txt_output.configure(state=DISABLED, wrap="word")
txt_output.grid(row=2, column=2)

option_list = [
    "L337",
    "RaNDom cApS",
    "OwO Speak"
]
selected = ui.StringVar(root)
selected.set(option_list[0])

opt_menu = ui.OptionMenu(root, selected, *option_list)
opt_menu.configure(width=40)
opt_menu.grid(row=3, column=0, columnspan=3)




btn_convert = ui.Button(root, text="Convert text!", command=convert)
btn_convert.configure(width=40)
btn_convert.grid(row=4, column=0, columnspan=3)

owo.owoify("test")

root.mainloop()



