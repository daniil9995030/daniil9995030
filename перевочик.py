from tkinter import *
from googletrans import Translator


translator = Translator()
print (translator.translate("text", dest='ru', src='auto'))
print (translator.translate("text", dest='en', src='auto'))
print (translator.translate("text", dest='en', src='auto'))
print (translator.translate("text", dest='ru', src='auto'))
def tran():
    text = t.get('1.0', END)
    text = t.get('1.0', END)
    print (F"Text to translate: {text}")
    print (F"Text to translate: {text}")
    v= translator.translate(text, src ="auto", dest = "ru")
    a= translator.translate(text, src ="auto", dest = "en")
    a= translator.translate(text, src ="auto", dest = "en")   
    a= translator.translate(text, src ="auto", dest = "ru")
   
   
    
    
    t.delete('1.0', END)
    t1.delete('1.0', END)
    t1.insert('1.0', a.text)
    


root = Tk()
root.geometry('500x350')
root.title('Переводчик danik')
root.resizable(width=False, height=False)
root['bg'] = 'black'
translator = Translator()

label = Label(root, fg='white', bg='black', font='Arial 15 bold', text='Введите текст на английском')
label.place(relx=0.5, y=30, anchor=CENTER)
t = Text(root, width=35, height=5, font='Arial 12 bold')
t.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text='Перевести', command=tran)
btn.place(relx=0.5, y=180, anchor=CENTER)

t1 = Text(root, width=35, height=5, font='Arial 12 bold')
t1.place(relx=0.5, y=260, anchor=CENTER)

root.mainloop()
