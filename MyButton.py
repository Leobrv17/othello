import tkinter as tk


class MyButton(tk.Button):
    def __init__(self, master, texte, fonction):
        tk.Button.__init__(self)
        self.configure(text=texte, command=fonction)
        self.configure(height=1,
                       width=10,
                       bg='#347940',
                       fg='white',
                       font=('Calibri', 10, 'bold'))