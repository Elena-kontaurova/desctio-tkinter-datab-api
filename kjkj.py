import tkinter as tk
from tkinter import Scrollbar, Canvas, Frame
from poi import EmployeeCard
from main import sotrud  # Импортируем функцию sotrud из вашего модуля


def main():
    ''' kjjk'''
    # Создаем главное окно
    root = tk.Tk()
    root.title("Тест карточек сотрудников")
    root.geometry('600x600')  # Размер окна

    # Создаем Canvas для размещения карточек
    canvas = Canvas(root)
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    # Устанавливаем ScrollableFrame на Canvas
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Подключаем полосу прокрутки к Canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Упаковываем Canvas и Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Получаем данные сотрудников из функции sotrud
    employees_data = sotrud()

    # Создаем карточки для каждого сотрудника и добавляем их во scrollable_frame
    for employee in employees_data:
        card = EmployeeCard(scrollable_frame, employee)

    # Запускаем главный цикл
    root.mainloop()

if __name__ == "__main__":
    main()
