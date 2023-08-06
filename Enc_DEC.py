from tkinter import *
import base64 
from tkinter import messagebox


def reset():
    enter.set("")
    text.delete(1.0, END)


def encode():
    password = enter.get()
    if password == "spark":
        x = Toplevel(root)
        x.title("Encoded text")
        x.geometry("400x200")

        message = text.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_byte = base64.b64encode(encode_message)
        encrypt = base64_byte.decode("ascii")

        Label(x, text="Encript").place(x=10, y=10)
        text2 = Text(x)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror(" ☠️☠ERROR  ☠️☠️ ", " 👉  Please enter password  ")
    elif password != "spark":
        messagebox.showerror(" ☠️☠ERROR ☠️☠️ ", "   👉    Wrong password")


def decode():
    password = enter.get()
    if password == "spark":
        x1 = Toplevel(root)
        x1.title("Decoded text")
        x1.geometry("400x200")

        message = text.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_byte = base64.b64decode(decode_message)
        decrypt = base64_byte.decode("ascii")

        Label(x1, text="decript").place(x=10, y=10)
        text2 = Text(x1)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)

    elif password == "" :
        messagebox.showerror(" ☠️☠ERROR ☠️☠️ ", "Please enter password")
    elif password != "spark":
        messagebox.showerror(" ☠️☠ERROR ☠️☠️ ", "Wrong password")


global enter

root = Tk()
root.geometry("480x480")
root.title("Encoding and Decoding")

Label(text="Enter ur message", font=(14)).place(x=150, y=10)

#   input box

text = Text(font=14, relief=GROOVE)
text.place(x=50, y=50, height=75, width=370)

Label(text="Enter ur password", font=12).place(x=150, y=135)

#  password entry

enter = StringVar()
Entry(textvariable=enter, font=14, show="#").place(x=50, y=175, height=30, width=370)

# encode button

e = PhotoImage(file='button.png')
Button(image=e, command=encode).place(x=50, y=255)

# decode button

d = PhotoImage(file='decode.png')
Button(image=d, command=decode).place(x=250, y=255)

#  Reset Button

p = PhotoImage(file='reset.png')
Button(image=p, command=reset).place(x=150, y=380)
root.mainloop()
