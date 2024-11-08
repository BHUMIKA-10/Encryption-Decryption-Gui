from tkinter import *
import tkinter.messagebox as tmsg
import base64


def encrypt():
    password=code.get()

    if password=="1234":
        screen = Toplevel(root)
        screen.title("Encryption")
        screen.geometry("400x200")
        screen.configure(bg="red")

        message =text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen,text="Encrypted Text",fg="black",background="White",font="lucida 10 bold").place(x=10,y=10)
        text2=Text(screen,font="lucida 10 bold",background="white",relief=GROOVE,bd=0,wrap=WORD,fg="black")
        text2.place(x=10,y=40,width=380,height=100)

        text2.insert(END,encrypt)

    elif password=="":
        tmsg.showerror("Encryption","Input Password")

    elif password !="1234":
        tmsg.showerror("Encryption","Invalid Password")

    
    
def decrypt():
    password=code.get()

    if password=="1234":
        screen1 = Toplevel(root)
        screen1.title("Decryption")
        screen1.geometry("400x200")
        screen1.configure(bg="forestgreen")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen1,text="Decrypted Text :",font="lucida 10 bold",fg="Black",background="White").place(x=10,y=10)
        text2=Text(screen1,font="lucida 10 bold",background="white",relief=GROOVE,bd=0,wrap=WORD,fg="Black")
        text2.place(x=10,y=40,width=380,height=100)

        text2.insert(END,decrypt)

    elif password=="":
        tmsg.showerror("Decryption","Input Password")

    elif password !="1234":
        tmsg.showerror("Decryption","Invalid Password")

def reset():
    code.set("")
    text1.delete(1.0,END)

global text1
global code
root=Tk()
root.geometry("375x398")
root.title("Encryption and Decryption app")
root.wm_iconbitmap("keys.ico")

Label(root,text="Enter text for Encryption and Decryption : ",font="lucida 11 bold",fg="black").place(x=10,y=10)
text1 =Text(font="robote 20",background="white",relief=GROOVE,wrap=WORD,bd=0)
text1.place(x=10,y=50,width=355,height=100)


Label(root,text="Enter secret key for Encryption and Decryption : ",font="lucida 11 bold",fg="black").place(x=10,y=170)
code=StringVar()
Entry(textvariable=code,width=19,bd=0,font="arial 25",show="*").place(x=10,y=200)


Button(root,text="ENCRYPT",background="red",height=2,width=23,fg="white",command=encrypt).place(x=10,y=250)
Button(root,text="DECRYPT",background="forestgreen",height=2,width=23,fg="white",command=decrypt).place(x=200,y=250)
Button(root,text="RESET",background="dodgerblue",height=2,width=50,fg="white",command=reset).place(x=10,y=300)
root.mainloop()