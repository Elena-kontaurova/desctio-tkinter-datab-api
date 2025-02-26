from connect import Department
import tkinter as tk


root = tk.Tk()
root.geometry('1424x500')

frame_jk = tk.Frame(root, background='green', height=30, width=1424)
frame_jk.pack(side='top')

frame_text = tk.Frame(root, background='gray', width=150, height=20)
frame_text.pack(side='top', pady=10, anchor='w', padx=135)

test = tk.Label(frame_text, text='Сотрудники', font=('Arial', 13))
test.pack()

frame = tk.Frame(root)
frame.pack()

def get_dep():
    ''' nkn'''
    dec = Department.select()
    return dec

def display():
    ''' klkl'''

    dec = get_dep()

    for sep in dec:
        frame_one = tk.Frame(frame, width=100, height=10, padx=1, pady=7)
        frame_one.pack(side='left', padx=1, pady=10)

        description = tk.Label(frame_one, text=f'{sep.description}', bg='green', fg='white', width=40, font=('', 9),
                               wraplength=110)
        description.pack(padx=10)
        director = tk.Label(frame_one, text=f'{sep.director}', bg='green', fg='white', width=45, font=('', 7),
                            wraplength=110)
        director.pack()
        assistant = tk.Label(frame_one, text=f'{sep.assistant}', bg='green', fg='white', width=45, font=('', 7),
                             wraplength=110)
        assistant.pack()

display()
root.mainloop()
