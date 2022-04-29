from tkinter import *
from tkinter import messagebox


def click():
    username = username_entry.get()
    password = password_entry.get()

    messagebox.showinfo('Авторизация успешно прошла', f'{username}, {password}')


root = Tk()
root.title('Авторизация')
root.geometry('450x230')



main_label = Label(root, text='Авторизация daniil windows')
main_label.pack()

username_label = Label(root, text='Имя пользователя')
username_label.pack()

username_entry = Entry(root)
username_entry.pack()

password_label = Label(root, text='Пароль')
password_label.pack()

password_entry = Entry(root)
password_entry.pack()

send_btn = Button(root, text='Войти', command=click)
send_btn.pack(padx=10, pady=8)

root.mainloop()