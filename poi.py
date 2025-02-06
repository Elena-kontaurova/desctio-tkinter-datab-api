''' jkjkjkjkj'''
import tkinter as tk


class EmployeeCard:
    ''' kjkjk'''
    def __init__(self, master, employee_data):
        self.master = master
        self.employee_data = employee_data

        # Создаем внешний фрейм для карточки с фиксированными размерами
        self.card_frame = tk.Frame(self.master,
                                   relief='sunken', borderwidth=2, pady=10,
                                   padx=10, bg='#D1FFA8', width=300, height=150)
        self.card_frame.pack_propagate(False)  # Отключаем автоматическое изменение размера
        self.card_frame.pack(padx=10, pady=5)

        self.display_employee_info()

    def display_employee_info(self):
        ''' Отображаем информацию о сотруднике на карточке '''
        department = self.employee_data['department']
        post = self.employee_data['post']
        fcs = self.employee_data['fcs']
        work_phone = self.employee_data['work_phone']
        cor_email = self.employee_data['cor_email']
        office = self.employee_data['office']

        # Форматирование информации на карточке
        label_title = f"{department} - {post}"
        label_name = f"{fcs}"
        _ = f"{work_phone} | {cor_email}"
        label_office = f"Кабинет: {office}"

        # Устанавливаем метки для отображения информации
        title_label = tk.Label(self.card_frame, text=label_title, 
                               bg='#D1FFA8', anchor='w', font=("Arial", 10, 'bold'))
        title_label.pack(fill='x')  # Заголовок занимает всю ширину

        name_label = tk.Label(self.card_frame, text=label_name, bg='#D1FFA8', anchor='w')
        name_label.pack(fill='x')

        contact_frame = tk.Frame(self.card_frame, bg='#D1FFA8')  # Фрейм для контактов
        contact_frame.pack(fill='x')

        # Создаем метки для телефона и почты
        phone_label = tk.Label(contact_frame, text=work_phone, bg='#D1FFA8', anchor='w')
        phone_label.pack(side='left', padx=5)

        email_label = tk.Label(contact_frame, text=cor_email, bg='#D1FFA8', anchor='w')
        email_label.pack(side='left', padx=5)

        office_label = tk.Label(self.card_frame, text=label_office, bg='#D1FFA8', anchor='w')
        office_label.pack(fill='x')
