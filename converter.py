from Tkinter import *

window = Tk()

def convert_btn_click_listener():

    gram_text.delete('1.0', END)
    kg_text.delete('1.0', END)
    pound_text.delete('1.0', END)
    try:
        gram_text.insert(INSERT ,e1_value.get() * 1000)
        kg_text.insert(INSERT,e1_value.get())
        pound_text.insert(INSERT,e1_value.get() * 2.20462)
    except:
        e1_value.set(0)


e1_value = IntVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=1,column=1)

btn = Button(window, command=convert_btn_click_listener, text="convert")
btn.grid(row=1, column=2)

gram_text = Text(window,height=1,width=20)
gram_text.grid(row=2,column=1)

kg_text = Text(window,height=1,width=20)
kg_text.grid(row=2,column=2)

pound_text = Text(window,height=1,width=20)
pound_text.grid(row=2,column=3)





window.mainloop()
