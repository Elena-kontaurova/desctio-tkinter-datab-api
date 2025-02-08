'''' ЗАПИСУК ОСВНОЙ'''
import tkinter as tk
from tkinter import messagebox, Frame, PhotoImage, Label, Scrollbar, Canvas
import requests
from jkjk import OrgChartApp
from main import sotrud  # Импортируйте вашу функцию sotrud
from poi import EmployeeCard


API_URL = "http://127.0.0.1:8000/api/v1/SignIn"

def open_success_window():
    '''Открывает окно с успешным входом'''
    window_main = tk.Toplevel(root)  # Использует Toplevel для нового окна
    window_main.geometry('800x600')
    window_main.resizable(False, False)

    frame_cap = Frame(window_main, background='#D1FFA8', height=80, width=800)
    frame_cap.grid(row=0, column=0, columnspan=2)

    logo_image = PhotoImage(file='logo.png')  # Замените на свой путь к изображению
    logo_image = logo_image.subsample(3)  # Уменьшение размера изображения
    logo_label = Label(frame_cap, image=logo_image, bg='#D1FFA8')
    logo_label.image = logo_image  # Храним ссылку на изображение, чтобы оно не удалялось
    logo_label.pack(side=tk.LEFT, padx=30)

    # Добавляем белый прямоугольник с текстом
    rect_frame = Frame(frame_cap, background='white', width=600, height=40)
    rect_frame.pack(side=tk.LEFT, padx=10, pady=10)

    text_label = Label(rect_frame, text="Организационная структура", bg='white', fg='black')
    text_label.pack(side=tk.LEFT, padx=235)

    # Создание основных фреймов
    frame_left = Frame(window_main, background='#FFFFFF', height=520, width=400)
    frame_left.grid(row=1, column=0)

    frame_left_table = Frame(window_main, background='#DCDCDC', height=480, width=370)
    frame_left_table.grid(row=1, column=0)
    OrgChartApp(frame_left_table)

    frame_right = Frame(window_main, background='#FFFFFF', height=520, width=400)
    frame_right.grid(row=1, column=1)

    frame_right_table = Frame(window_main, background='#DCDCDC', height=480, width=370)
    frame_right_table.grid(row=1, column=1)

    # Создаем Canvas для размещения карточек
    canvas = Canvas(frame_right_table, width=360, height=480)
    scrollbar = Scrollbar(frame_right_table, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    # Устанавливаем ScrollableFrame на Canvas
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Подключаем полосу прокрутки к Canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Упаковываем Canvas и Scrollbar в фрейм
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Получаем данные сотрудников из функции sotrud
    employees_data = sotrud()

    # Создаем карточки для каждого сотрудника и добавляем их во scrollable_frame
    for employee in employees_data:

        _ = EmployeeCard(scrollable_frame, employee)

    window_main.protocol("WM_DELETE_WINDOW", close_program)



def close_program():
    '''Закрывает основное окно приложения'''
    root.destroy()


def sign_in():
    '''Обрабатывает вход пользователя'''
    name = username_entry.get()
    password = password_entry.get()

    try:
        # Отправка POST запроса
        response = requests.post(API_URL, json={"name": name, "password": password}, timeout=5)

        # Обработка ответа от сервера
        if response.status_code == 200:
            open_success_window()  # Открываем новое окно
            root.withdraw()  # Скрываем текущее окно
        else:
            messagebox.showerror("Ошибка", response.json().get("detail", "Ошибка при входе"))

    except requests.ConnectionError:
        messagebox.showerror("Ошибка соединения", "Не удалось соединиться с сервером.")
    except requests.Timeout:
        messagebox.showerror("Ошибка", "Запрос превысил время ожидания.")

# Основное окно приложения
root = tk.Tk()
root.title("Авторизация")
root.geometry('800x600')

# Создание виджетов для ввода данных
username_label = tk.Label(root, text="Имя пользователя:")
username_label.pack(pady=5)

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Пароль:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)
login_button = tk.Button(root, text="Войти", command=sign_in)
login_button.pack(pady=20)

# Запуск главного цикла
root.mainloop()
