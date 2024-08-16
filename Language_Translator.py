from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x320')
root.resizable(0,0)
root.iconbitmap('logo_lt.ico')
root['bg'] = 'black'

root.title('Language Translator')
Label(root, text="Language Translator", font="arial 22 bold underline").pack()

Label(root,text="Enter your personalized texts", font="arial 13").place(x=105, y=90)

inp_text = Entry(root, width=60)
inp_text.place(x=30, y=130)
inp_text.get()

Label(root, text="Output", font="arial 12 bold").place(x=680,y=90)
op_text = Text(root, font="arial 20", height=5, wrap=WORD, padx=5, pady=5, width=35)
op_text.place(x=500, y=125)

language=list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=150, y=180)
dest_lang.set("choose language")

def Translate():
    translator = Translator()
    translated = translator.translate(text=inp_text.get(), dest=dest_lang.get())
    op_text.delete(1.0, END)
    op_text.insert(END, translated.text)

Button(root, text="Translate", font="arial 12 bold", pady=5, command=Translate, bg="skyblue", activebackground="yellow").place(x=345, y=180)

root.mainloop()
