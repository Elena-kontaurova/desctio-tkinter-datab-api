''' файл для левой части таблицы'''
import tkinter as tk

class OrgChartApp:
    ''' рисуем блоки'''
    def __init__(self, frame):
        self.frame = frame

        # Создание Canvas для визуализации графа
        self.canvas = tk.Canvas(self.frame, bg='#DCDCDC', width=370, height=475)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Пример данных об организационной структуре
        self.departments = {
            "Дороги россии": ["Адми. департамент", "Ака. умные дороги"],
            "Ака. умные дороги": [],
            "Адми. департамент": ["Договорной отдел", "Общий отдел"],
            "Договорной отдел": [],
            "Общий отдел": ["Лецензионный отдел", "Управ. маркетинга"],
            "Лецензионный отдел": [],
            "Управ. маркетинга": []
        }

        # Актуальные размеры для размещения блоков
        self.block_width = 120
        self.block_height = 50
        self.vertical_gap = 60
        self.horizontal_gap = 20

        # Начинаем рисовать граф
        self.draw_org_chart()

    def draw_org_chart(self):
        ''' начальные координаиы'''
        x_offset = 150
        y_offset = 20
        self.draw_department("Дороги россии", x_offset, y_offset)

    def draw_department(self, department, x, y):
        '''' Рисуем блок для текущего отдела'''
        self.canvas.create_rectangle(
            x, y, x + self.block_width, y + self.block_height, fill='#D1FFA8')
        self.canvas.create_text(x + self.block_width / 2, y + self.block_height / 2,
                                text=department, font=('Helvetica', 8))

        sub_departments = self.departments.get(department, [])

        # Если есть подотделы, рисуем их
        if sub_departments:
            sub_x_start = x - ((
                len(sub_departments) - 1) * (self.block_width + self.horizontal_gap)) / 2
            sub_y = y + self.vertical_gap

            for i, sub_department in enumerate(sub_departments):
                sub_x = sub_x_start + i * (self.block_width + self.horizontal_gap)
                self.draw_department(sub_department, sub_x, sub_y)

                # Рисуем линию от текущего отдела к подотделу
                self.canvas.create_line(
                    x + self.block_width / 2,
                    y + self.block_height,
                    sub_x + self.block_width / 2,
                    sub_y
                )
