from tkinter import *
import random , string
import pyperclip

web = Tk()
web.geometry("400x300")
web.resizable(0,0)
web.title("PYTHON PROJECT  -  CAPTCHA GENERATOR")

Label(web,text = 'Captcha Generator', font = 'arial 20 bold').pack()
Label(web,text = "________",  font = 'arial 20 bold').pack(side = BOTTOM)

pass_label = Label(web,text = "CAPTCHA LENGTH", font = 'arial 20 bold').pack()
pass_len = IntVar()
lenght = Spinbox(web, from_ =6, to_ = 30, textvariable=pass_len, width = 15).pack()
pass_str = StringVar()

def Generator():
    captcha = []

    if pass_len.get() >=4:
        captcha.append(random.choice(string.ascii_uppercase))
        captcha.append(random.choice(string.digits))
        captcha.append(random.choice(string.punctuation))
        captcha.append(random.choice(string.ascii_lowercase))

        for i in range(pass_len.get()-4):
            captcha.append(random.choice(string.ascii_uppercase + string.digits + string.punctuation + string.ascii_lowercase))

        random.shuffle(captcha)
    else:
        for _ in range(pass_len.get()):
            captcha.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))

    pass_str.set(''.join(captcha))
def Copy_captcha():
    pyperclip.copy(pass_str.get())
Button(web, text = "GENERATE CAPTCHA", command = Generator).pack(pady=5)
Entry(web, textvariable = pass_str).pack()
Button(web, text = 'COPY TO CLIPBOARD', command = Copy_captcha).pack(pady = 5)

web.mainloop()