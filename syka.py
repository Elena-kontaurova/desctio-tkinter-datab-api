'''fjfjfj'''
import tkinter as tk
from tkinter import PhotoImage, Label
from connect import Department

def gerate(frame):
    ''' jkjkj'''
    # root = tk.Tk()
    # root.title('Сука')
    # root.geometry('400x500')
    # root.resizable(False, False)

    fra = tk.Frame(frame, width=400, height=500)
    fra.grid(column=0, row=0)

    label = tk.Label(fra, text="один", background='green', width=25, height=2)
    label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    label2 = tk.Label(fra, text="два", background='green', width=25, height=2)
    label2.grid(row=1, column=0, padx=10)

    label3 = tk.Label(fra, text="три", background='green', width=25, height=2)
    label3.grid(row=1, column=1)

def sotrud(frame):
    ''' lklkl'''
    frame2 = tk.Frame(frame, width=400, height=120, background='green')
    frame2.grid(column=0, row=0, padx=10, pady=10)

    one = tk.Label(frame2, text="Лицензионный отдел", background='green')
    one.grid(row=0, column=0)
    two = tk.Label(frame2, text="Дирик", background='green')
    two.grid(row=0, column=1, padx=40)
    th = tk.Label(frame2, text="Контаурова Елена Сергеевна", background='green', font=('', 12))
    th.grid(row=1, column=0, columnspan=2, sticky="w")
    fo = tk.Label(frame2, text="+7 999 999 99 99", background='green')
    fo.grid(row=2, column=0, sticky="w")
    fi = tk.Label(frame2, text="www@mail.ru", background='green')
    fi.grid(row=2, column=1)
    s = tk.Label(frame2, text="1234", background='green', font=('', 8))
    s.grid(row=3, column=0, sticky="w")

    frame3 = tk.Frame(frame, width=400, height=120, background='green')
    frame3.grid(column=0, row=1, padx=10, pady=10)

    one = tk.Label(frame3, text="Лицензионный отдел", background='green')
    one.grid(row=0, column=0)
    two = tk.Label(frame3, text="Дирик", background='green')
    two.grid(row=0, column=1, padx=40)
    th = tk.Label(frame3, text="Контаурова Елена Сергеевна", background='green', font=('', 12))
    th.grid(row=1, column=0, columnspan=2, sticky="w")
    fo = tk.Label(frame3, text="+7 999 999 99 99", background='green')
    fo.grid(row=2, column=0, sticky="w")
    fi = tk.Label(frame3, text="www@mail.ru", background='green')
    fi.grid(row=2, column=1)
    s = tk.Label(frame3, text="1234", background='green', font=('', 8))
    s.grid(row=3, column=0, sticky="w")


aga = tk.Tk()
aga.geometry("800x600")

sosi0 = tk.Frame(aga, background='green', width=800, height=90)
sosi0.grid(row=0, column=0, columnspan=2)

logo_image = PhotoImage(file='Logo.png')
logo_image = logo_image.subsample(4)
logo_lable = Label(sosi0, image=logo_image, bg='green')
logo_lable.grid(row=0, column=0, sticky='w', padx=10)

pizda = tk.Frame(sosi0, background='white')
pizda.grid(column=0, row=0, columnspan=2, pady=10, padx=120)

text_label = tk.Label(pizda, text="Организационная структура", bg='white', fg='black', width=80)
text_label.grid(row=0, column=1, columnspan=2)

sosi1 = tk.Frame(aga, background='green', width=380, height=400)
sosi1.grid(row=1, column=0, pady=130, padx=30, sticky='n')
gerate(sosi1)

sosi2 = tk.Frame(aga, width=400, height=400)
sosi2.grid(row=1, column=1, pady=130, padx=30, sticky='n')
sotrud(sosi2)

# sosi3 = tk.Frame(aga, background='green', width=300, height=50)
# sosi3.grid(row=2, column=1)

def open_window():
    ''' kjkjs'''
    aaa = tk.Tk()
    aaa.geometry('500x500')
    aaa.mainloop()

bb = tk.Button(sosi2, command=open_window, text='+', background='green')
bb.grid(row=2, column=0, sticky='se', padx=10, pady=20)


def fetch_comments():
    ''' nkn'''
    comments = Department.select()
    return comments


aga.mainloop()
