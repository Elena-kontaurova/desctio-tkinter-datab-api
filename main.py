''' главное окно'''
import tkinter as tk
from tkinter import Frame, PhotoImage, Label


window_main = tk.Tk()
window_main.geometry('800x600')
window_main.resizable(False, False)


frame_cap = Frame(window_main, background='#D1FFA8', height=80, width=800)
frame_cap.grid(row=0, column=0, columnspan=2)


logo_image = PhotoImage(file='logo.png')
logo_image = logo_image.subsample(3)
logo_label = tk.Label(frame_cap, image=logo_image, bg='#D1FFA8')
logo_label.pack(side=tk.LEFT, padx=30)

# Добавляем белый прямоугольник
rect_frame = Frame(frame_cap, background='white', width=600, height=40)
rect_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Добавляем текст в белый прямоугольник
text_label = Label(rect_frame, text="Организационная структура",
                   bg='white', fg='black')
text_label.pack(side=tk.LEFT, padx=235)


frame_left = Frame(window_main, background='#FFFFFF', height=520, width=400)
frame_left.grid(row=1, column=0)

frame_left_table = Frame(window_main, background='#DCDCDC',
                         height=480, width=370)
frame_left_table.grid(row=1, column=0)

frame_right = Frame(window_main, background='#FFFFFF', height=520, width=400)
frame_right.grid(row=1, column=1)

frame_right_table = Frame(window_main, background='#DCDCDC',
                          height=480, width=370)
frame_right_table.grid(row=1, column=1)


window_main.mainloop()
